import json

# Aktuelle Rangliste als Dict: username -> {'points': int, 'booster': float or None}
current_ranking = {
    "DarkOnCrack": {"points": 620, "booster": 2.0},
    "Justinsenpai": {"points": 167, "booster": None},
    "artoftheblade": {"points": 127, "booster": None},
    "Satranc599": {"points": 122, "booster": None},
    "Abd_el_wahab": {"points": 99, "booster": 1.9},
    "POPOIPOIPOI": {"points": 98, "booster": None},
    "Kurse-Aura1": {"points": 95, "booster": None},
    "Konariq7": {"points": 94, "booster": 1.7},
    "VariantsMain": {"points": 92, "booster": None},
    "DRUHA12": {"points": 70, "booster": None},
    "Last_Suspect": {"points": 65, "booster": None},
    "BlotterFan": {"points": 61, "booster": 1.8},
    "Clesio-MorgaM": {"points": 59, "booster": None},
    "Cold_Sewy12": {"points": 48, "booster": 1.5},
    "PushAttack14": {"points": 47, "booster": None},
    "This-Is-Agamveer": {"points": 41, "booster": None},
    "manglee": {"points": 41, "booster": None},
    "Janislav2000": {"points": 32, "booster": None},
    "tunu2011": {"points": 26, "booster": 1.6},
    "VTacademy": {"points": 25, "booster": None},
    "koreshok73": {"points": 23, "booster": None},
    "bbk10s": {"points": 22, "booster": None},
    "kubak5": {"points": 22, "booster": None},
    "LucienTupin": {"points": 21, "booster": None},
    "tharindujayasuriya": {"points": 19, "booster": None},
    "c4energy": {"points": 18, "booster": None},
    "BlitzWarlord": {"points": 18, "booster": None},
    "handyacc": {"points": 18, "booster": None},
    "Mc-ArboledaAxel": {"points": 16, "booster": None},
    "TheRuleBreaker122": {"points": 15, "booster": None},
    "Supperhero_2012": {"points": 13, "booster": None},
    "TacticalCrush_404": {"points": 12, "booster": None},
    "BlackPanda2024": {"points": 12, "booster": None},
    "Chonma": {"points": 12, "booster": 1.4},
    "bulletmaniac": {"points": 6, "booster": None},
    "Devraj-123": {"points": 6, "booster": None},
    "Arjun-Saha6": {"points": 6, "booster": None},
    "EgorGromovYT": {"points": 6, "booster": None},
    "Skysparks": {"points": 6, "booster": None},
    "KillingHeartattack": {"points": 6, "booster": 1.3},
    "dunk-master": {"points": 5, "booster": None},
    "GeekingKing": {"points": 4, "booster": None},
    "A_Khurramov_05": {"points": 4, "booster": None},
    "coldkarmaguy": {"points": 4, "booster": None},
    "Vidishnarra": {"points": 4, "booster": None},
    "ComeToBaba1": {"points": 4, "booster": 1.2},
    "Zerkycharlie": {"points": 3, "booster": None},
    "Ozgur3838": {"points": 3, "booster": None},
    "ZugzwangMode": {"points": 3, "booster": 1.1},
    "Che947": {"points": 3, "booster": None},
    "borak-kopitiam": {"points": 2, "booster": None},
    "blueblue8887": {"points": 2, "booster": None},
    "ciyaerdal4735": {"points": 2, "booster": None},
    "Checkmate_Drifters": {"points": 2, "booster": None},
    "RumijaBarCG21": {"points": 2, "booster": None},
    "Bullet_Thomas": {"points": 2, "booster": None},
    "capt_ateradz": {"points": 2, "booster": None},
    "jash_the_goat": {"points": 1, "booster": None},
}

new_table_json = """
{"rank":1,"score":236,"rating":2513,"username":"DarkOnCrack","flair":"nature.glowing-star","patronColor":5,"performance":2501}
{"rank":2,"score":73,"rating":2236,"username":"AhsapAhsap","flair":"activity.lichess-bullet","performance":2220}
{"rank":3,"score":43,"rating":2181,"username":"tomkruz88","performance":2151}
{"rank":4,"score":38,"rating":1975,"username":"Helokid","flair":"smileys.melting-face","performance":1938}
{"rank":5,"score":32,"rating":2028,"username":"Justinsenpai","performance":1977}
{"rank":6,"score":29,"rating":2228,"username":"just_chess12","performance":2303}
{"rank":7,"score":26,"rating":2104,"username":"BlackPanda2024","flair":"nature.panda","performance":2173}
{"rank":8,"score":16,"rating":1706,"username":"KillingHeartattack","flair":"activity.1st-place-medal","performance":1703}
{"rank":9,"score":13,"rating":2129,"username":"BlitzWarlord","flair":"activity.lichess-blitz","performance":2130}
{"rank":10,"score":8,"rating":2160,"username":"BlotterFan","flair":"symbols.fleur-de-lis","performance":2088}
{"rank":11,"score":8,"rating":1425,"username":"SilentExecution","flair":"objects.crossed-swords","performance":1724}
{"rank":12,"score":6,"rating":2076,"username":"Aura_Farming77","flair":"smileys.cold-face","performance":2113}
{"rank":13,"score":4,"rating":2164,"username":"PhilipX_2023","flair":"smileys.smiling-face-with-horns","performance":2009}
{"rank":14,"score":3,"rating":1856,"username":"sribna","flair":"activity.club-suit","performance":1819}
{"rank":15,"score":2,"rating":2093,"username":"tunu2011","flair":"smileys.astonished-face-blob","performance":2251}
"""

# =========================
# APPLY SCORES (OLD BOOSTERS APPLY ONCE)
# =========================

new_table = []

for line in new_table_json.strip().splitlines():
    line = line.strip()
    if not line:
        continue
    new_table.append(json.loads(line))


for entry in new_table:
    username = entry["username"]
    score = entry["score"]

    if username not in current_ranking:
        current_ranking[username] = {"points": 0, "booster": None}

    booster = current_ranking[username]["booster"]
    if booster:
        score = int(score * booster)

    current_ranking[username]["points"] += score

# =========================
# RESET ALL BOOSTERS
# =========================

for user in current_ranking:
    current_ranking[user]["booster"] = None

# =========================
# ASSIGN NEW BOOSTERS TO TOP 10
# =========================

booster_levels = [2.0, 1.9, 1.8, 1.7, 1.6, 1.5, 1.4, 1.3, 1.2, 1.1]

new_table_sorted = sorted(new_table, key=lambda x: x["score"], reverse=True)

for i in range(min(10, len(new_table_sorted))):
    current_ranking[new_table_sorted[i]["username"]]["booster"] = booster_levels[i]

# =========================
# SORT FINAL RANKING
# =========================

sorted_ranking = sorted(
    current_ranking.items(),
    key=lambda x: x[1]["points"],
    reverse=True
)

# =========================
# OUTPUT
# =========================

for rank, (username, data) in enumerate(sorted_ranking, start=1):
    booster_str = f" ({data['booster']}x boost next arena)" if data["booster"] else ""
    print(f"{rank}. @{username}: {data['points']}{booster_str}")

print("\n# ===== COPY FOR NEXT ARENA =====\n")
print("current_ranking = {")
for username, data in sorted_ranking:
    booster = data["booster"]
    booster_str = booster if booster else "None"
    print(f'    "{username}": {{"points": {data["points"]}, "booster": {booster_str}}},')
print("}")
