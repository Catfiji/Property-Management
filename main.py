
import random
from os import system
from time import sleep



class House:

	def __init__(self, Name, Price, Health, IsOwned):
		self.name = Name 
		self.price = Price 
		self.health = Health
		self.IsOwned = IsOwned

	def list_self(self):

		print(self.name)
		print("price: $", self.price)
		print("Conditon: ", self.health)


names = ["Cock", "Paul", "Street", "Bob"]

def get_House_Name():
	l = random.choice(names)
	n = random.randint(200,800)
	n = str(n)
	name = f"{n} {l}"

	return name

house1 = House(get_House_Name(),random.randint(2000,8000), 50, False) # Price, Condition/Health

house2 = House(get_House_Name(), random.randint(2000,8000), 20, False) 

house3 = House(get_House_Name(), random.randint(2000,8000), 70, False) 

Houses = [house1, house2, house3] # QOL

def main():
	print("			Houses:")
	for i in Houses:
		i.list_self()
		print("\n")

main()
