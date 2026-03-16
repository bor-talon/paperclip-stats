#!/usr/bin/env python3
"""Simple ASCII chart for paperclip stats."""

def print_chart(count):
    print(f"\n📎 Paperclip Count: {count}\n")
    bar = "█" * min(count, 50)
    print(f"[{bar}]")
    if count > 50:
        print(f"  (+{count - 50} more)")
    print()

if __name__ == "__main__":
    import sys
    count = int(sys.argv[1]) if len(sys.argv) > 1 else 0
    print_chart(count)
