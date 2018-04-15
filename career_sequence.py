# career_sequence.py
# standard career progression

import random
import math
import sys,os
import time
sys.path.append(os.path.realpath('..'))

import career_data


def roll_one_dice():
    return random.randint(1, 6)


def roll_two_dice():
    return roll_one_dice() + roll_one_dice()


def get_enlistment_info(enlistment):
    return "{}+, +1 for {}-{}/+2 for {}-{}".format(enlistment[0], enlistment[1][0][0], enlistment[1][0][1],
                                                   enlistment[1][1][0], enlistment[1][1][1])


def enlist(char, job, enlistment):
    print("Enlistment step - {}+ to join the {}!".format(enlistment[0], job))
    time.sleep(2)
    dm = 0
    # test case for Nobility
    if job == "Nobility":
        return char[5] >= 10
    # check if Rogue
    if job == "Rogues":
        if char[career_data.upp.index(enlistment[1][0][0])] <= enlistment[1][0][1]:
            dm += 1
    else:
        if char[career_data.upp.index(enlistment[1][0][0])] >= enlistment[1][0][1]:
            dm += 1
    if char[career_data.upp.index(enlistment[1][1][0])] >= enlistment[1][1][1]:
        dm += 2
    result = roll_two_dice() + dm
    print("Your result: {}".format(result))
    time.sleep(2)
    return result >= enlistment[0]


def survive(char, job, survival, terms):
    print("Survival step - {}+ to avoid injury!".format(survival[0]))
    time.sleep(2)
    roll = roll_two_dice()
    dm = 0
    if job == "Nobility":
        lived = roll >= survival[0]
    elif job == "Belters":
        dm += terms
        lived = roll + dm >= survival[0]
    else:
        if char[career_data.upp.index(survival[1][0])] >= survival[1][1]:
            dm += 1
        lived = roll + dm >= survival[0]
    print("Your result: {}".format(roll + dm))
    time.sleep(2)
    if lived:
        print("You survived another term in the {}!".format(job))
    else:
        print("You were injured while on active duty.")
    return lived


def promotion(name, char, rank, promo, career):
    result = roll_two_dice()
    print("Promotion step - {}+ to get promoted!".format(promo[0]))
    time.sleep(2)
    if char[career_data.upp.index(promo[1][0])] >= promo[1][1]:
        result += 1
    print("Your result: {}".format(result))
    time.sleep(2)
    if result >= promo[0] and rank < 6:
        rank += 1
        print("You got a promotion! "
              "Congratulations, you are now {} {}.".format(career_data.career_info[career_data.careers.index(career[0])][0][rank], name))
        return True
    else:
        print("Congratulations, you did not get promoted this term.")
        return False


def commission(name, char, rank, comm, career):
    result = roll_two_dice()
    print("Commission step - {}+ to get a commission!".format(comm[0]))
    time.sleep(2)
    if char[career_data.upp.index(comm[1][0])] >= comm[1][1]:
        result += 1
    print("Your result: {}".format(result))
    time.sleep(2)
    if result >= comm[0]:
        print("You received a commission! "
              "Congratulations, you are now {} {}.".format(career_data.career_info[career_data.careers.index(career[0])][0][1], name))
        rank += 1
        return True
    else:
        print("You did not receive a commission. Congratulations!")
        return False


def reenlist(reup):
    print("Re-enlistment step - {}+ to re-enlist!".format(reup))
    time.sleep(2)
    result = roll_two_dice()
    print("Your result: {}".format(result))
    time.sleep(2)
    if result >= reup:
        print("Your re-enlistment request was approved!\n")
        return True
    else:
        print("Your re-enlistment request was denied!")
        print("Mustering you out!")
        return False


def get_position_info(position):
    if position is None:
        return "None"
    else:
        return "{}+, +1 for {}-{}".format(position[0], position[1][0], position[1][1])


def get_starting_skills(starting_skills):
    skills = ""
    if starting_skills is None:
        return skills
    else:
        for key, value in starting_skills.items():
            skills += "\n\t\tRank {}: {}".format(key, value)
        return skills


def print_upp(upp):
    print("\nUPP: Str-{} Dex-{} End-{} Int-{} Edu-{} Soc-{}".
          format(upp[0], upp[1], upp[2], upp[3], upp[4], upp[5]))


def career_steps(name, upp, age, terms, career, rank):
    reup = "Y"
    job = career[0]
    # enlistment = career[1]
    survival = career[2]
    comm = career[3]
    promo = career[4]
    re_up = career[5]
    starting_skills = career[6]
    skills_learned = []

    while reup == "Y":
        print_upp(upp)
        print("Term: {}".format(terms))
        print("Age at start of term: {}".format(age))
        # starting skills, if any step
        if terms == 0:
            get_rank_skills(starting_skills, skills_learned, 0)
        print("Starting skills: {}".format(skills_learned))
        # survival/injury step
        if not survive(upp, job, survival, terms):
            age += 2
            terms += 0.5
            muster_out(name, terms, age, rank, upp, dict((i, skills_learned.count(i)) for i in skills_learned), career)
            break
        else:
            terms += 1
            age += 4
        # commission step
        cm = False
        pm = False
        if rank == 0 and career[3] is not None:
            if commission(name, upp, rank, comm, career):
                cm = True
                rank = 1
                get_rank_skills(starting_skills, skills_learned, 1)
        # promotion step
        if rank > 0 and career[4] is not None:
            if promotion(name, upp, rank, promo, career):
                pm = True
                rank += 1
                get_rank_skills(starting_skills, skills_learned, rank)

        # calculate available skills step
        upp = get_skillz(career, cm, pm, skills_learned, terms, upp)
        print("UPP: ", upp)
        sorted_skills = dict((i, skills_learned.count(i)) for i in skills_learned)
        print_current_skills(sorted_skills)
        upp = aging(terms, upp)
        reup = input("Re-enlist for another term? (Y/N) ")[0].upper()
        if reup == 'Y':
            if reenlist(re_up):
                continue
            else:
                muster_out(name, terms, age, rank, upp, sorted_skills, career)
                break
        else:
            print("Mustering you out!")
            muster_out(name, terms, age, rank, upp, sorted_skills, career)
            return False


def get_skillz(career, cm, pm, skills_learned, terms, upp):
    skills_available = 1
    if career[0] == "Scouts" and terms > 1:
        skills_available += 1

    if terms == 1:
        skills_available += 1
    if cm:
        skills_available += 1
    if pm:
        skills_available += 1
    # learn skills step
    print("Skills step - You have {} skills available this term!".format(skills_available))
    time.sleep(2)
    # print("(R)andom or (C)hoose? ")
    print("Skills learned:")
    # rank skills
    for a in range(skills_available):
        if upp[3] >= 8:
            skill = career_data.career_skills[career_data.careers.index(career[0])][random.randint(0, 3)][
                random.randint(0, 5)]
        else:
            skill = career_data.career_skills[career_data.careers.index(career[0])][random.randint(0, 2)][
                random.randint(0, 5)]
        print(skill)
        time.sleep(1)
        if skill == 'Str' or skill == 'Dex' or skill == 'End' or skill == 'Int' or skill == 'Edu' or skill == 'Soc':
            upp = update_upp(upp, skill, 1)
        else:
            skills_learned.append(skill)
    return upp


def get_rank_skills(starting_skills, skills_learned, rank):
    if starting_skills is None:
        return
    for key, value in starting_skills.items():
        if key == rank:
            print("You learned {}.".format(value))
            skills_learned.append(value)


def print_current_skills(sorted_skills):
    skill_list = 'Current skills: '
    for key, value in sorted_skills.items():
        skill_list += "{}-{}  ".format(key, value)
    print(skill_list)


def convert_upp(upp):
    true_upp = ''
    for stat in upp:
        true_upp += str(convert_to_hex(stat))
    return true_upp


def update_upp(upp, skill, bonus):
    upp[career_data.upp.index(skill)] += bonus
    return upp


def convert_to_hex(value):
    hex_values = ["A", "B", "C", "D", "E", "F"]
    if value >= 15:
        return hex_values[5]
    elif 15 > value >= 10:
        return hex_values[value - 10]
    else:
        return value


def muster_out(name, terms, age, rank, upp, sorted_skills, career):
    benefits = terms + math.ceil(rank / 2)
    muster_benefits = []
    muster_out_benefits = career_data.career_info[career_data.careers.index(career[0])][1]
    muster_out_cash = career_data.career_info[career_data.careers.index(career[0])][2]
    cash = 0
    pension = 0
    print("\nYou exited the {} at rank {} after {} terms of service.".format(career[0], rank, terms))
    print("You are given {} mustering-out benefits.".format(benefits))
    print("Three of these may be cash.")
    rolls = 0
    cash_rolls = 0
    while rolls + cash_rolls < benefits:
        cash, cash_rolls, rolls = get_benefits(cash, cash_rolls, muster_benefits, muster_out_benefits, muster_out_cash,
                                               rank, rolls, sorted_skills, upp)
    if terms >= 5:
        pension = 4000 + ((terms - 5) * 2000)
    sorted_muster = dict((i, muster_benefits.count(i)) for i in muster_benefits)
    print_muster_benefits(sorted_muster)
    print("Cash earned: Cr{}".format(cash))
    print("Annual pension: Cr{}".format(pension))
    print_character(name, terms, age, rank, upp, sorted_skills, sorted_muster, cash, career)


def get_benefits(cash, cash_rolls, muster_benefits, muster_out_benefits, muster_out_cash, rank, rolls, sorted_skills,
                 upp):
    ben = input("(B)enefit or (C)ash? ")[0].upper()
    if ben == 'B':
        roll = roll_one_dice()
        if rank > 4:
            roll += 1
        benefit = muster_out_benefits[roll - 1]
        if benefit[:3] in career_data.upp:
            update_upp(upp, benefit[:3], int(benefit[-1]))
            print("You improved your {} by {}.".format(benefit[:3], benefit[-2:]))
        else:
            muster_benefits.append(benefit)
            print("You earned a {}.".format(benefit))
        rolls += 1
    elif ben == 'C':
        if cash_rolls >= 3:
            print("You have taken the maximum number of Cash rolls. Roll for benefits instead.")
        else:
            roll = roll_one_dice()
            if 'Gambling' in sorted_skills:
                roll += 1
            cash += muster_out_cash[roll - 1]
            cash_rolls += 1
            print("You earned Cr{}".format(muster_out_cash[roll - 1]))
    return cash, cash_rolls, rolls


def print_muster_benefits(sorted_muster):
    muster_list = "Muster-out benefits earned: "
    for key, value in sorted_muster.items():
        muster_list += "{}({})  ".format(key, value)
    print(muster_list)


def print_character(name, terms, age, rank, upp, sorted_skills, sorted_muster, cash, career):
    career_name = career[0]
    if career[0][-1] == 's':
        career_name = career[0][:-1]
    name = input("What is your name, Traveller? : ")
    character_sheet = "\n+-------------------------------------------------+\n"
    character_sheet += "{}, {} {}\n".format(name, career_name, career_data.career_info[career_data.careers.index(career[0])][0][rank])
    character_sheet += "{}  Age {} {} term(s) ".format(convert_upp(upp), age, terms)
    character_sheet += "Cr{}\n".format(cash)
    character_sheet += "Skills: "
    for key, value in sorted_skills.items():
        character_sheet += "{}-{}  ".format(key, value)
    character_sheet += "\nBenefits: "
    for key, value in sorted_muster.items():
        character_sheet += "{}({})  ".format(key, value)
    character_sheet += "\n+-------------------------------------------------+\n"
    print(character_sheet)
    if input("Write character to file? ")[0].upper() == 'Y':
        dir = os.path.dirname(__file__)

        path = "Characters"
        name = name.replace(" ", "_")
        filename = os.path.join(dir, path, name)
        f = open(filename + ".txt", "w")
        f.write(character_sheet)
        print("Character written to {}.txt".format(name))


def aging(terms, upp):
    print("Aging step - {} terms served.".format(terms))
    if terms < 4:
        print("No effects due to aging.")
        print_upp(upp)
        return upp
    print("Checking for aging effects.")
    if 4 <= terms <= 7:
        if roll_two_dice() < 8:
            upp[0] = upp[0]-1
            print("-1 Strength: {}".format(upp[0]))
        else: print("No Strength loss")
        if roll_two_dice() < 7:
            upp[1] = upp[1] -1
            print("-1 Dexterity: {}".format(upp[1]))
        else: print("No Dexterity Loss")
        if roll_two_dice() < 8:
            upp[2] =upp[2]-1
            print("-1 Endurance: {}".format(upp[2]))
        else: print("No Endurance loss")
    if 7 < terms <= 11:
        if roll_two_dice() < 9:
            upp[0] -= 1
            print("-1 Strength: {}".format(upp[0]))
        else: print("No Strength loss")
        if roll_two_dice() < 8:
            upp[1] -= 1
            print("-1 Dexterity: {}".format(upp[1]))
        else: print("No Dexterity Loss")
        if roll_two_dice() < 9:
            upp[2] -= 1
            print("-1 Endurance: {}".format(upp[2]))
        else: print("No Endurance loss")
    if terms >= 12:
        if roll_two_dice() < 9:
            upp[0] -= 2
        else: print("No Strength loss")
        if roll_two_dice() < 9:
            upp[1] -= 2
        else: print("No Dexterity Loss")
        if roll_two_dice() < 9:
            upp[2] -= 2
        else: print("No Dexterity Loss")
        if roll_two_dice() < 9:
            upp[3] -= 1
        else: print("No Intelligence loss")

    print("Your starting UPP:", upp)
    print("Your updated UPP: \nUPP: Str-{} Dex-{} End-{} Int-{} Edu-{} Soc-{}".
          format(upp[0], upp[1], upp[2], upp[3], upp[4], upp[5]))

    return upp
