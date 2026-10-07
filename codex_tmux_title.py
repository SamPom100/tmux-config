#!/usr/bin/env python3

import json
import os
from pathlib import Path
import re
import sqlite3
import subprocess
import sys


def main():
    pane = os.environ.get("TMUX_PANE")
    socket = os.environ.get("TMUX", "").split(",", 1)[0]
    if not pane or not socket:
        return

    event = json.load(sys.stdin)
    transcript = event.get("transcript_path")
    if not transcript:
        return
    with open(transcript, encoding="utf-8") as stream:
        metadata = json.loads(stream.readline()).get("payload", {})
    if metadata.get("source") != "cli" or metadata.get("id") != event.get("session_id"):
        return

    codex_home = Path(os.environ.get("CODEX_HOME", Path.home() / ".codex"))
    database = codex_home / "goals_1.sqlite"
    title = ""
    if database.is_file():
        with sqlite3.connect(database.resolve().as_uri() + "?mode=ro", uri=True, timeout=0.2) as connection:
            goal = connection.execute(
                "SELECT objective FROM thread_goals WHERE thread_id = ?",
                (event["session_id"],),
            ).fetchone()
        if goal:
            title = re.sub(r"https?://\S+", "", goal[0])
            title = " ".join(re.sub(r"[^\w .,:!?'/()-]", " ", title).split())
            if len(title) > 80:
                title = title[:81].rsplit(" ", 1)[0][:80]

    tmux = ["tmux", "-S", socket]
    current = subprocess.run(
        tmux + ["show-options", "-pqv", "-t", pane, "@codex_goal_title"],
        check=True, capture_output=True, text=True, timeout=2,
    ).stdout.rstrip("\n")
    if current == title:
        return
    subprocess.run(
        tmux + ["set-option", "-p", "-t", pane, "@codex_goal_title", title],
        check=True, capture_output=True, timeout=2,
    )
    subprocess.run(
        tmux + ["set-hook", "-R", "-t", pane, "pane-title-changed"],
        check=True, capture_output=True, timeout=2,
    )


if __name__ == "__main__":
    try:
        main()
    except (OSError, ValueError, TypeError, sqlite3.Error, subprocess.SubprocessError):
        pass
