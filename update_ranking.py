import json

# Aktuelle Rangliste als Dict: username -> {'points': int, 'booster': float or None}
current_ranking = {
    "DarkOnCrack": {"points": 2419, "booster": None},
    "Chess_Training_2021": {"points": 508, "booster": 1.6},
    "Alex-31": {"points": 424, "booster": None},
    "VariantsMain": {"points": 334, "booster": None},
    "Helokid": {"points": 322, "booster": None},
    "Justinsenpai": {"points": 318, "booster": None},
    "tomkruz88": {"points": 270, "booster": None},
    "Abd_el_wahab": {"points": 231, "booster": None},
    "rj08": {"points": 202, "booster": 1.7},
    "Conrad_Gagnon": {"points": 198, "booster": 1.3},
    "BharatBhushanVerma": {"points": 186, "booster": 1.8},
    "minipekka1": {"points": 158, "booster": None},
    "Esen-Zerk": {"points": 148, "booster": None},
    "mike-bear": {"points": 132, "booster": None},
    "zooz-Zerk": {"points": 128, "booster": None},
    "artoftheblade": {"points": 127, "booster": None},
    "UnHolYDuO": {"points": 124, "booster": 2.0},
    "phone-zerk": {"points": 123, "booster": None},
    "HRVCHESSSTREAM": {"points": 123, "booster": None},
    "Satranc599": {"points": 122, "booster": None},
    "Alcedo": {"points": 121, "booster": None},
    "SchachBasti": {"points": 119, "booster": 1.9},
    "just_chess12": {"points": 105, "booster": None},
    "POPOIPOIPOI": {"points": 100, "booster": None},
    "Konariq7": {"points": 100, "booster": None},
    "Kurse-Aura1": {"points": 95, "booster": None},
    "fin34601473braunpaul": {"points": 89, "booster": None},
    "LucienTupin": {"points": 89, "booster": None},
    "Mahamaha14": {"points": 87, "booster": None},
    "BlotterFan": {"points": 87, "booster": None},
    "AhsapAhsap": {"points": 82, "booster": None},
    "Clesio-MorgaM": {"points": 81, "booster": None},
    "EEAguitarn1": {"points": 79, "booster": None},
    "ElBasmgy": {"points": 77, "booster": None},
    "tunu2011": {"points": 73, "booster": None},
    "FranceWinsWorldCup": {"points": 72, "booster": None},
    "Ahmad_AFG": {"points": 72, "booster": None},
    "DRUHA12": {"points": 70, "booster": None},
    "RodriFK": {"points": 70, "booster": None},
    "GeekingKing": {"points": 68, "booster": None},
    "Last_Suspect": {"points": 65, "booster": None},
    "IZerkYouLose": {"points": 63, "booster": None},
    "Goku_black419": {"points": 62, "booster": None},
    "RumijaBarCG21": {"points": 56, "booster": None},
    "test_acc123": {"points": 54, "booster": None},
    "C8c7C8c7C8c7C8c7C8c7": {"points": 51, "booster": None},
    "Cold_Sewy12": {"points": 48, "booster": None},
    "PushAttack14": {"points": 47, "booster": None},
    "Chonma": {"points": 47, "booster": None},
    "VVIPVIBES": {"points": 45, "booster": None},
    "Ezrg94": {"points": 44, "booster": 1.5},
    "kingboers": {"points": 43, "booster": None},
    "gojosaturo1234567": {"points": 43, "booster": 1.4},
    "This-Is-Agamveer": {"points": 41, "booster": None},
    "manglee": {"points": 41, "booster": None},
    "BlackPanda2024": {"points": 38, "booster": None},
    "Retasea_400": {"points": 38, "booster": None},
    "Gyusudhdh_zerk": {"points": 38, "booster": None},
    "CANCINARTUCEL": {"points": 36, "booster": None},
    "timothyemmanuel": {"points": 35, "booster": None},
    "Agam2013": {"points": 35, "booster": None},
    "doruk2606": {"points": 33, "booster": None},
    "Janislav2000": {"points": 32, "booster": None},
    "BlitzWarlord": {"points": 31, "booster": None},
    "asswolve": {"points": 30, "booster": None},
    "KillingHeartattack": {"points": 30, "booster": None},
    "WalterFire": {"points": 28, "booster": None},
    "Skysparks": {"points": 26, "booster": 1.1},
    "rohanvv07082010": {"points": 26, "booster": 1.2},
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
    "healLan": {"points": 11, "booster": None},
    "Ajuju": {"points": 11, "booster": None},
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
    "Carlotaurus": {"points": 8, "booster": None},
    "Egorchess01": {"points": 8, "booster": None},
    "Mayangnabila": {"points": 7, "booster": None},
    "bulletmaniac": {"points": 6, "booster": None},
    "Devraj-123": {"points": 6, "booster": None},
    "EgorGromovYT": {"points": 6, "booster": None},
    "Aura_Farming77": {"points": 6, "booster": None},
    "Mathew2014": {"points": 6, "booster": None},
    "manu2013ss": {"points": 6, "booster": None},
    "xavier_77": {"points": 6, "booster": None},
    "CHesslayer2301": {"points": 6, "booster": None},
    "Elwan03": {"points": 6, "booster": None},
    "dunk-master": {"points": 5, "booster": None},
    "Bagii_Bagii": {"points": 5, "booster": None},
    "A_Khurramov_05": {"points": 4, "booster": None},
    "coldkarmaguy": {"points": 4, "booster": None},
    "PhilipX_2023": {"points": 4, "booster": None},
    "S_E_C_R_E_T": {"points": 4, "booster": None},
    "Enserman123": {"points": 4, "booster": None},
    "AVYUKT_GARG": {"points": 4, "booster": None},
    "Zerkycharlie": {"points": 3, "booster": None},
    "ZugzwangMode": {"points": 3, "booster": None},
    "sribna": {"points": 3, "booster": None},
    "learningchess6": {"points": 3, "booster": None},
    "DIMAStup": {"points": 3, "booster": None},
    "okoh11122233": {"points": 3, "booster": None},
    "Gyusudh": {"points": 3, "booster": None},
    "AJESHHRAO12": {"points": 3, "booster": None},
    "Grabytx12": {"points": 3, "booster": None},
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
    "SENTHILGANESAN": {"points": 2, "booster": None},
    "sirmull": {"points": 2, "booster": None},
    "Jerronbabylansu": {"points": 2, "booster": None},
    "jash_the_goat": {"points": 1, "booster": None},
}

new_table_json = """
{"rank":1,"score":102,"rating":2512,"username":"UnHolYDuO","performance":2367}
{"rank":2,"score":96,"rating":2334,"username":"VVIPVIBES","performance":2402}
{"rank":3,"score":78,"rating":2406,"username":"hmmmhmmmhmmm","performance":2301}
{"rank":4,"score":45,"rating":2054,"username":"Jerronbabylansu","performance":2063}
{"rank":5,"score":41,"rating":2140,"username":"abhigyan_a_b","flair":"symbols.mending-heart","performance":2100}
{"rank":6,"score":34,"rating":1993,"username":"RumijaBarCG21","flair":"people.flexed-biceps","performance":2011}
{"rank":7,"score":33,"rating":2379,"username":"minipekka1","performance":2361}
{"rank":8,"score":24,"rating":1734,"username":"Alcedo","flair":"symbols.small-blue-diamond","patronColor":1,"performance":1851}
{"rank":9,"score":16,"rating":1780,"username":"Conrad_Gagnon","performance":1878}
{"rank":10,"score":14,"rating":2214,"username":"rj08","performance":2281}
{"rank":11,"score":13,"rating":2080,"username":"ElBasmgy","performance":2027}
{"rank":12,"score":12,"rating":2199,"username":"tomkruz88","performance":2012}
{"rank":13,"score":8,"rating":2502,"username":"SandaruDamsara","flair":"smileys.skull","performance":2229}
{"rank":14,"score":8,"rating":2017,"username":"Arjun-Saha6","flair":"smileys.angry-face-with-horns","performance":2065}
{"rank":15,"score":4,"rating":2234,"username":"Chairopian","flair":"people.zombie","performance":2526}
{"rank":16,"score":4,"rating":1427,"username":"schwarzerrabe","performance":1603}
{"rank":17,"score":3,"rating":2795,"username":"ThinkingKnight9","performance":2206}
{"rank":18,"score":2,"rating":2133,"username":"KING_OF_KILLER","flair":"smileys.angry-face-with-horns","performance":2172}
{"rank":19,"score":2,"rating":2137,"username":"HugeSmoggyFirebird","flair":"smileys.smiling-face-with-horns-blob","performance":2110}
{"rank":20,"score":2,"rating":1641,"username":"Thabang-Nate","performance":1615}
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
