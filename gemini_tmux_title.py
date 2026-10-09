#!/usr/bin/env python3

import json
import os
from pathlib import Path
import re
import subprocess
import sys
from urllib.parse import urlsplit


def url_label(match):
    parts = [part for part in urlsplit(match.group(0)).path.split("/") if part]
    for part in parts:
        if re.fullmatch(r"[A-Za-z]+-\d+", part):
            return part
    named = [part for part in parts if re.search(r"[A-Za-z]", part)]
    return named[-1] if named else ""


def clean_title(text):
    # Remove outer tags like <USER_REQUEST> if present
    match = re.search(r"<USER_REQUEST>(.*?)</USER_REQUEST>", text, re.DOTALL)
    if match:
        text = match.group(1).strip()
    # Replace URLs with short labels
    title = re.sub(r"https?://\S+", url_label, text)
    # Strip special formatting characters
    title = " ".join(re.sub(r"[^\w .,:!?'/()-]", " ", title).split())
    if len(title) > 60:
        title = title[:61].rsplit(" ", 1)[0][:60]
    return title.strip()


def extract_first_prompt(transcript_path):
    if not transcript_path or not os.path.isfile(transcript_path):
        return None
    try:
        with open(transcript_path, "r", encoding="utf-8") as f:
            for line in f:
                if not line.strip():
                    continue
                data = json.loads(line)
                if data.get("type") == "USER_INPUT":
                    content = data.get("content", "")
                    if content:
                        return clean_title(content)
    except Exception:
        pass
    return None


def main():
    # Always respond with a valid PreInvocation JSON contract
    response = {"injectSteps": []}
    
    try:
        raw_input = sys.stdin.read()
        event = json.loads(raw_input) if raw_input.strip() else {}
    except Exception:
        event = {}

    pane = os.environ.get("TMUX_PANE")
    socket = os.environ.get("TMUX", "").split(",", 1)[0]

    if pane and socket and event:
        transcript_path = event.get("transcriptPath")
        title = extract_first_prompt(transcript_path)
        if title:
            tmux = ["tmux", "-S", socket]
            try:
                current = subprocess.run(
                    tmux + ["show-options", "-pqv", "-t", pane, "@agent_title"],
                    capture_output=True, text=True, timeout=1,
                ).stdout.strip()
                if current != title:
                    subprocess.run(
                        tmux + ["set-option", "-p", "-t", pane, "@agent_title", title],
                        check=True, capture_output=True, timeout=1,
                    )
                    # Trigger the tmux pane-title-changed hook
                    subprocess.run(
                        tmux + ["set-hook", "-R", "-t", pane, "pane-title-changed"],
                        capture_output=True, timeout=1,
                    )
            except Exception:
                pass

    json.dump(response, sys.stdout)


if __name__ == "__main__":
    main()
