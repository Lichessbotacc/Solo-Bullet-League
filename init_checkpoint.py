#!/usr/bin/env python3
"""
EINMALIG AUSFÜHREN – setzt last_processed_tournament auf das aktuell
neueste abgeschlossene Turnier, sodass das Hauptscript nur zukünftige
Turniere verarbeitet.

Ausführen mit:
    LICHESS_TOKEN=dein_token python3 init_checkpoint.py
"""

import json
import os
import requests

TEAM_ID      = "solo-ultrabullet-league"
RANKING_FILE = "ranking.json"
API_BASE     = "https://lichess.org/api"
TOKEN        = os.environ["LICHESS_TOKEN"]

HEADERS_NDJSON = {"Authorization": f"Bearer {TOKEN}", "Accept": "application/x-ndjson"}

def get_latest_finished_tournament() -> dict | None:
    url = f"{API_BASE}/team/{TEAM_ID}/arena"
    resp = requests.get(url, headers=HEADERS_NDJSON, timeout=30)
    resp.raise_for_status()

    latest = None
    for line in resp.text.strip().splitlines():
        line = line.strip()
        if not line:
            continue
        t = json.loads(line)
        if t.get("status") == "finished":
            # API returns newest first — so first finished one is the latest
            if latest is None:
                latest = t
            else:
                # compare by startsAt
                if t.get("startsAt", 0) > latest.get("startsAt", 0):
                    latest = t
    return latest

def main():
    with open(RANKING_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)

    print("Fetching tournament list …")
    latest = get_latest_finished_tournament()

    if not latest:
        print("❌ No finished tournaments found.")
        return

    tid   = latest["id"]
    tname = latest.get("fullName", tid)
    print(f"✅ Latest finished tournament: {tname} ({tid})")
    print(f"   Setting this as checkpoint — all future tournaments will be processed.")

    data["last_processed_tournament"] = tid

    with open(RANKING_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"💾 Saved to {RANKING_FILE}. You're good to go!")

if __name__ == "__main__":
    main()
