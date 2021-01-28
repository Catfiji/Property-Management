
import random 
from os import system
from time import sleep

class player:
	def __init__(self, balance):
		self.balance = balance 

class House:

	def __init__(self, Name, Price, Health, IsOwned):
		self.name = Name 
		self.price = Price 
		self.health = Health
		self.IsOwned = IsOwned
		self.sell_price = self.price * 100 / 40
	

	def list_self(self):
		print(self.name)
		print("price: $", self.price)
		print("Conditon: ", self.health)
		print(self.sell_price)

names = ["Cock", "Paul", "Street", "Bob"]

def get_House_Name():
	l = random.choice(names)
	n = random.randint(200,800)
	n = str(n)
	name = f"{n} {l}"

	return name
pla = player(10000)
house1 = House(get_House_Name(),random.randint(3000,9000), random.randint(50,90), False) # Price, Condition/Health

house2 = House(get_House_Name(), random.randint(2000,8000), random.randint(40,90), False) 


house3 = House(get_House_Name(), random.randint(2000,8000), random.randint(40,90), False) 
starter_Houses = [house1, house2, house3] # QOL
starter_home = None
owned_houses = []

counter = 0

def inv():
	system('clear')
	print(f"		Balance: {pla.balance}\n")
	print("		Owned Houses:\n")
	counter = 0

  for i in owned_houses:
		counter += 1
		print(f"[{counter}]")

  i.list_self()
	user_input = input("")
	user_input = int(user_input) - 1
	try:
		house = owned_houses[user_input]
		
	except:

    print("Do not own house")

  user_input = input("[1] fix house [2] sell house ")

def house_menu():
	global Houses
	global counter
	global starter_home
	print("			Houses:")
	for i in starter_Houses:
		counter += 1
		print(f"[{counter}]")
		i.list_self()
		print("\n")
	user_input = input("")
  
  user_input = int(user_input) - 1
  
  if user_input > -1 and user_input < 3:
	
  starter_home = starter_Houses[user_input]
		owned_houses.append(starter_home)
		pla.balance -= starter_home.price
	
	else:
		print("Pick a actual number!")
	inv()
