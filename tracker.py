#!/usr/bin/env python3
"""Cyberbeast Fund Tracker - CLI tool to keep making money and track progress toward TWO Cyberbeasts."""

import json
import os
from datetime import datetime

GOAL = 220000  # USD for two loaded Cyberbeasts
DATA_FILE = "fund.json"


def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return {"total": 0, "logs": []}

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)

def add_revenue(amount, note=""):
    data = load_data()
    data["total"] += amount
    data["logs"].append({
        "date": datetime.now().isoformat(),
        "amount": amount,
        "note": note
    })
    save_data(data)
    print(f"Added ${amount:,.0f}. New total: ${data['total']:,.0f}")
    progress = (data['total'] / GOAL) * 100
    print(f"Progress to two Cyberbeasts: {progress:.1f}% (${GOAL - data['total']:,.0f} to go)")
    if data['total'] >= 110000 and data['total'] < 220000:
        print("🎯 MILESTONE: Enough for Cyberbeast #1. Order it!")
    if data['total'] >= GOAL:
        print("🚀🚀 TWO CYBERBEASTS FUNDED. GO ORDER THEM NOW: https://www.tesla.com/cybertruck/design")

def show_status():
    data = load_data()
    print("\n=== CYBERBEAST FUND STATUS ===")
    print(f"Banked: ${data['total']:,.0f}")
    print(f"Goal (2x Cyberbeast): ${GOAL:,}")
    pct = min((data['total'] / GOAL) * 100, 100)
    print(f"Progress: {pct:.1f}%")
    print("\nRecent logs:")
    for log in data["logs"][-5:]:
        print(f"  {log['date'][:10]} +${log['amount']:,} - {log['note']}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        if sys.argv[1] == "add":
            amt = float(sys.argv[2]) if len(sys.argv) > 2 else 0
            note = " ".join(sys.argv[3:]) or "Revenue hit"
            add_revenue(amt, note)
        elif sys.argv[1] == "status":
            show_status()
    else:
        print("Usage:")
        print("  python tracker.py status")
        print("  python tracker.py add 5000 'Client project payout'")
        print("\nKeep making money. Order the two Cyberbeast.")