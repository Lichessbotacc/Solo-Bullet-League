#!/usr/bin/env python3
"""
EINMALIG AUSFÜHREN – speichert alle abgeschlossenen Turniere als Checkpoint.

Die andere Datei (Bot) nimmt dann nur noch zukünftige Turniere.

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
    """Holt ALLE abgeschlossenen Turniere des Teams."""
    resp = requests.get(
        f"{API_BASE}/team/{team_id}/arena",
        params={"status": 30, "nb": 200},
        headers=HEADERS_NDJSON,
        timeout=30,
    )
    resp.raise_for_status()
    tournaments = []
    for line in resp.text.strip().splitlines():
        line = line.strip()
        if line:
            tournaments.append(json.loads(line))
    return tournaments  # neuestes zuerst


def set_checkpoint(key, team_id):
    path = f"ranking_{key}.json"
    print(f"\n--- {key} ({team_id}) ---")

    if not os.path.exists(path):
        print(f"  ⚠️  {path} nicht gefunden – übersprungen.")
        return

    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

    tournaments = fetch_all_finished(team_id)
    if not tournaments:
        print("  ⚠️  Keine abgeschlossenen Turniere gefunden.")
        return

    # Alle abgeschlossenen Turnier-IDs speichern
    processed_ids = [t["id"] for t in tournaments]
    data["processed_tournaments"] = processed_ids
    data["last_processed_tournament"] = processed_ids[0]  # neuestes

    print(f"  ✅ {len(processed_ids)} Turniere als abgeschlossen markiert.")
    print(f"  ✅ Checkpoint → {tournaments[0].get('fullName', processed_ids[0])}")

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

    print("\n✅ Fertig! Der Bot verarbeitet ab jetzt nur noch neue Turniere.")


if __name__ == "__main__":
    main()
