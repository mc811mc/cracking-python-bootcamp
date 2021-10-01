import string

gender = str(input("""What is your gender? Enter "m" for male and "f" for female. """))
name = str(input("What is your name? "))
name = string.capwords(name)
gender = gender.lower()
timeframe = int(input("What year is it in your world? ")) 

if gender == "m":
    partner_name = str(input("What is the name of your Queen? "))
    partner_name = string.capwords(partner_name)
    kingdom = str(input("What is the name of your Kingdom? "))
    kingdom = string.capwords(kingdom)
    ally = str(input("""Do you have allies? Enter "y" for yes and "n" for no. """))
    ally = ally.lower()
    if ally == "y":
        paladin = str(input("What is the name of your Paladin? "))
        paladin = string.capwords(paladin)
        wizard = str(input("What is the name of your Wizard? "))
        wizard = string.capwords(wizard)
        warrior = str(input("What is the name of your Warrior? "))
        warrior = string.capwords(warrior)
    elif ally == "n":
        pass
    enemy = str(input("""Do you have enemies? Enter "y" for yes and "n" for no."""))
    enemy = enemy.lower()
    if enemy == "y":
        print(name, "has enemies, more enemies than", name, "can imagine!")
        thief = str(input("What is the name of your thief? "))
        thief = string.capwords(thief)
        sorcerer = str(input("What is the name of your sorceror? "))
        sorcerer = string.capwords(sorcerer)
        rogue = str(input("What is the name of your rogue? "))
        rogue = string.capwords(rogue)
    elif enemy =="n":
        pass
    villian = str(input("What is the name of your Villian? "))
    villian = string.capwords(villian)
    war = str(input("What is the name of the War? "))
    war = string.capwords(war)
    year = int(input("How many years did the war last? "))
    article = "his"
    partner = "queen"
    leader_title = "King"
    partner_title = "Queen"
elif gender == "f":
    partner_name = str(input("What is the name of your King? "))
    partner_name = string.capwords(partner_name)
    kingdom = str(input("What is the name of your Kingdom? "))
    kingdom = string.capwords(kingdom)
    ally = str(input("""Do you have allies? Enter "y" for yes and "n" for no. """))
    ally = ally.lower()
    if ally == "y":
        paladin = str(input("What is the name of your Paladin? "))
        paladin = string.capwords(paladin)
        wizard = str(input("What is the name of your Wizard? "))
        wizard = string.capwords(wizard)
        warrior = str(input("What is the name of your Warrior? "))
        warrior = string.capwords(warrior)
    elif ally == "n":
        pass
    enemy = str(input("""Do you have enemies? Enter "y" for yes and "n" for no."""))
    enemy = enemy.lower()
    if enemy == "y":
        print(name, "has enemies", name, "has too many enemies to fight off!")
        thief = str(input("What is the name of your thief? "))
        thief = string.capwords(thief)
        sorcerer = str(input("What is the name of your sorceror? "))
        sorcerer = string.capwords(sorcerer)
        rogue = str(input("What is the name of your rogue? "))
        rogue = string.capwords(rogue)
    elif enemy =="n":
        pass
    villian = str(input("What is the name of your Villian? "))
    villian = string.capwords(villian)
    war = str(input("What is the name of the War? "))
    war = string.capwords(war)
    year = int(input("How many years did the war last? "))
    article = "her"
    partner = "king"
    leader_title = "Queen"
    partner_title = "King"
else:
    print("Please try again by entering either m or f.")
    exit()

#Multiple Story Lines Depending on Condition

if ally == "y" and enemy == "y":
    yes_yes_story = f"""

    Zzz...

    Welcome, {name}. You are about to enter the world where the Kingdom of {kingdom} has been at peace for as long as history can remember.

    Alongside you, you have your {partner} {partner_name} to help you through thick and thin. 

    Let us enter the Kingdom of {kingdom}.

    In {timeframe}, {leader_title} {name} and {partner_title} {partner_name} ruled the Kingdom of {kingdom}.

    However, in a far far distant land, there lived their nemesis Villian {villian} always looking for the oportunity to seize the Kingdom of {kingdom}.

    On a Sunday morning, Villian {villian} and his army led by Thief {thief}, Sorcerer {sorcerer}, and Rogue {rogue} 
    pillaged their land, stole precious resources, and brutally attacked their villagers.
        
    Filled with rage, {leader_title} {name} and {partner_title} {partner_name} with the help of Paladin {paladin}, Wizard {wizard}, and Warrior {warrior} valiantly fought back 
    and defeated Villian {villian} after {year} years of fierce fighting.

    Order was finally restored with Villian {villian} taken to jail deep in their kingdom.

    """
    print(yes_yes_story)

elif ally == "y" and enemy == "n":
    yes_no_story = f"""

    Zzz...

    Welcome, {name}. You are about to enter the world where the Kingdom of {kingdom} has been at peace for as long as history can remember.

    Alongside you, you have your {partner} {partner_name} to help you through thick and thin. 

    Let us enter the Kingdom of {kingdom}.

    In {timeframe}, {leader_title} {name} and {partner_title} {partner_name} ruled the Kingdom of {kingdom}.

    However, in a far far distant land, there lived their nemesis Villian {villian} always looking for the oportunity to seize the Kingdom of {kingdom}.

    Despite Villian {villian}'s ambitions, the Kingdom of {kingdom} has always been under the proctection of the three mighty heroes
    known as Paladin {paladin}, Wizard {wizard}, and Warrior {warrior}. The trio held back Villian {villian} to even take attempts on conquering their kingdom.

    The Kingdom of {kingdom} was never in peril and everyone lived a happy life. 

    """
    print(yes_no_story)

elif ally == "n" and enemy == "y":
    no_yes_story = f"""

    Zzz...

    Welcome, {name}. You are about to enter the world where the Kingdom of {kingdom} has been at peace for as long as history can remember.

    Alongside you, you have your {partner} {partner_name} to help you through thick and thin. 

    Let us enter the Kingdom of {kingdom}.

    In {timeframe}, {leader_title} {name} and {partner_title} {partner_name} ruled the Kingdom of {kingdom}.

    However, in a far far distant land, there lived their nemesis Villian {villian} always looking for the oportunity to seize the Kingdom of {kingdom}.

    On a Sunday morning, {villian} and his army led by {thief}, {sorcerer}, and {rogue} 
    pillaged their land, stole precious resources, and brutally attacked their villagers.
        
    Filled with rage, {leader_title} {name} and {partner_title} {partner_name} tried to get as much as they could from nearby kingdoms.

    However, without forces on their own, they reluctantly gave in to evil {villian} at the end of the day.

    The history of the Kingdom would now change forever. From Kingdom {kingdom}, {villian} switched the name to Kingdom of {villian}. 

    The rest has not been yet told to the world. 

    """

    print(no_yes_story)
    
elif ally == "n" and enemy == "n":
    no_no_story = f"""
    
    Zzz...

    Welcome, {name}. You are about to enter the world where the Kingdom of {kingdom} has been at peace for as long as history can remember.

    Alongside you, you have your {partner} {partner_name} to help you through thick and thin. 

    Let us enter the Kingdom of {kingdom}.

    In {timeframe}, {leader_title} {name} and {partner_title} {partner_name} ruled the Kingdom of {kingdom}.

    However, in a far far distant land, there lived their nemesis Villian {villian} always looking for the oportunity to seize the Kingdom of {kingdom}.

    Despite {villian}'s ambitions, he did not have any forces to conquer the Kingdom of {kingdom}. 

    News spread across the kingdom that {villian} was up to no good. 

    Quickly, {leader_title} {name} gathered his followers and commanded to make a team that would deter {villian} to ever look over the kingdom
    for the future days of {kingdom}.

    Pressure was building up on both sides, each agitating one another for something the world wished not to experience. 

    To be continued...

    """
    
    print(no_no_story)