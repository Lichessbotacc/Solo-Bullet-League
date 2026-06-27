#!/usr/bin/env python3
"""
EINMALIG AUSFÜHREN – setzt Checkpoint für alle (oder eine) Liga(en).

Usage:
    LICHESS_TOKEN=xxx python init_checkpoint.py
    LICHESS_TOKEN=xxx python init_checkpoint.py ultrabullet
"""

import json, os, sys, requests

LEAGUES = {
    "ultrabullet": "solo-ultrabullet-league",
    "bullet":      "solo-bullet-league",
    "blitz":       "solo-blitz-league",
    "rapid":       "solo-rapid-league",
}

API_BASE       = "https://lichess.org/api"
TOKEN          = os.environ["LICHESS_TOKEN"]
HEADERS_NDJSON = {"Authorization": f"Bearer {TOKEN}", "Accept": "application/x-ndjson"}


def set_checkpoint(key, team_id):
    path = f"ranking_{key}.json"
    print(f"\n--- {key} ({team_id}) ---")
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

    resp = requests.get(f"{API_BASE}/team/{team_id}/arena?status=30",
                        headers=HEADERS_NDJSON, timeout=30)
    resp.raise_for_status()
    tournaments = [json.loads(l) for l in resp.text.strip().splitlines() if l.strip()]

    if not tournaments:
        print("  ⚠️  No finished tournaments found.")
        return

    latest = tournaments[0]
    tid = latest["id"]
    print(f"  ✅ Checkpoint → {latest.get('fullName', tid)} ({tid})")
    data["last_processed_tournament"] = tid

    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"  💾 Saved {path}")


def main():
    to_run = {sys.argv[1]: LEAGUES[sys.argv[1]]} if len(sys.argv) > 1 else LEAGUES
    for key, team_id in to_run.items():
        set_checkpoint(key, team_id)
    print("\n✅ Done!")

if __name__ == "__main__":
    main()
