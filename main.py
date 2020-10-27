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
							gold = random.randint(2,10)
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
						break