#!/usr/bin/env python3

import json
import re
import sys
from urllib.parse import urlsplit

GOAL_CLEAR_WORDS = {"clear", "stop", "off", "reset", "none", "cancel"}
TYPED_GOAL = re.compile(r"\s*/goal(?:\s+(.*?))?\s*$", re.DOTALL)
LOGGED_GOAL = re.compile(
    r"<command-name>/goal</command-name>.*?<command-args>(.*?)</command-args>", re.DOTALL
)


def url_label(match):
    parts = [part for part in urlsplit(match.group(0)).path.split("/") if part]
    for part in parts:
        if re.fullmatch(r"[A-Za-z]+-\d+", part):
            return part
    named = [part for part in parts if re.search(r"[A-Za-z]", part)]
    return named[-1] if named else ""


def usable(condition):
    if condition and condition.strip().lower() not in GOAL_CLEAR_WORDS:
        return condition
    return None


def goal_from_transcript(path):
    with open(path, encoding="utf-8") as stream:
        for line in stream:
            if '"type":"user"' not in line or "<command-name>/goal</command-name>" not in line:
                continue
            content = json.loads(line).get("message", {}).get("content")
            if not isinstance(content, str):
                continue
            match = LOGGED_GOAL.search(content)
            condition = usable(match.group(1)) if match else None
            if condition:
                return condition
    return None


def main():
    event = json.load(sys.stdin)
    if event.get("session_title"):
        return

    match = TYPED_GOAL.match(event.get("prompt") or "")
    condition = usable(match.group(1)) if match else None
    if not condition and event.get("transcript_path"):
        condition = goal_from_transcript(event["transcript_path"])
    if not condition:
        return

    title = re.sub(r"https?://\S+", url_label, condition)
    title = " ".join(re.sub(r"[^\w .,:!?'/()-]", " ", title).split())
    if len(title) > 80:
        title = title[:81].rsplit(" ", 1)[0][:80]
    if not title:
        return

    json.dump(
        {"hookSpecificOutput": {"hookEventName": "UserPromptSubmit", "sessionTitle": title}},
        sys.stdout,
    )


if __name__ == "__main__":
    try:
        main()
    except (OSError, ValueError, TypeError, AttributeError):
        pass
