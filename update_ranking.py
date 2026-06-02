import json

# Aktuelle Rangliste als Dict: username -> {'points': int, 'booster': float or None}
current_ranking = {
    "DarkOnCrack": {"points": 2415, "booster": 2.0},
    "Chess_Training_2021": {"points": 456, "booster": None},
    "Alex-31": {"points": 424, "booster": None},
    "VariantsMain": {"points": 334, "booster": None},
    "Helokid": {"points": 322, "booster": None},
    "Justinsenpai": {"points": 318, "booster": None},
    "tomkruz88": {"points": 254, "booster": 1.7},
    "Abd_el_wahab": {"points": 231, "booster": None},
    "Esen-Zerk": {"points": 148, "booster": None},
    "mike-bear": {"points": 132, "booster": None},
    "zooz-Zerk": {"points": 128, "booster": 1.9},
    "artoftheblade": {"points": 127, "booster": None},
    "Satranc599": {"points": 122, "booster": None},
    "Conrad_Gagnon": {"points": 118, "booster": 1.3},
    "Alcedo": {"points": 117, "booster": None},
    "phone-zerk": {"points": 114, "booster": None},
    "just_chess12": {"points": 105, "booster": None},
    "POPOIPOIPOI": {"points": 100, "booster": None},
    "Konariq7": {"points": 100, "booster": None},
    "Kurse-Aura1": {"points": 95, "booster": None},
    "fin34601473braunpaul": {"points": 89, "booster": None},
    "Mahamaha14": {"points": 87, "booster": None},
    "BlotterFan": {"points": 87, "booster": None},
    "minipekka1": {"points": 85, "booster": None},
    "LucienTupin": {"points": 85, "booster": None},
    "AhsapAhsap": {"points": 82, "booster": None},
    "Clesio-MorgaM": {"points": 81, "booster": None},
    "ElBasmgy": {"points": 77, "booster": None},
    "EEAguitarn1": {"points": 76, "booster": 1.5},
    "HRVCHESSSTREAM": {"points": 75, "booster": 1.8},
    "tunu2011": {"points": 73, "booster": None},
    "FranceWinsWorldCup": {"points": 72, "booster": None},
    "Ahmad_AFG": {"points": 72, "booster": None},
    "DRUHA12": {"points": 70, "booster": None},
    "RodriFK": {"points": 70, "booster": None},
    "GeekingKing": {"points": 68, "booster": 1.4},
    "Last_Suspect": {"points": 65, "booster": None},
    "IZerkYouLose": {"points": 63, "booster": None},
    "Goku_black419": {"points": 62, "booster": None},
    "C8c7C8c7C8c7C8c7C8c7": {"points": 51, "booster": 1.6},
    "Cold_Sewy12": {"points": 48, "booster": None},
    "RumijaBarCG21": {"points": 48, "booster": None},
    "PushAttack14": {"points": 47, "booster": None},
    "Chonma": {"points": 47, "booster": None},
    "VVIPVIBES": {"points": 45, "booster": None},
    "kingboers": {"points": 43, "booster": 1.2},
    "This-Is-Agamveer": {"points": 41, "booster": None},
    "manglee": {"points": 41, "booster": None},
    "BlackPanda2024": {"points": 38, "booster": None},
    "Retasea_400": {"points": 38, "booster": None},
    "CANCINARTUCEL": {"points": 36, "booster": None},
    "timothyemmanuel": {"points": 35, "booster": None},
    "Agam2013": {"points": 35, "booster": None},
    "Gyusudhdh_zerk": {"points": 35, "booster": 1.1},
    "Janislav2000": {"points": 32, "booster": None},
    "BlitzWarlord": {"points": 31, "booster": None},
    "asswolve": {"points": 30, "booster": None},
    "rj08": {"points": 29, "booster": None},
    "doruk2606": {"points": 28, "booster": None},
    "KillingHeartattack": {"points": 28, "booster": None},
    "WalterFire": {"points": 28, "booster": None},
    "VTacademy": {"points": 25, "booster": None},
    "schwarzerrabe": {"points": 24, "booster": None},
    "koreshok73": {"points": 23, "booster": None},
    "JohnnyChess": {"points": 23, "booster": None},
    "bbk10s": {"points": 22, "booster": None},
    "kubak5": {"points": 22, "booster": None},
    "Che947": {"points": 22, "booster": None},
    "Ficheal": {"points": 21, "booster": None},
    "Arjun-Saha6": {"points": 20, "booster": None},
    "tharindujayasuriya": {"points": 19, "booster": None},
    "Asherdarin": {"points": 19, "booster": None},
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
    "HiHelloHey": {"points": 14, "booster": None},
    "Supperhero_2012": {"points": 13, "booster": None},
    "Lightning_of_chess": {"points": 13, "booster": None},
    "TacticalCrush_404": {"points": 12, "booster": None},
    "Blue-green-world": {"points": 12, "booster": None},
    "ComeToBaba1": {"points": 10, "booster": None},
    "BRUNO90_7p": {"points": 10, "booster": None},
    "pompitarelojerita": {"points": 10, "booster": None},
    "KaanKa18": {"points": 10, "booster": None},
    "vwz": {"points": 9, "booster": None},
    "vasudev9": {"points": 9, "booster": None},
    "SilentExecution": {"points": 8, "booster": None},
    "Vidishnarra": {"points": 8, "booster": None},
    "Livoncik": {"points": 8, "booster": None},
    "Ochesage": {"points": 8, "booster": None},
    "UrasAras4444": {"points": 8, "booster": None},
    "Mayangnabila": {"points": 7, "booster": None},
    "bulletmaniac": {"points": 6, "booster": None},
    "Devraj-123": {"points": 6, "booster": None},
    "EgorGromovYT": {"points": 6, "booster": None},
    "Skysparks": {"points": 6, "booster": None},
    "Aura_Farming77": {"points": 6, "booster": None},
    "test_acc123": {"points": 6, "booster": None},
    "Mathew2014": {"points": 6, "booster": None},
    "manu2013ss": {"points": 6, "booster": None},
    "xavier_77": {"points": 6, "booster": None},
    "dunk-master": {"points": 5, "booster": None},
    "Carlotaurus": {"points": 5, "booster": None},
    "A_Khurramov_05": {"points": 4, "booster": None},
    "coldkarmaguy": {"points": 4, "booster": None},
    "PhilipX_2023": {"points": 4, "booster": None},
    "S_E_C_R_E_T": {"points": 4, "booster": None},
    "Enserman123": {"points": 4, "booster": None},
    "Zerkycharlie": {"points": 3, "booster": None},
    "ZugzwangMode": {"points": 3, "booster": None},
    "sribna": {"points": 3, "booster": None},
    "learningchess6": {"points": 3, "booster": None},
    "DIMAStup": {"points": 3, "booster": None},
    "okoh11122233": {"points": 3, "booster": None},
    "Gyusudh": {"points": 3, "booster": None},
    "borak-kopitiam": {"points": 2, "booster": None},
    "blueblue8887": {"points": 2, "booster": None},
    "ciyaerdal4735": {"points": 2, "booster": None},
    "Checkmate_Drifters": {"points": 2, "booster": None},
    "Bullet_Thomas": {"points": 2, "booster": None},
    "capt_ateradz": {"points": 2, "booster": None},
    "VenusaurBeedrill": {"points": 2, "booster": None},
    "FatDummy": {"points": 2, "booster": None},
    "Retroceso": {"points": 2, "booster": None},
    "RookNRollMaster": {"points": 2, "booster": None},
    "Caleb_IL": {"points": 2, "booster": None},
    "DrGrekenstein12": {"points": 2, "booster": None},
    "Budding_champ": {"points": 2, "booster": None},
    "FRGUnrated": {"points": 2, "booster": None},
    "german11": {"points": 2, "booster": None},
    "jash_the_goat": {"points": 1, "booster": None},
}

new_table_json = """
{"rank":1,"score":73,"rating":2309,"username":"minipekka1","performance":2170}
{"rank":2,"score":63,"rating":2268,"username":"rj08","performance":2156}
{"rank":3,"score":48,"rating":2168,"username":"test_acc123","flair":"smileys.sleeping-face-blob","performance":2315}
{"rank":4,"score":28,"rating":2590,"username":"BharatBhushanVerma","flair":"symbols.broken-heart","performance":2489}
{"rank":5,"score":28,"rating":1838,"username":"Conrad_Gagnon","performance":1840}
{"rank":6,"score":27,"rating":2092,"username":"HRVCHESSSTREAM","performance":2039}
{"rank":7,"score":11,"rating":1808,"username":"healLan","patronColor":7,"performance":1977}
{"rank":8,"score":9,"rating":2364,"username":"phone-zerk","flair":"smileys.anxious-face-with-sweat","performance":2129}
{"rank":9,"score":8,"rating":1931,"username":"RumijaBarCG21","flair":"people.flexed-biceps","performance":1954}
{"rank":10,"score":6,"rating":1708,"username":"CHesslayer2301","flair":"nature.fire","performance":1970}
{"rank":11,"score":6,"rating":1801,"username":"Elwan03","performance":1730}
{"rank":12,"score":5,"rating":1809,"username":"doruk2606","flair":"activity.lichess-bullet","performance":1817}
{"rank":13,"score":3,"rating":1831,"username":"Carlotaurus","flair":"symbols.fleur-de-lis","performance":2145}
{"rank":14,"score":3,"rating":2067,"username":"AJESHHRAO12","performance":2061}
{"rank":15,"score":2,"rating":1713,"username":"SENTHILGANESAN","flair":"smileys.skull-and-crossbones","performance":2317}
{"rank":16,"score":2,"rating":2558,"username":"DarkOnCrack","flair":"nature.glowing-star","patronColor":6,"performance":2209}
{"rank":17,"score":2,"rating":2000,"username":"EEAguitarn1","flair":"activity.lichess-rapid","performance":2030}
{"rank":18,"score":2,"rating":2134,"username":"sirmull","performance":1820}
{"rank":19,"score":2,"rating":1679,"username":"KillingHeartattack","flair":"activity.1st-place-medal","performance":1607}
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
