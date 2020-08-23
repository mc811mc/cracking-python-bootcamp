from time import sleep

gender = str(input("""What is your gender? Enter "m" for male and "f" for female. """))
name = str(input("What is your name? "))
gender = gender.lower()
timeframe = int(input("What year is it in your world? ")) 

if gender == "m":
    partner_name = str(input("What is the name of your Queen? "))
    kingdom = str(input("What is the name of your Kingdom? "))
    ally = str(input("""Do you have allies? Enter "y" for yes and "n" for no. """))
    enemy = str(input("""Do you have enemies? Enter "y" for yes and "n" for no."""))
    paladin = str(input("What is the name of your Paladin? "))
    wizard = str(input("What is the name of your Wizard? "))
    warrior = str(input("What is the name of your Warrior? "))
    if enemy == "y":
        print(name, "has enemies, got a lot of enemies")
    villian = str(input("What is the name of your Villian? "))
    war = str(input("What is the name of the War? "))
    year = int(input("How many years did the war last? "))
    thief = str(input("What is the name of your thief? "))
    sorcerer = str(input("What is the name of your sorceror? "))
    rogue = str(input("What is the name of your rogue? "))
    article = "his"
    partner = "queen"
    leader_title = "King"
    partner_title = "Queen"
elif gender == "f":
    partner_name = str(input("What is the name of your King? "))
    kingdom = str(input("What is the name of your Kingdom? "))
    ally = str(input("""Do you have allies? Enter "y" for yes and "n" for no. """))
    enemy = str(input("""Do you have enemies? Enter "y" for yes and "n" for no."""))
    paladin = str(input("What is the name of your Paladin? "))
    wizard = str(input("What is the name of your Wizard? "))
    warrior = str(input("What is the name of your Warrior? "))
    if enemy == "y":
        print(name, "has enemies, got a lot of enemies")
    villian = str(input("What is the name of your Villian? "))
    war = str(input("What is the name of the War? "))
    year = int(input("How many years did the war last? "))
    thief = str(input("What is the name of your thief? "))
    sorcerer = str(input("What is the name of your sorceror? "))
    rogue = str(input("What is the name of your rogue? "))
    article = "her"
    partner = "king"
    leader_title = "Queen"
    partner_title = "King"

story = f"""

Zzz...

Welcome, {name}. You are about to enter the world where the Kingdom of {kingdom} has been at peace for as long as history can remember.

Alongside you, you have your {partner} {partner_name} to help you through thick and thin. 

Let us enter the Kingdom of {kingdom}.

In {timeframe}, {leader_title} {name} and {partner_title} {partner_name} ruled the Kingdom of {kingdom}.

However, in a far far distant land, there lived their nemesis Villian {villian} always looking for the oportunity to seize the Kingdom of {kingdom}.

On a Sunday morning, {villian} and his army led by {thief}, {sorcerer}, and {rogue} 
pillaged their land, stole precious resources, and brutally attacked their villagers.
       
Filled with rage, {leader_title} {name} and {partner_title} {partner_name} with the help of {paladin}, {wizard}, and {warrior} valiantly fought back 
and defeated {villian} after {year} years of fierce fighting.

Order was finally restored with {villian} taken to jail deep in their kingdom.

"""

print(story)