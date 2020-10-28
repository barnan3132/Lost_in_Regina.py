import random

from classes import*

player = Player()
battle = False
locked = False

xyz = input("What is your name?\n")
print("After days of wondering the backcountry of Saskatchewan. You rest for a short while. Your eyes darken...")
print("You wake up to a somewhat deserted downtown town")
print("You could visit the town") 
print("or you will stay in the plains to see what else you missed...")
while player.hp > 0:

	if player.hp > player.maxhp:
		player.hp = player.maxhp

print(f'\nWould you like to continue onward, {xyz}? (Y/N)')
ans = input().lower()

if ans == "y":
		encounter = random.randint(1,100)
		if encounter < 10:
			locked = True
			while locked == True:
				print("You found a barrel while out in a canola field! It appears to be locked...Do you want to try and unlock it? (Y/N)")
				chest = input().lower()

				if chest != "y" and chest != "n":
					print("Please enter a valid action")

				elif chest == "y":
					unlock = random.randint(1,100)

					if player.lockpicks == True:
						if unlock <= 80:
							gold = random.randint(2,19)
							player.gold = player.gold + gold
							print(f"You opened the barrel! You found {gold} gold inside of it!\nYou now have {player.gold} gold.")
							locked = False
						elif unlock > 80:
							print("Unfortunately, you were not able to open the barrel")
							locked = False
							continue

					elif unlock > 80:
						gold = random.randint(2,10)
						player.gold = player.gold + gold
						print(f"You opened the barrel! You found {gold} gold inside of it!\nYou now have {player.gold} gold.")
						locked = False

					elif unlock <= 80:
						print("Unfortunately, you were not able to open the barrel")
						locked = False
						continue

				elif chest == "n":
					continue

		elif encounter >= 10:
			battle = True

			while battle == True:
				if player.upg == 0:
					enemy_class = random.choice([Deer, Crow])
				else:
					enemy_class = random.choice([Deer, Crow, Wolf])

				enemy = enemy_class()
				enemy_name = enemy_class.__name__

				print(f"You encounter a {enemy_name}! (A to attack)")

				enemy.hp = enemy.hp + random.choice([-2, -1, 0, 1, 2])

				while enemy.hp > 0 or player.hp > 0:
					print("Press A to attack")
					user = input().lower()

					if user != "a" and user != "y":
						print("Invalid! Please try again!")
						continue

					if user == "a":
						enemy.hp = enemy.hp - player.dmg
						print(f"You dealt {player.dmg} damage to the {enemy_name}!")

					if enemy.hp <= 0:
						print("The enemy has been killed!")
						battle = False

						loot = random.randint(1,100)

						if loot >= 70:
							print("Whats this...? You found a health potion next to the corpse! Some of your wounds have been healed!")
							player.hp = player.hp + 5
							print(f"You now have {player.hp} health.")
						else:
							gold = random.randint(1, 4)
							player.gold = player.gold + gold

							print(f"Whats this..? You found {gold} gold on the corpse!\nYou now have {player.gold} gold!")
						break

					if user == "a":
						enemy.dmg = enemy.dmg + random.choice([0, 1]) - player.ac
						player.hp = player.hp - enemy.dmg

						if enemy.dmg > 0:
							print(f"The {enemy_name} hits back! it deals {enemy.dmg} damage to you!")
						elif enemy.dmg <= 0:
							print(f"The {enemy_name}'s blow was completely deflected by your {player.armor}!")
					if player.hp <= 0:

						print(f"The {enemy_name} knocked you out!\nYou wake up several hours later, and discover that while you were out someone stole your gold...")
						player.gold = 0
						print(f"You now have {player.gold} gold")
						player.hp = 6
						battle = False
                        
elif ans == "n":
        print(f'you have {player.hp}and{player.gold} gold.')
        print(f'You walk into town to see whats open')
        print(f'You see 3 places open:\nbar/CO-Op/Church')

        if village == "tavern":
            print("The Co-Op is busy. The bartender offers you a beer or a medicine for one gold.")
            print(f'Do you accept? (Drink/Medicine')
            print()
        
            inn = input().lower()
        
            if inn == "medicine":
                if player.gold < 2:
                    print("You dont have enough gold!")
                    print(f'You have{player.gold}')
            
                elif player.gold >= 2:
                    cost = 2
                    player.gold = player.gold - cost
                    print("You buy some medicine and it heals you")
                    print(f'You have{player.gold}')
                    player.hp = player.maxhp

            if inn == "drink":
                if player.gold < 1:
                    print("Not enough gold!")
                    print(f'You have{player.gold}')
        
            elif player.gold >= 1:
                cost = 1
                player.gold = player.gold - cost
                print("you drink a few beers with the bartender till the late hour")
                print(f'You have{player.gold}')
                drunken_event = random.randomint(1,100)

                if drunken_event > 10 and drunken_event <= 55:
                    print("You become hazy and tipsy! Be carful next time!")
                    rint("You also lost 5 gold!")
                    print(f'You have{player.gold}')

                elif drunken_event >= 55:
                    good_bet= random.randint(1,5)
                    player.gold = player.gold + good_bet
                    print(f"The night was filled with much beer and many bets!")
                    print(f'You won {good_bet} in bets tonight!')
                    print(f'You have{player.gold}')
            
                elif drinking_event <= 10:
                    print(f'While drunk, you walk outside and a deer confronts you!')
                    enemy_class = Deer()
                    while enemy.hp > 0 or player.hp > 0:
                        print("Press A to attack")
                        user = input().lower()

                        if user != "a" and user != "y":
                            print("Please enter a valid action")
                            continue

                        if user == "a":
                            enemy.hp = enemy.hp - player.dmg
                            print(f"You dealt {player.dmg} damage to the deer!")
                    
                        if enemy.hp <= 0:
                            print("The deer is slain!")
                        
                            loot = random.randint(1,51)
                            if loot >=35:
                                print("You found a bandaid on the deer! Lucky!")
                            else:
                                gold = random.randint(2, 5)
                                player.gold = player.gold + gold
                                print(f"Whats this..? You found {gold} gold on the  corpse!")
                                print(f'You have{player.gold}')
                            break

                        if user == "a":
                            player.hp = player.hp - enemy.dmg
                            print(f"The deer does {enemy.dmg} damage to you!")
                    
                        if player.hp <= 0:
                            print(f"The Deer knocked you out!\nYou wake up several hours later")
                            print("and discover that while you were out someone stole your gold...")
                            player.hp = 5
                            print(f"You now have {player.gold} gold")
                            break

        elif village == "coop":
            print("The Co-Op is busy with activity")
            print("You see on your left a clothing stand ")
            print("On your right you see a weapons stand ")
            print("Directly ahead is a locks and lockpick stand")
            print("Would you like to go to the (Clothing/Weapons/Locks)")
            coop = input().lower()

            if coop == "clothing":
                print("Would you like do buy anything?(Y/N)")
                armor = ["Leather jacket", "Steel plated jacket"]
                leather_price = 8
                steel_price = 25
                if ans == "y":
                    print(f"The smith says he currently has {armor} in stock. Would you care to purchase one?(Y/N)")
                    ans2 = input().lower()

                    if ans2 == "y":
                        print(f"Which armor would you care to buy?")
                        print(f"The {armor[0]} costs {leather_price} and the {armor[1]} costs {steel_price}.\n{armor[0]} or {armor[1]}")
                        
                        ans3 = input().lower()

                        if ans3 =="leather":
                            if player.gold < leather_price:
                                print("You do not have enough gold!")
                            elif player.gold >= leather_price:
                                player.gold = player.gold - leather_price
                                print(f"The cashier sells you the leather jacket")
                                print(f"Your armor level has increased!\nYou now have {player.gold} gold.")
                                player.ac = 1
                                player.armor = "Leather armor"

                        if ans3 =="steel":
                            if player.gold < steel_price:
                                print("You do not have enough gold!")
                                continue
                                
                            elif player.gold >= steel_price:
                                player.gold = player.gold - steel_price
                                print(f"The cashier sells you the leather jacket")
                                print(f"Your armor level has increased!\nYou now have {player.gold} gold.")
                                player.ac = 2
                                player.upg = player.upg + 1
                                player.armor = "Steel Plate armor"

                    elif ans =="n":	
                        print("The Cashier nods and asks you to come back if you change your mind.")
                        continue
                        
                elif ans == "n":
                    print("The cashier nods to leave.")
                    continue

        if coop == "weapons":
            
            if player.upg == 0:
                cost = 10
                print(f"The blacksmith agrees to upgrade your dagger for {cost} gold.")
                print(f"You have {player.gold} gold.")
                print(f" Do you want him to upgrade your dagger? (Y/N)")
                upgrade = input().lower()
                
                if upgrade == "y":
                    if player.gold < cost:
                        print("You do not have enough gold!")
                        continue
                        
                    elif player.gold >= cost:
                        player.gold = player.gold - cost
                        print("The blacksmith upgraded your dagger.")
                        print("You now do more damage per hit!")
                        player.dmg = player.dmg + 2
                        player.upg = player.upg + 1
                    elif upgrade == "n":
                        continue
                        
                    elif player.upg == 1:
                        cost = 25
                        
                        print(f"The blacksmith agrees to upgrade your dagger for {cost} gold.")
                        print(f"You have {player.gold} gold.")
                    print("Do you want him to upgrade your blade? (Y/N)")
                    upgrade = input().lower()
                    if upgrade == "y":
                        if player.gold < cost:
                            print("You do not have enough gold!")
                            continue
                        elif player.gold >= cost:
                            player.gold = player.gold - cost
                            print("The blacksmith upgraded your dagger.")
                            print(" You now do more damage per hit!")
                            player.dmg = player.dmg + 2
                            player.upg = player.upg + 1       
                    elif upgrade == "n":
                        continue
                        
                
                elif player.upg == 2:
                    cost = 50
                    print(f"The blacksmith agrees to upgrade your dagger for {cost} gold.")
                    print(f"You have {player.gold} gold.")
                    print("Do you want him to upgrade your blade? (Y/N)")
                    upgrade = input().lower()
                    if upgrade == "y":
                        if player.gold < cost:
                            print("You do not have enough gold!")
                            continue
                        elif player.gold >= cost:
                            player.gold = player.gold - cost
                            print("The blacksmith upgraded your dagger.")
                            print("You now do more damage per hit!")
                            player.dmg = player.dmg + 2
                            player.upg = player.upg + 1
                            
                    elif upgrade == "n":
                        continue
                        
                elif player.upg >= 3:
                    print(f"The cashier tells you that he cannot upgrade your blade any further.")
                    continue     

        elif coop == "locks":
            print("The locksmith hastly asks you'd like to buy a set (Y/N)")
            locks = input().lower()

            if locks == "y":
                price = 20
                locks2 = ["lockpicks",]
                print(f"The merchant tells you he currently has {locks2} in stock.")
                print(f"They cost {price} gold. Would you like to buy them? (Y/N)")
                
                ans = input().lower()
                
                if ans =="y":
                    if player.gold < price:
                        print("You do not have enough gold!")
                        continue
                        
                    elif player.gold >= price:
                        player.gold = player.gold - price
                        player.lockpicks = True
                        print(f"You bought the {locks2}")
                        print("You now have {player.gold} gold left")
                        
                    elif ans =="n":
                        print("The merchant yells at you for wasting his time")
                        continue
                        
            elif locks =="n":
                print("The merchant yells at you angrily for wasting his time, and demands you leave him be.")
                continue
                
        else:
            print("Please enter a valid action")
            continue


elif village == "church":
        if player.hp < 10:
            print("You have been healed!")
            player.hp = player.hp + 10
            continue
        else:
            print("Enter a valid")
else:
    print("Please try again!")
    continue