#!/usr/bin/env python3
"""
EINMALIG AUSFÜHREN – setzt last_processed_tournament auf das aktuell
neueste abgeschlossene Turnier.
"""

import json
import os
import requests

TEAM_ID      = "solo-ultrabullet-league"
RANKING_FILE = "ranking.json"
API_BASE     = "https://lichess.org/api"
TOKEN        = os.environ["LICHESS_TOKEN"]

HEADERS_NDJSON = {"Authorization": f"Bearer {TOKEN}", "Accept": "application/x-ndjson"}


def main():
    with open(RANKING_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)

    print("Fetching tournament list …")
    url = f"{API_BASE}/team/{TEAM_ID}/arena"
    resp = requests.get(url, headers=HEADERS_NDJSON, timeout=30)
    resp.raise_for_status()

    tournaments = []
    for line in resp.text.strip().splitlines():
        line = line.strip()
        if line:
            tournaments.append(json.loads(line))

    if not tournaments:
        print("❌ No tournaments found at all.")
        return

    print(f"Found {len(tournaments)} tournaments total.")
    print("\n--- First 3 tournaments (raw fields) ---")
    for t in tournaments[:3]:
        print(json.dumps(t, indent=2))
        print("---")

    # Try to find latest finished one using all possible fields
    latest = None
    for t in tournaments:
        tid = t.get("id")
        # Check every possible "finished" indicator
        is_done = (
            t.get("isFinished") is True
            or t.get("status") == "finished"
            or t.get("status") == 30          # Lichess internal status code for finished
            or t.get("secondsToFinish") == 0
            or ("winner" in t)
        )
        if is_done:
            latest = t
            break  # API returns newest first, so first finished = latest

    if not latest:
        # Fallback: just take the first one (newest) regardless
        print("\n⚠️  Could not detect finished status — using newest tournament as checkpoint.")
        latest = tournaments[0]

    tid   = latest["id"]
    tname = latest.get("fullName", tid)
    print(f"\n✅ Checkpoint set to: {tname} ({tid})")

    data["last_processed_tournament"] = tid

    with open(RANKING_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"💾 Saved to {RANKING_FILE}. Done!")


if __name__ == "__main__":
    main()
