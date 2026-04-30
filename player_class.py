import random
from item_class import Item
from sympy import false

from item_class import *
class Player:
    def __init__(self):
        self.hp= 25
        self.attack=random.randint(3,7)
        self.defense=random.randint(2,5)
        self.inventory=[]
        self.weapon=[]
        self.armor=[]
        self.artifact=[]


    def choose_item(self):
        if len(self.inventory)==0:
            print("You don't have any items in your inventory.")
            return False, None
        if len(self.inventory)<3:
            print("You have following Items in your inventory:")
            for i,id in enumerate(self.inventory, start=1):
                #print(id.id)
                #print(self.inventory)
                print(f"{i}. {ITEMS[id.id].name}")

            while True:
                choice = input("Which item do you want to use? Enter number: ")

                if not choice.isdigit():
                    print("Please enter a valid number.")
                    continue

                choice = int(choice)

                if 1 <= choice <= len(self.inventory):
                    selected_item = self.inventory[choice - 1]
                    print(f"You selected: {selected_item.name}")
                    return True, self.inventory[choice - 1]
                else:
                    print("Number out of range. Try again.")


    def equip(self,item:Item):
        if "weapon" in  item.tags:
            self.weapon.append(item)
        elif "armor" in item.tags:
            self.armor.append(item)
        elif "artifact" in item.tags:
            self.artifact.append(item)
        else:
            self.inventory.append(item)

    def buff_increase(self,item:Item):
        if item.buff_type=="attack":
            self.attack+=item.buff_value
        elif item.buff_type=="defense":
            self.defense+=item.buff_value
        elif item.buff_type=="hp":
            print("HP Healed")
            self.hp+=item.buff_value

# invertor=[Item["healing"],Item["Sword"]]

