#!/usr/bin/env python3
from datetime import datetime, timezone
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parents[2]
SCHEDULE_FILE=ROOT/".github/maintenance/schedule.json"
README_FILE=ROOT/"README.md"

def add_section(title,text):
    if not README_FILE.exists(): return False
    current=README_FILE.read_text(encoding="utf-8")
    marker=f"## {title.title()}"
    if marker in current: return False
    README_FILE.write_text(current.rstrip()+f"\n\n{marker}\n\n{text}\n",encoding="utf-8")
    return True

def main():
    schedule=json.loads(SCHEDULE_FILE.read_text(encoding="utf-8"))
    task=schedule.get(datetime.now(timezone.utc).date().isoformat())
    if not task: return 0
    sections={
        "development_workflow": ("development workflow", "Add a simple Django development workflow for Accord-HMS."),
        "testing_notes": ("testing notes", "Document the existing Django check and test commands."),
    }
    title,text=sections[task["task_id"]]
    add_section(title,text)
    return 0

if __name__=="__main__":
    raise SystemExit(main())
