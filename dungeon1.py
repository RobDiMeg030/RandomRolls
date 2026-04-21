import random
from action_class import *
from npc_classes import *
from item_class import *
from player_class import *

from sqlalchemy.sql.operators import truediv


# room class

class Room:
    def __init__(self, type):
        self.type = type


    def describe(self):
        description = {
             "enemy": "A hostile enemy appears!",
            "treasure": "There is a treasure chest in the room.",
            "empty": "The room is empty.",
            "junction": "There is a junction ahead.",
            "merchant": "You arrive at the merchant.",
            "boss": "A powerful boss stands before you!"



        }
        return description[self.type]







# dungeon class
class Dungeon:
    def __init__(self, size=6):
        self.rooms = self.generate_dungeon(size)

    def generate_dungeon(self, size):
        rooms = []
        room_types = ["enemy", "treasure", "empty", "merchant"]

        unique=["treasure","merchant"] # theese rooms can only be appear once per run
        used_unique=set()

        rooms.append(Room("enemy")) ## first room is a enemy

        for _ in range(size - 2):
            possible=[]

            for r in room_types:
                if r in used_unique and r in unique:
                    continue

                possible.append(r)

            chosen=random.choice(possible)
            if chosen in unique:
                used_unique.add(chosen)

            rooms.append(Room(chosen))

        rooms.append(Room("boss"))
        return rooms

# test

def load_items():
    global ITEMS
    with open("items.json") as f:
        data = json.load(f)

    for item_data in data:
        item_id = item_data["id"]
        ITEMS[item_id] = Item.from_json(item_data)

### main game

def main():
    dungeon=Dungeon(size=6)
    player = Player()
    load_items()

    ###test

    player.inventory.append(ITEMS["healing_potion"])

    print("Welcome to Dungeon !!!")
    for i,room in enumerate(dungeon.rooms):
        print(f"{i}. {room.describe()}")
        if room.type == "enemy":
            npc = Enenmy("enemy")
            action = Action("fight", None)
            action.fight(player, npc)


        elif room.type == "boss":
            npc = Enenmy("boss")
            action = Action("fight", None)
            action.fight(player, npc)

        input("Press Enter to continue in the dungeon...")

    print("LEVEL CLEARED !!!!!")

if __name__ == "__main__":
    load_items()
    player=Player()

    main()
