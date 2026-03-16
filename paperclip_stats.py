#!/usr/bin/env python3
"""Paperclip stats tracker - simple CLI for tracking paperclip counts."""

import json
import os
from datetime import datetime
from pathlib import Path

STATS_FILE = Path.home() / ".paperclip_stats.json"

def load_stats():
    if STATS_FILE.exists():
        with open(STATS_FILE) as f:
            return json.load(f)
    return {"count": 0, "history": []}

def save_stats(stats):
    with open(STATS_FILE, "w") as f:
        json.dump(stats, f, indent=2)

def add(n=1):
    stats = load_stats()
    stats["count"] += n
    stats["history"].append({"action": "add", "amount": n, "timestamp": datetime.now().isoformat()})
    save_stats(stats)
    print(f"Added {n} paperclip(s). Total: {stats['count']}")

def remove(n=1):
    stats = load_stats()
    stats["count"] = max(0, stats["count"] - n)
    stats["history"].append({"action": "remove", "amount": n, "timestamp": datetime.now().isoformat()})
    save_stats(stats)
    print(f"Removed {n} paperclip(s). Total: {stats['count']}")

def show():
    stats = load_stats()
    print(f"Paperclip count: {stats['count']}")
    if stats["history"]:
        print(f"Last action: {stats['history'][-1]['action']}")

if __name__ == "__main__":
    import sys
    cmd = sys.argv[1] if len(sys.argv) > 1 else "show"
    n = int(sys.argv[2]) if len(sys.argv) > 2 else 1
    
    if cmd == "add":
        add(n)
    elif cmd == "remove":
        remove(n)
    else:
        show()
