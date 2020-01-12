import pygame
import random
from timeit import default_timer as timer
pygame.init()

print("")

#DISPLAY RESOLUTION
displayWidth = 800
displayHeight = 600

#SETTING DISPLAY AND CAPTION
gameDisplay = pygame.display.set_mode((displayWidth,displayHeight))
pygame.display.set_caption("Tamagotchi")
clock = pygame.time.Clock()

#COLOUR VARIABLES
white = (255,255,255)

#IMAGE VARIABLES
hashitamatchi = pygame.image.load("hash.png")
kuribotchi = pygame.image.load("kuri.png")
mukimukitchi = pygame.image.load("muki.png")
tamatchi = pygame.image.load("tama.png")
yasaguretchi = pygame.image.load("yasa.png")
duck = pygame.image.load("duck.png")
play = pygame.image.load("play.png")
feed = pygame.image.load("feed.png")
save = pygame.image.load("save.png")
medicine = pygame.image.load("medicine.png")
heart = pygame.image.load("heart.png")
shit = pygame.image.load("shit.png")

#IMAGE DISPLAY FUNCTION
def imageDisplay(x,y,image):
	gameDisplay.blit(image,(x,y))

#TAMAGOTCHI CLASS
class Tamagotchi:
	#INITIAL
	def __init__(self,species,nickname):
		self.species = species
		self.nickname = nickname
		self.fullness = 2
		self.happiness = 2
		self.age = 0
		self.healthiness = 3
		
	#FEEDING METHOD
	def eat(self):
		self.fullness += 1
	
	#ADDING HAPPINESS METHOD
	def smile(self):
		self.happiness += 1
	
	#INCREASING HEALTHINESS METHOD
	def ayyy(self):
		self.healthiness += 1
	
	#DECREASING HEALTHINESS METHOD
	def ouf(self):
		self.healthiness -= 1

#SAVING DATA FUNCTION
def saveData(species,nickname,fullness,happiness,age,healthiness,displayShit,timeSpent,shitTime,specX,specY):
	#WRITING DATA FOR ALL VARIABLES TO data.txt
	with open("data.txt","w") as f:
		#SPECIES
		f.write(species + "\n")
		#NICKNAME
		if nickname:
			f.write(nickname + "\n")
		else:
			f.write("None" + "\n")
		#FULLNESS VALUE
		f.write(str(fullness) + "\n")
		#HAPPINESS VALUE
		f.write(str(happiness) + "\n")
		#AGE VALUE
		f.write(str(age) + "\n")
		#HEALTHINESS VALUE
		f.write(str(healthiness) + "\n")
		#displayShit VARIABLE VALUE
		if displayShit:
			f.write("1" + "\n")
		else:
			f.write("0" + "\n")
		#timeSpent VARIABLE VALUE
		f.write(str(timeSpent) + "\n")
		#shitTime VARIABLE VALUE
		f.write(str(shitTime) + "\n")
		#specX VARIABLE VALUE
		f.write(str(specX) + "\n")
		#specY VARIABLE VALUE
		f.write(str(specY))

#LOADING DATA FUNCTION
def loadData():
	with open("data.txt","r") as f:
		data = f.readlines()
		#SPECIES
		data[0] = data[0][:-1]
		#NICKNAME
		data[1] = data[1][:-1]
		#FULLNESS
		data[2] = int(data[2][:-1])
		#HAPPINESS
		data[3] = int(data[3][:-1])
		#AGE
		data[4] = int(data[4][:-1])
		#HEALTHINESS
		data[5] = int(data[5][:-1])
		#DISPLAYSHIT
		data[6] = bool(int(data[6][:-1]))
		#TIMESPENT
		data[7] = int(data[7][:-1])
		#SHITTIME
		data[8] = float(data[8][:-1])
		#SPECX
		data[9] = float(data[9][:-1])
		#SPECY
		data[10] = float(data[10][:-1])
		#RETURN WHOLE LIST OF DATA
		return data

#INITIALIZING savedData VARIABLE
#IF data.txt EXISTS
try:
	with open("data.txt") as f:
		savedData = loadData()
#IF data.txt DOES NOT EXIST
except:
	savedData = []

#GAME LOOP FUNCTION
def gameLoop(existingData):

	#IF data.txt HAS NO SAVED DATA
	if not existingData:

		#BEGINNING OF START-GAME
		startExit = False

		#[START-GAME LOOP]
		while not startExit:

			#X-POSITIONS OF ALL TAMAGOTCHI IN THE START
			hashX = displayWidth*0.03
			kuriX = displayWidth*0.23
			mukiX = displayWidth*0.42
			tamaX = displayWidth*0.60
			yasaX = displayWidth*0.80

			#Y-POSITONS OF ALL TAMAGOTCHI IN THE START
			hashY = displayHeight*0.4
			kuriY = displayHeight*0.45
			mukiY = displayHeight*0.46
			tamaY = displayHeight*0.45
			yasaY = displayHeight*0.35

			#{EVENT LOOP}
			for event in pygame.event.get():
				#WHEN MOUSE IS CLICKED:
				if event.type == pygame.MOUSEBUTTONDOWN:
					mx,my = pygame.mouse.get_pos()
					if my > 207 and my < 404:
						if mx > 20 and mx < 164:
							tamagotchi = hashitamatchi
						elif mx > 182 and mx < 324:
							tamagotchi = kuribotchi
						elif mx > 333 and mx < 474:
							tamagotchi = mukimukitchi
						elif mx > 479 and mx < 620:
							tamagotchi = tamatchi
						elif mx > 634 and mx < 782:
							tamagotchi = yasaguretchi
						#START-GAME LOOP WILL NOW EXIT
						startExit = True
			#END OF EVENT LOOP
						
			#FILL BACKGROUND WHITE
			gameDisplay.fill(white)

			#DISPLAY ALL TAMAGOTCHI
			imageDisplay(hashX,hashY,hashitamatchi)
			imageDisplay(kuriX,kuriY,kuribotchi)
			imageDisplay(mukiX,mukiY,mukimukitchi)
			imageDisplay(tamaX,tamaY,tamatchi)
			imageDisplay(yasaX,yasaY,yasaguretchi)
				
			pygame.display.update()
		#END OF START-GAME LOOP
			
		#INITIALIZING species AS CHOSEN TAMAGOTCHI
		if tamagotchi == hashitamatchi:
			specY = hashY
			species = "HASHITAMATCHI"
		elif tamagotchi == kuribotchi:
			specY = kuriY
			species = "KURIBOTCHI"
		elif tamagotchi == mukimukitchi:
			specY = mukiY
			species = "MUKIMUKITCHI"
		elif tamagotchi == tamatchi:
			specY = tamaY
			species = "TAMATCHI"
		else:
			specY = yasaY
			species = "YASAGURETCHI"
		specX = displayWidth * 0.4

		#INITIALIZING TAMAGOTCHI'S nickname VARIABLE
		response = input("Would you like to give your pet a nickname? (Y/N) ")
		print("")
		if response == "Y" or response == "y":
			nickname = input()
			tamaObj = Tamagotchi(species,nickname)
		else:
			tamaObj = Tamagotchi(species,None)

		displayShit = False
		timeSpent = 0
		shitTime = 0
	else:
		tamaObj = Tamagotchi(existingData[0],existingData[1])
		tamaObj.fullness = existingData[2]
		tamaObj.happiness = existingData[3]
		tamaObj.age = existingData[4]
		tamaObj.healthiness = existingData[5]

		print(tamaObj.species)

		if tamaObj.species == "HASHITAMATCHI":
			tamagotchi = hashitamatchi
		elif tamaObj.species == "KURIBOTCHI":
			tamagotchi = kuribotchi
		elif tamaObj.species == "MUKIMUKITCHI":
			tamagotchi = mukimukitchi
		elif tamaObj.species == "TAMATCHI":
			tamagotchi = tamatchi
		elif tamaObj.species == "YASAGURETCHI":
			tamagotchi = yasaguretchi
		
		displayShit = existingData[6]
		timeSpent = existingData[7]
		shitTime = existingData[8]
		specX = existingData[9]
		specY = existingData[10]
	
	gameExit = False
	timeElapsed = 0
	x_change = 0

	#[REAL-GAME LOOP]
	while not gameExit:
		
		start = timer()

		#FILL BACKGROUND WHITE
		gameDisplay.fill(white)

		#{EVENTS LOOP}
		for event in pygame.event.get():

			#IF EXIT IS CLICKED:
			if event.type == pygame.QUIT:
				gameExit = True
		
			#IF KEY IS PRESSED:
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					x_change = -5
				elif event.key == pygame.K_RIGHT:
					x_change = 5
			
			#IF KEY IS RELEASED:
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
					x_change = 0
			
			#IF MOUSE IS CLICKED...
			if event.type == pygame.MOUSEBUTTONDOWN:
				mx,my = pygame.mouse.get_pos()
				#print(mx,my)
				#BOTTOM BUTTONS
				if my > 488 and my <= 600:
					#DUCK BUTTON
					if mx >= 0 and mx < 194 and displayShit:
						displayShit = False
						shitTime = 0
					#FEED BUTTON
					elif mx > 194 and mx < 399:
						if tamaObj.fullness < 4:
							tamaObj.eat()
							if tamaObj.healthiness < 10:
								tamaObj.ayyy()
							try:
								print("You fed " + tamaObj.nickname + ".")
								print("")
							except:
								print("You fed " + tamaObj.species + ".")
								print("")
						else:
							if tamaObj.healthiness > 0:
								tamaObj.ouf()
								try:
									print(tamaObj.nickname + " is eating too much!")
									print("")
								except:
									print(tamaObj.species + " is eating too much!")
									print("")
					#SAVE BUTTON
					elif mx > 399 and mx < 603:
						print("Progress saved.")
						print("")
						saveData(tamaObj.species,tamaObj.nickname,tamaObj.fullness,tamaObj.happiness,tamaObj.age,tamaObj.healthiness,displayShit,timeSpent,shitTime,specX,specY)
					#PLAY BUTTON
					elif mx > 603 and mx <= 800:
						if tamaObj.happiness < 10:
							tamaObj.smile()
							try:
								print(tamaObj.nickname + " loved playing with you!")
								print("")
							except:
								print(tamaObj.species + " loved playing with you!")
								print("")
						else:
							try:
								print(tamaObj.nickname + " doesn't wanna play with you.")
								print("")
							except:
								print(tamaObj.species + " doesn't wanna play with you.")
								print("")		
				#TOP BUTTONS
				elif my >= 0 and my < 120:
					#MEDICINE BUTTON
					if mx > 349 and mx < 657:
						if tamaObj.healthiness < 2:
							tamaObj.ayyy()
							try:
								print(tamaObj.nickname + " got a bit better :)")
								print("")
							except:
								print(tamaObj.species + " got a bit better :)")
								print("")
						else:
							if tamaObj.healthiness > 0:
								tamaObj.ouf()
								try:
									print(tamaObj.nickname + " got a bit worse!")
									print("")
								except:
									print(tamaObj.species + " got a bit worse!")
									print("")
					#STATS BUTTON
					elif mx > 657 and mx < 800:
						print("Species: " + tamaObj.species)
						if tamaObj.nickname:
							print("Nickname: " + tamaObj.nickname)
						print("Fullness", tamaObj.fullness)
						print("Happiness:", tamaObj.happiness)
						print("Age:", tamaObj.age)
						print("Healthiness:", tamaObj.healthiness)
						print("")

		#REEVALUATE TAMAGOTCHI'S X-POSITION
		specX += x_change

		#DISPLAY IMAGES
		imageDisplay(specX,specY,tamagotchi)
		imageDisplay(0,490,duck)
		imageDisplay(199,490,feed)
		imageDisplay(403,490,save)
		imageDisplay(605,490,play)
		imageDisplay(340,0,medicine)
		imageDisplay(660,0,heart)

		#FPS
		clock.tick(60)

		end = timer()

		#ADDING TO SHITTIME
		if displayShit:
			shitTime += (end-start)

		#RECALCULATING TAMAGOTCHI'S ATTRIBUTES
		if pygame.time.get_ticks()//1000 != timeElapsed:
			timeElapsed = pygame.time.get_ticks()//1000
			timeSpent += 1
		tamaObj.age = timeSpent//60
		#IF 30 SECONDS PASS:
		if timeSpent % 30 == 0:
			if tamaObj.fullness > 0:
				tamaObj.fullness -= 1
			displayShit = True
			if int(shitTime) % 20:
				tamaObj.ouf()
				try:
					print(tamaObj.nickname + " got unhealthier :(")
					print("")
				except:
					print(tamaObj.species + " got unhealthier :(")
					print("")
						
		#DISPLAY SHIT
		if displayShit:
			imageDisplay(135,300,shit)

		#Consistently update screen
		pygame.display.update()

gameLoop(savedData)
pygame.quit()
quit()