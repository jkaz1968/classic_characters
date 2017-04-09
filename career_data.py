# career_data.py - rank, mustering-out benefits and cash benefits for each career

# career_skills.py
# module containing the skill lists for all career options

# upp list
upp = ["Str", "Dex", "End", "Int", "Edu", "Soc"]

# career_list includes all careers added to the char gen system so far. Stats in parens are bonus stats (+1/+2).
careers = ["Navy", "Marines", "Army", "Scouts", "Merchants",
           "Pirates", "Belters", "Sailors", "Diplomats", "Doctors", "Flyers",
           "Barbarians", "Bureaucrats", "Rogues", "Nobility", "Scientists", "Hunters"]

# career_rolls covers all relevant values needed to achieve each stage of career
# [career, enlistment, [survival, bonus upp#], [position, bonus upp#], [promo, bonus upp#], reenlist, [service skills]]
career_list = [
    # Book 1 careers
    ["Navy", (8, [["Int", 8], ["Edu", 9]]), (5, ["Int", 7]), (10, ["Soc", 9]), (8, ["Edu", 8]), 6,
     {0: "", 5: "Soc", 6: "Soc"}],
    ["Marines", (9, [["Int", 8], ["Str", 8]]), (6, ["End", 8]), (9, ["Edu", 7]), (9, ["Soc", 8]), 6,
     {0: "Cutlass", 1: "Revolver"}],
    ["Army", (5, [["Dex", 6], ["End", 5]]), (5, ["Edu", 6]), (5, ["End", 7]), (6, ["Edu", 7]), 7,
     {0: "Rifle", 1: "SMG"}],
    ["Scouts", (7, [["Int", 6], ["Str", 8]]), (7, ["End", 7]), None, None, 3, {0: "Pilot"}],
    ["Merchants", (7, [["Str", 7], ["Int", 6]]), (5, ["Int", 7]), (4, ["Int", 6]), (10, ["Int", 9]), 4, {4: "Pilot"}],
    # Supplement 4 careers p. 6
    ["Pirates", (7, [["Soc", 7], ["End", 9]]), (6, ["Int", 6]), (9, ["Str", 10]), (8, ["Int", 9]), 7,
     {0: "Brawling", 1: "Pilot"}],
    ["Belters", (8, [["Dex", 9], ["Int", 6]]), (9, ["Terms", ""]), None, None, 7, {0: "Vacc Suit"}],
    ["Sailors", (6, [["End", 10], ["Str", 8]]), (5, ["End", 8]), (5, ["Int", 9]), (6, ["Edu", 8]), 6, None],
    ["Diplomats", (8, [["Edu", 8], ["Soc", 9]]), (3, ["Edu", 9]), (5, ["Int 8"]), (10, ["Soc", 10]), 5, {0: "Liaison"}],
    ["Doctors", (9, [["Int", 8], ["Dex", 9]]), (3, ["Int", 8]), None, None, 4, {0: "Medical"}],
    ["Flyers", (6, [["Str", 7], ["Dex", 9]]), (5, ["Dex", 8]), (5, ["Edu", 6]), (8, ["Edu", 8]), 6, {0: "Air Craft"}],
    # Supplement 4 careers p.,8
    ["Barbarians", (5, [["End", 9], ["Str", 10]]), (6, ["Str", 8]), (6, ["Str", 10]), (9, ["Int", 6]), 6,
     {0: "Sword", 2: "Blade Cbt", 5: "Leader"}],
    ["Bureaucrats", (5, [["Edu", 9], ["Str", 8]]), (4, ["Edu", 10]), (6, ["Soc", 9]), (7, ["Int", 9]), 3, None],
    ["Rogues", (6, [["Soc", 8], ["End", 7]]), (6, ["Int", 9]), None, None, 5, {0: "Streetwise"}],
    ["Nobility", (0, [["Soc", 10], [None, None]]), (3, [None, None]), (5, ["Edu", 9]), (12, ["Int", 10]), 4, None],
    ["Scientists", (6, [["Int", 9], ["Edu", 10]]), (5, ["Edu", 9]), None, None, 5, {0: "Computer"}],
    ["Hunters", (9, [["Dex", 10], ["End", 9]]), (6, ["Str", 10]), None, None, 5, {0: "Hunting"}]
]

career_skills = [
    # Book 1 careers
    # 0 navy
    [
        ["Str", "Dex", "End", "Int", "Edu", "Soc"],  # pdt
        ["Ship's Boat", "Vacc Suit", "Fwd Obs", "Gunnery", "Blade Cbt", "Gun Cbt"],  # sst
        ["Vacc Suit", "Mechanical", "Electronic", "Engineering", "Gunnery", "Jack-o-T"],  # aed
        ["Medical", "Navigation", "Engineering", "Computer", "Pilot", "Admin"]
    ],  # ed8+

    # 1 marines
    [
        ["Str", "Dex", "End", "Gambling", "Brawling", "Blade Cbt"],  # pdt
        ["ATV", "Vacc Suit", "Blade Cbt", "Gun Cbt", "Blade Cbt", "Gun Cbt"],  # sst
        ["Vehicle", "Mechanical", "Electronic", "Tactics", "Blade Cbt", "Gun Cbt"],  # aed
        ["Medical", "Tactics", "Tactics", "Computer", "Leader", "Admin"]
    ],  # ed8+

    # 2 army
    [
        ["Str", "Dex", "End", "Gambling", "Brawling", "Blade Cbt"],  # pdt
        ["ATV", "Vacc Suit", "Blade Cbt", "Gun Cbt", "Blade Cbt", "Gun Cbt"],  # sst
        ["Vehicle", "Mechanical", "Electronic", "Tactics", "Blade Cbt", "Gun Cbt"],  # aed
        ["Medical", "Tactics", "Tactics", "Computer", "Leader", "Admin"]
    ],  # ed8+

    # 3 scout
    [
        ["Str", "Dex", "End", "Int", "Edu", "Gun Cbt"],  # pdt
        ["Air/Raft", "Vacc Suit", "Mechanical", "Navigation", "Electronics", "Jack-o-T"],  # sst
        ["Vehicle", "Mechanical", "Electronic", "Jack-o-T", "Gunnery", "Medical"],  # aed
        ["Medical", "Navigation", "Engineering", "Computer", "Pilot", "Jack-o-T"]
    ],  # ed8+

    # 4 merchant
    [
        ["Str", "Dex", "End", "Str", "Blade Cbt", "Bribery"],  # pdt
        ["Vehicle", "Vacc Suit", "Jack-o-T", "Steward", "Electronics", "Gun Cbt"],  # sst
        ["Streetwise", "Mechanical", "Electronic", "Navigation", "Gunnery", "Medical"],  # aed
        ["Medical", "Navigation", "Engineering", "Computer", "Pilot", "Admin"]
    ],  # ed8+

    # Supplement 4 Careers
    # 5 pirate
    [
        ["Str", "Dex", "End", "Gambling", "Brawling", "Blade Cbt"],  # pdt
        ["Blade Cbt", "Vacc Suit", "Gun Cbt", "Gunnery", "Zero-G Cbt", "Gun Cbt"],  # sst
        ["Streetwise", "Gunnery", "Engineering", "Ship Tactics", "Tactics", "Mechanical"],  # aed
        ["Navigation", "Pilot", "Forgery", "Computer", "Leader", "Electronic"]
    ],  # ed8+

    # 6 belter
    [
        ["Str", "Dex", "End", "Gambling", "Brawling", "Vacc Suit"],  # pdt
        ["Vacc Suit", "Vacc Suit", "Prospecting", "Fwd Obs", "Prospecting", "Ship's Boat"],  # sst
        ["Ship's Boat", "Electronic", "Prospecting", "Mechanical", "Prospecting", "Instruction"],  # aed
        ["Medical", "Navigation", "Engineering", "Computer", "Pilot", "Jack-o-T"]
    ],  # ed8+

    # 7 sailor
    [
        ["Str", "Dex", "End", "Gambling", "Brawling", "Carousing"],  # pdt
        ["Gun Cbt", "Comms", "Fwd Obs", "Vehicle", "Vehicle", "Battle Dress"],  # sst
        ["Water Craft", "Electronic", "Mechanical", "Gravitics", "Navigation", "Demolition"],  # aed
        ["Medical", "Vehicle", "Streetwise", "Computer", "Admin", "Jack-o-T"]
    ],  # ed8+

    # 8 diplomat
    [
        ["Str", "Edu", "Int", "Blade Cbt", "Gun Cbt", "Carousing"],  # pdt
        ["Int", "Vacc Suit", "Vehicle", "Vehicle", "Gambling", "Computer"],  # sst
        ["Forgery", "Streetwise", "Interrogation", "Recruiting", "Instruction", "Admin"],  # aed
        ["Liaison", "Liaison", "Admin", "Computer", "Soc", "Jack-o-T"]
    ],  # ed8+

    # 9 doctor
    [
        ["Str", "Dex", "End", "Int", "Edu", "Soc"],  # pdt
        ["Dex", "Electronic", "Medical", "Streetwise", "Medical", "Blade Cbt"],  # sst
        ["Medical", "Medical", "Mechanical", "Electronic", "Computer", "Admin"],  # aed
        ["Medical", "Medical", "Admin", "Computer", "Int", "Edu"]
    ],  # ed8+

    # 10 flyer
    [
        ["Str", "Dex", "End", "Gambling", "Brawling", "Carousing"],  # pdt
        ["Brawling", "Vacc Suit", "Gun Cbt", "Vehicle", "Vehicle", "Vehicle"],  # sst
        ["Aircraft", "Mechanical", "Electronic", "Gravitics", "Gun Cbt", "Survival"],  # aed
        ["Medical", "Leader", "Pilot", "Computer", "Jack-o-T", "Admin"]
    ],  # ed8+

    # 11 barbarian
    [
        ["Str", "Str", "Str", "Carousing", "Dex", "End"],  # pdt
        ["Brawling", "Blade Cbt", "Blade Cbt", "Bow Cbt", "Bow Cbt", "Gun Cbt"],  # sst
        ["Blade Cbt", "Mechanical", "Survival", "Recon", "Streetwise", "Bow Cbt"],  # aed
        ["Medical", "Interrogation", "Tactics", "Leader", "Instruction", "Jack-o-T"]
    ],  # ed8+

    # 12 bureaucrat
    [
        ["End", "Edu", "Int", "Brawling", "Carousing", "Dex"],  # pdt
        ["Gun Cbt", "Vehicle", "Instruction", "Vehicle", "Blade Cbt", "Edu"],  # sst
        ["Recruiting", "Vehicle", "Liaison", "Interrogation", "Admin", "Admin"],  # aed
        ["Admin", "Admin", "Computer", "Admin", "Jack-o-T", "Leader"]
    ],  # ed8+

    # 13 rogue
    [
        ["Str", "Dex", "End", "Int", "Brawling", "Carousing"],  # pdt
        ["Blade Cbt", "Gun Cbt", "Demolition", "Vehicle", "Edu", "Vehicle"],  # sst
        ["Streetwise", "Forgery", "Bribery", "Carousing", "Liaison", "Ship's Boat"],  # aed
        ["Medical", "Bribery", "Forgery", "Computer", "Leader", "Jack-o-T"]
    ],  # ed8+

    # 14 noble
    [
        ["Str", "Dex", "End", "Int", "Carousing", "Brawling"],  # pdt
        ["Gun Cbt", "Blade Cbt", "Hunting", "Vehicle", "Bribery", "Dex"],  # sst
        ["Pilot", "Ship's Boat", "Vehicle", "Navigation", "Engineering", "Leader"],  # aed
        ["Medical", "Computer", "Admin", "Liaison", "Leader", "Jack-o-T"]
    ],  # ed8+

    # 15 scientist
    [
        ["Str", "Dex", "End", "Int", "Edu", "Carousing"],  # pdt
        ["Instruction", "Blade Cbt", "Vehicle", "Jack-o-T", "Navigation", "Survival"],  # sst
        ["Mechanical", "Electronic", "Gravitics", "Computer", "Int", "Edu"],  # aed
        ["Life Sciences", "Computer", "Chemistry", "Leader", "Int", "Physics"]
    ],  # ed8+

    # 16 hunter
    [
        ["Str", "Dex", "End", "Int", "Blade Cbt", "Gun Cbt"],  # pdt
        ["Blade Cbt", "Gun Cbt", "Survival", "Hunting", "Vehicle", "Hunting"],  # sst
        ["Gravitics", "Mechanical", "Electronic", "Computer", "Hunting", "Admin"],  # aed
        ["Medical", "Computer", "Hunting", "Leader", "Survival", "Admin"]
    ],  # ed8+
]

career_info = [
    # Book 1 careers
    # 0 navy
    [
        ["", "Ensign", "Lieutenant", "Lt Commander", "Commander", "Captain", "Admiral"],
        ["Low Psg", "Int +1", "Edu +2", "Blade", "TAS Membership", "High Psg", "Soc +2"],
        [1000, 5000, 5000, 10000, 20000, 50000, 50000],
        "The Navy handles both in-system defense and interstellar actions."
    ],

    # 1 marines
    [
        ["", "Lieutenant", "Captain", "Major", "Lt Colonel", "Colonel", "Brigadier"],
        ["Low Psg", "Int +2", "Edu +1", "Blade", "TAS Membership", "High Psg", "Soc +2"],
        [2000, 5000, 5000, 10000, 20000, 30000, 40000],
        "The Marines are the ground combat division of the space Navy."
    ],

    # 2 army
    [
        ["", "Lieutenant", "Captain", "Major", "Lt Colonel", "Colonel", "General"],
        ["Low Psg", "Int +1", "Edu +2", "Gun", "High Psg", "Mid Psg", "Soc +1"],
        [2000, 5000, 10000, 10000, 10000, 20000, 30000],
        "The Army is responsible for maintaining long-term planetside security."
    ],

    # 3 scouts
    [
        ["", "", "", "", "", "", ""],
        ["Low Psg", "Int +2", "Edu +2", "Blade", "Gun", "Scout Ship"],
        [20000, 20000, 30000, 30000, 50000, 50000, 50000],
        "The Scout Service seeks out new worlds and civilizations."
    ],

    # 4 merchants
    [
        ["", "4th Officer", "3rd Officer", "2nd Officer", "1st Officer", "Captain", "Captain"],
        ["Low Psg", "Int +1", "Edu +1", "Gun", "Blade", "Low Psg", "Free Trader"],
        [1000, 5000, 10000, 20000, 20000, 40000, 40000],
        "Merchants fly the trade routes between worlds."
    ],

    # Supplement 4 characters
    # 5 pirates
    [
        ["", "Henchman", "Lieutenant", "Mate", "Commander", "Captain", "Commodore"],
        ["Low Psg", "Int +1", "Weapon", "Letter of Marque", "Soc -1", "Mid Psg", "Corsair"],
        [0, 0, 1000, 10000, 50000, 50000, 50000],
        "Pirates are raiders and privateers who harass legitimate merchants on trade routes."
    ],

    # 6 belters
    [
        ["", "", "", "", "", "", ""],
        ["Low Psg", "Int +1", "Weapon", "High Psg", "TAS Membership", "Seeker"],
        [0, 0, 1000, 10000, 100000, 100000, 100000],
        "Belters are miners and prospectors who live and work in asteroid belts."
    ],

    # 7 sailors
    [
        ["", "Ensign", "Lieutenant", "Lt Commander", "Commander", "Captain", "Admiral"],
        ["Low Psg", "Edu +1", "Weapon", "Weapon", "High Psg", "High Psg", "Soc +1"],
        [2000, 5000, 10000, 10000, 10000, 20000, 30000],
        "Sailors are the 'wet navy' of planetside military forces."
    ],

    # 8 diplomats
    [
        ["3rd Secretary", "2nd Secretary", "1st Secretary", "Counselor", "Minister", "Ambassador"],
        ["Low Psg", "Int +1", "Edu +2", "Weapon", "Soc +1", "High Psg", "TAS Membership'"],
        [10000, 10000, 10000, 20000, 50000, 60000, 70000],
        "Diplomats are responsible for international and interplanetary negotiations."
    ],

    # 9 doctors
    [
        ["", "", "", "", "", "", ""],
        ["Low Psg", "Edu +1", "Edu +1", "Weapon", "Instruments", "Mid Psg", ""],
        [20000, 20000, 20000, 30000, 40000, 60000, 100000],
        "Doctors are medical professionals including physicians and surgeons."
    ],

    # 10 flyers
    [
        ["", "Flying Officer", "Flight Lt", "Squadron Leader", "Wing Commander", "Group Captain", "Air Marshal"],
        ["Low Psg", "Edu +1", "Weapon", "Weapon", "High Psg", "Mid Psg", "Soc +1"],
        [2000, 5000, 10000, 10000, 10000, 20000, 30000],
        "Flyers are the air forces of planetside military."
    ],

    # 11 barbarians
    [
        ["", "Warrior", "Warrior", "Warrior", "Warrior", "Chief", "Chief"],
        ["Low Psg", "Blade", "Blade", "Blade", "'", "High Psg", "High Psg"],
        [0, 0, 1000, 2000, 3000, 4000, 5000],
        "Barbarians are typically from tribes and pre-technological societies."
    ],

    # 12 bureaucrats
    [
        ["", "Clerk", "Supervisor", "Assistant Manager", "Manager", "Executive", "Director"],
        ["Low Psg", "Mid Psg", "", "Watch", "", "High Psg", "Soc +1"],
        [0, 0, 10000, 10000, 40000, 40000, 80000],
        "Bureaucrats keep the government functioning as the civil service."
    ],

    # 13 rogues
    [
        ["", "", "", "", "", "", ""],
        ["Low Psg", "Soc +1", "Gun", "Blade", "High Psg", "TAS Membership"],
        [0, 0, 10000, 10000, 50000, 100000, 100000],
        "Rogues are basically thieves and scoundrels, the criminal underbelly of the future."
    ],

    # 14 nobles
    [
        ["", "Knight", "Baron(ess)", "Marquis/Marquesa", "Count(ess)", "Duke/Duchess", "Duke/Duchess"],
        ["High Psg", "High Psg", "Gun", "Blade", "TAS Membership", "Yacht", ""],
        [10000, 50000, 50000, 100000, 100000, 100000, 200000],
        "The nobility is the upper crust of society."
    ],

    # 15 scientists
    [
        ["", "", "", "", "", "", ""],
        ["Low Psg", "Mid Psg", "High Psg", "+1 Soc", "Gun", "Lab Ship", ""],
        [1000, 2000, 5000, 10000, 20000, 30000, 40000],
        "Scientists do research and exploration."
    ],

    # 16 hunters
    [
        ["", "", "", "", "", "", ""],
        ["Low Psg", "Mid Psg", "High Psg", "Weapon", "Weapon", "Safari Ship"],
        [1000, 1000, 5000, 5000, 10000, 100000, 100000],
        "Hunters are professionals usually paid to track and capture (or kill) exotic beasts."
    ]

]
