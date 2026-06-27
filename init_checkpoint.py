#!/usr/bin/env python3
"""
EINMALIG AUSFÜHREN – setzt Checkpoint für alle (oder eine) Liga(en).

Setzt last_processed_tournament auf das neueste ABGESCHLOSSENE Turnier,
damit der Bot ab sofort alle ZUKÜNFTIGEN Turniere verarbeitet.

Usage:
    LICHESS_TOKEN=xxx python init_checkpoint.py
    LICHESS_TOKEN=xxx python init_checkpoint.py bullet
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


def fetch_all_finished(team_id):
    """Holt ALLE abgeschlossenen Turniere (paginiert über nb-Parameter)."""
    tournaments = []
    resp = requests.get(
        f"{API_BASE}/team/{team_id}/arena",
        params={"status": 30, "nb": 100},
        headers=HEADERS_NDJSON,
        timeout=30,
    )
    resp.raise_for_status()
    for line in resp.text.strip().splitlines():
        line = line.strip()
        if line:
            tournaments.append(json.loads(line))
    return tournaments


def set_checkpoint(key, team_id):
    path = f"ranking_{key}.json"
    print(f"\n--- {key} ({team_id}) ---")

    # Ranking-Datei laden
    if not os.path.exists(path):
        print(f"  ⚠️  {path} nicht gefunden – übersprungen.")
        return

    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

    # Alle abgeschlossenen Turniere holen
    tournaments = fetch_all_finished(team_id)
    if not tournaments:
        print("  ⚠️  Keine abgeschlossenen Turniere gefunden.")
        print("  ℹ️  Setze last_processed_tournament auf null – alle zukünftigen Turniere werden verarbeitet.")
        data["last_processed_tournament"] = None
    else:
        # Checkpoint = neuestes abgeschlossenes Turnier
        # → Bot verarbeitet ab jetzt nur noch NEUE (zukünftige) Turniere
        latest = tournaments[0]
        tid = latest["id"]
        name = latest.get("fullName", tid)
        print(f"  ✅ Letztes abgeschlossenes Turnier: {name} ({tid})")
        print(f"  ℹ️  Alle zukünftigen Turniere werden ab jetzt verarbeitet.")
        data["last_processed_tournament"] = tid

    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"  💾 Gespeichert: {path}")


def main():
    if len(sys.argv) > 1:
        key = sys.argv[1]
        if key not in LEAGUES:
            print(f"❌ Unbekannte Liga: {key}")
            print(f"   Verfügbar: {', '.join(LEAGUES.keys())}")
            sys.exit(1)
        to_run = {key: LEAGUES[key]}
    else:
        to_run = LEAGUES

    for key, team_id in to_run.items():
        set_checkpoint(key, team_id)

    print("\n✅ Fertig! Der Bot verarbeitet ab jetzt alle neuen Turniere.")


if __name__ == "__main__":
    main()
