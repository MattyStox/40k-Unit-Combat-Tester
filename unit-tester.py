import random
from colorama import init, Fore, Back, Style

# this is the main file for "unit tester", providing the 
# ability to enter in unit atttributes for attacker and defender
# and see the anticipated results based on random dice roles

class Attacker():
    def __init__(self, name, attacks, damage, strength, ws, ap):
        self.name: ""
        self.attacks = 0
        self.damage = 0
        self.strength = 0
        self.ws = 0
        self.ap = -0
        self.models = 0

class Defender():
    def __init__(self, name, toughness, save, wound):
        self.name: ""
        self.toughness = 0
        self.save = 0
        self.wound = 0
        self.models = 0

def main():

    print()
    print("*********************************")
    print()
    print("Unit Comparison Simulator (UCS)")
    print()
    print("*********************************")
    print()

    print("NOTE:  Currently hand to hand combat only")
    print()

    #Basic details
    print(Fore.YELLOW + "Let's get some basic unit information")
    print(Style.RESET_ALL)
    Attacker.name = input("What is the name of your unit? : ")
    Attacker.models = int(input("How many MODELS are fighting in the unit? : "))
    print()

    #Attributes - attackers
    print(Fore.YELLOW + "Let's get some information about the {}'s unit" .format(Attacker.name))
    print(Style.RESET_ALL)
    Attacker.strength = int(input("What is the STRENGTH charateristic of the Attackers in this unit? : "))
    Attacker.ws = int(input("What is the WEAPON SKILL charateristic of the Attackers in this unit? : "))
    Attacker.attacks = int(input("What is the ATTACK charateristic of the Attackers in this unit? : "))
    Attacker.damage = int(input("What is the DAMAGE rating of the weapon used in this unit? : "))
    Attacker.ap = int(input("What AP modifiers do the weapons in this unit have? : "))
    print()
    unitComp = int(input(Fore.RED + "Does your unit composition give you additional attacks?  If yes, how many per model - if no, enter 0 : "))
    print(Style.RESET_ALL)
    print()

    print(Fore.YELLOW + "Let's get some information about the defending unit")
    print(Style.RESET_ALL)
    #Attribues - defenders
    Defender.name = input("What is the name of your unit? : ")
    Defender.models = int(input("How many MODELS are there in this unit have? : "))
    Defender.toughness = int(input("What is the TOUGHNESS charateristic of the Defenders in their unit? : "))
    Defender.wound = int(input("How many WOUNDS do each model in this unit have? : "))
    Defender.save = int(input("What is the SAVE charateristic of the Attacker.models in their unit? : "))
    print()

    numDice = (Attacker.models * Attacker.attacks) + (Attacker.models * unitComp)
    totalAttacks = Attacker.attacks + unitComp

    print("Here's the information you provided.")
    print()
    print(Fore.GREEN +"{}" .format(Attacker.name))
    print(Style.RESET_ALL)
    print("Model in the Unit = {}" .format(Attacker.models))
    print("Weapon skill = {}" .format(Attacker.ws))
    print("Total Attacks = {}" .format(totalAttacks))
    print("Strength = {}" .format(Attacker.strength))
    print("Weapon damage = {}" .format(Attacker.damage))
    print("Weapon AP = {}" .format(Attacker.ap))
    print()
    print(Fore.RED +"{}" .format(Defender.name))
    print(Style.RESET_ALL)
    print("Model in the Unit = {}" .format(Defender.models))
    print("Toughness = {}" .format(Defender.toughness))
    print("Wounds per model = {} " .format(Defender.wound))
    print("Save per model = {}" .format(Defender.save))
    print()

    start = input("Press ENTER if ready to attack")

    #need = 0

    print()
    print(Fore.YELLOW + "You have {} models in this unit and get {} attacks each.  You're rolling {} dice hitting on {}+..." .format(Attacker.models, totalAttacks, numDice, Attacker.ws))
    print(Style.RESET_ALL)

    need = Attacker.ws

    #INITIAL HIT

    result = [random.randint(1, 6) for x in range(0, numDice)]
    print(result, numDice)
    print()

    count = sorted(i for i in result if i >= need)
    total_wins = len(count)

    print(Fore.GREEN + "You hit {} times" .format(total_wins, need))
    print(Style.RESET_ALL)

    #WOUNDING

    if Attacker.strength > Defender.toughness:
        Attacker.wound = 3
    elif Attacker.strength < Defender.toughness:
        Attacker.wound = 5
    else:
        Attacker.wound = 4
    
    #Need to add in conditions for double S over T and vice versa

    need = Attacker.wound

    print(Fore.YELLOW + "{}(s) scored {} hits and roll to wound on {}+ (Strength {} vs Toughness {})..." .format(Attacker.name, total_wins, Attacker.wound, Attacker.strength, Defender.toughness))
    print(Style.RESET_ALL)

    result = [random.randint(1, 6) for x in range(0, total_wins)]
    print(result, total_wins)
    print()

    count = sorted(i for i in result if i >= need)
    total_wins = len(count)

    damage = total_wins * Attacker.damage

    print(Fore.GREEN + "You wound {} times causing {} damage." .format(total_wins, damage))
    print(Style.RESET_ALL)

    #SAVES

    need = Defender.save - Attacker.ap

    if need > 6:
        print(Fore.YELLOW + "{} roll to save {} incoming wounds totalling {} damage, and are unable to make a saving throw ({}+)..." .format(Defender.name, total_wins, damage, need))
        print(Style.RESET_ALL)
    else:
        print(Fore.YELLOW + "{} roll to save {} incoming wounds totalling {} damage, needing rolls of {}+..." .format(Defender.name, total_wins, damage, need))
        print(Style.RESET_ALL)

    

    result = [random.randint(1, 6) for x in range(0, total_wins)]
    print(result, total_wins)
    print()

    count = sorted(i for i in result if i >= need)
    saved = len(count)
    count = sorted(i for i in result if i < need)
    survive = len(count)

   # if Defender.wound >=2 :
        #final_damage = (survive * Attacker.damage) /2
   # else:
        #final_damage = survive * Attacker.damage

    final_damage = survive * Attacker.damage

    print(Fore.GREEN + "{} save {} incoming wounds and take the remaining {} wound(s) totalling {} damage" .format(Defender.name, saved, survive, final_damage))
    print(Style.RESET_ALL)

    alive = final_damage / Defender.wound

    if alive > Defender.models:
        alive = ("ALL")

    print(Fore.RED + "{} {} have fallen in battle (Unit was {} models with {} wound(s) each)" .format(alive, Defender.name, Defender.models, Defender.wound))
    print(Style.RESET_ALL)

main()

while True:
    answer = input("Run again? (y/n): ")
    if answer not in ('y', 'n'):
        print("Invalid input.")
        break
    if answer == 'y':
        main()
    else:
        print("Goodbye")
        break
