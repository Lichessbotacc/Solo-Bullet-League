import json

# Aktuelle Rangliste als Dict: username -> {'points': int, 'booster': float or None}
current_ranking = {
    "DarkOnCrack": {"points": 1996, "booster": 1.9},
    "Alex-31": {"points": 424, "booster": None},
    "VariantsMain": {"points": 334, "booster": None},
    "Justinsenpai": {"points": 318, "booster": None},
    "Helokid": {"points": 232, "booster": 1.7},
    "Abd_el_wahab": {"points": 231, "booster": 1.4},
    "Chess_Training_2021": {"points": 198, "booster": 2.0},
    "tomkruz88": {"points": 196, "booster": None},
    "Esen-Zerk": {"points": 148, "booster": 1.8},
    "artoftheblade": {"points": 127, "booster": None},
    "Satranc599": {"points": 122, "booster": None},
    "phone-zerk": {"points": 114, "booster": None},
    "POPOIPOIPOI": {"points": 100, "booster": None},
    "Konariq7": {"points": 100, "booster": None},
    "Kurse-Aura1": {"points": 95, "booster": None},
    "Mahamaha14": {"points": 87, "booster": None},
    "Clesio-MorgaM": {"points": 81, "booster": None},
    "BlotterFan": {"points": 75, "booster": None},
    "Alcedo": {"points": 75, "booster": 1.5},
    "AhsapAhsap": {"points": 73, "booster": None},
    "FranceWinsWorldCup": {"points": 72, "booster": None},
    "Conrad_Gagnon": {"points": 72, "booster": 1.1},
    "Ahmad_AFG": {"points": 72, "booster": 1.6},
    "DRUHA12": {"points": 70, "booster": None},
    "Last_Suspect": {"points": 65, "booster": None},
    "just_chess12": {"points": 64, "booster": None},
    "IZerkYouLose": {"points": 63, "booster": None},
    "LucienTupin": {"points": 58, "booster": None},
    "fin34601473braunpaul": {"points": 55, "booster": 1.2},
    "Goku_black419": {"points": 55, "booster": 1.3},
    "ElBasmgy": {"points": 50, "booster": None},
    "Cold_Sewy12": {"points": 48, "booster": None},
    "tunu2011": {"points": 48, "booster": None},
    "PushAttack14": {"points": 47, "booster": None},
    "Chonma": {"points": 47, "booster": None},
    "mike-bear": {"points": 47, "booster": None},
    "VVIPVIBES": {"points": 45, "booster": None},
    "This-Is-Agamveer": {"points": 41, "booster": None},
    "manglee": {"points": 41, "booster": None},
    "BlackPanda2024": {"points": 38, "booster": None},
    "Retasea_400": {"points": 38, "booster": None},
    "RodriFK": {"points": 33, "booster": None},
    "Janislav2000": {"points": 32, "booster": None},
    "BlitzWarlord": {"points": 31, "booster": None},
    "Agam2013": {"points": 29, "booster": None},
    "doruk2606": {"points": 28, "booster": None},
    "KillingHeartattack": {"points": 28, "booster": None},
    "EEAguitarn1": {"points": 27, "booster": None},
    "VTacademy": {"points": 25, "booster": None},
    "koreshok73": {"points": 23, "booster": None},
    "bbk10s": {"points": 22, "booster": None},
    "kubak5": {"points": 22, "booster": None},
    "Che947": {"points": 22, "booster": None},
    "GeekingKing": {"points": 22, "booster": None},
    "Ficheal": {"points": 21, "booster": None},
    "tharindujayasuriya": {"points": 19, "booster": None},
    "c4energy": {"points": 18, "booster": None},
    "handyacc": {"points": 18, "booster": None},
    "Tipchess": {"points": 17, "booster": None},
    "Ozgur3838": {"points": 17, "booster": None},
    "Mc-ArboledaAxel": {"points": 16, "booster": None},
    "Best_Chess_Player15": {"points": 16, "booster": None},
    "TheRuleBreaker122": {"points": 15, "booster": None},
    "Try_Different_Bro28": {"points": 15, "booster": None},
    "RWDHDK67": {"points": 14, "booster": None},
    "Andyisagoodboy": {"points": 14, "booster": None},
    "Supperhero_2012": {"points": 13, "booster": None},
    "TacticalCrush_404": {"points": 12, "booster": None},
    "ComeToBaba1": {"points": 10, "booster": None},
    "BRUNO90_7p": {"points": 10, "booster": None},
    "vwz": {"points": 9, "booster": None},
    "Arjun-Saha6": {"points": 9, "booster": None},
    "vasudev9": {"points": 9, "booster": None},
    "SilentExecution": {"points": 8, "booster": None},
    "Vidishnarra": {"points": 8, "booster": None},
    "Livoncik": {"points": 8, "booster": None},
    "bulletmaniac": {"points": 6, "booster": None},
    "Devraj-123": {"points": 6, "booster": None},
    "EgorGromovYT": {"points": 6, "booster": None},
    "Skysparks": {"points": 6, "booster": None},
    "Aura_Farming77": {"points": 6, "booster": None},
    "test_acc123": {"points": 6, "booster": None},
    "dunk-master": {"points": 5, "booster": None},
    "A_Khurramov_05": {"points": 4, "booster": None},
    "coldkarmaguy": {"points": 4, "booster": None},
    "PhilipX_2023": {"points": 4, "booster": None},
    "schwarzerrabe": {"points": 4, "booster": None},
    "Ochesage": {"points": 4, "booster": None},
    "UrasAras4444": {"points": 4, "booster": None},
    "Zerkycharlie": {"points": 3, "booster": None},
    "ZugzwangMode": {"points": 3, "booster": None},
    "sribna": {"points": 3, "booster": None},
    "learningchess6": {"points": 3, "booster": None},
    "DIMAStup": {"points": 3, "booster": None},
    "borak-kopitiam": {"points": 2, "booster": None},
    "blueblue8887": {"points": 2, "booster": None},
    "ciyaerdal4735": {"points": 2, "booster": None},
    "Checkmate_Drifters": {"points": 2, "booster": None},
    "RumijaBarCG21": {"points": 2, "booster": None},
    "Bullet_Thomas": {"points": 2, "booster": None},
    "capt_ateradz": {"points": 2, "booster": None},
    "Asherdarin": {"points": 2, "booster": None},
    "VenusaurBeedrill": {"points": 2, "booster": None},
    "FatDummy": {"points": 2, "booster": None},
    "Retroceso": {"points": 2, "booster": None},
    "RookNRollMaster": {"points": 2, "booster": None},
    "Caleb_IL": {"points": 2, "booster": None},
    "jash_the_goat": {"points": 1, "booster": None},
}

new_table_json = """
{"rank":1,"score":129,"rating":2618,"username":"Chess_Training_2021","flair":"objects.crown","performance":2435}
{"rank":2,"score":85,"rating":2395,"username":"minipekka1","performance":2401}
{"rank":3,"score":85,"rating":2485,"username":"mike-bear","flair":"objects.teddy-bear","patronColor":3,"performance":2238}
{"rank":4,"score":53,"rating":2097,"username":"Helokid","flair":"smileys.melting-face","performance":2066}
{"rank":5,"score":51,"rating":2434,"username":"DarkOnCrack","flair":"nature.glowing-star","patronColor":6,"performance":2192}
{"rank":6,"score":46,"rating":1963,"username":"RumijaBarCG21","flair":"people.flexed-biceps","performance":2097}
{"rank":7,"score":41,"rating":2219,"username":"just_chess12","performance":2154}
{"rank":8,"score":37,"rating":2660,"username":"RodriFK","flair":"nature.black-cat","performance":2439}
{"rank":9,"score":35,"rating":1582,"username":"timothyemmanuel","performance":1719}
{"rank":10,"score":30,"rating":1614,"username":"asswolve","performance":1889}
{"rank":11,"score":29,"rating":2270,"username":"rj08","performance":1873}
{"rank":12,"score":28,"rating":1670,"username":"Alcedo","flair":"symbols.small-blue-diamond","patronColor":1,"performance":1966}
{"rank":13,"score":28,"rating":1988,"username":"WalterFire","performance":1742}
{"rank":14,"score":27,"rating":2053,"username":"ElBasmgy","performance":1836}
{"rank":15,"score":26,"rating":2013,"username":"CANCINARTUCEL","performance":1956}
{"rank":16,"score":20,"rating":1423,"username":"schwarzerrabe","performance":1478}
{"rank":17,"score":17,"rating":1589,"username":"Asherdarin","flair":"smileys.astonished-face-blob","performance":1656}
{"rank":18,"score":14,"rating":1583,"username":"HiHelloHey","performance":1848}
{"rank":19,"score":12,"rating":2116,"username":"tunu2011","flair":"nature.bison","performance":1937}
{"rank":20,"score":10,"rating":2694,"username":"pompitarelojerita","performance":1824}
{"rank":21,"score":5,"rating":2300,"username":"Mayangnabila","patronColor":1,"performance":2154}
{"rank":22,"score":5,"rating":1803,"username":"Carlotaurus","flair":"symbols.fleur-de-lis","performance":2023}
{"rank":23,"score":4,"rating":2147,"username":"Ochesage","performance":1822}
{"rank":24,"score":3,"rating":1370,"username":"okoh11122233","flair":"smileys.winking-face-with-tongue","performance":1558}
{"rank":25,"score":2,"rating":1730,"username":"DrGrekenstein12","flair":"activity.lichess-berserk","performance":1519}
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
