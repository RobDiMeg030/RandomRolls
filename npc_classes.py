import random

class Enenmy:
    def __init__(self,type):
        self.type = type

        stats={
            "enemy": {
                "name": "Goblin",
                "hp": 12,
                "attack": random.randint(1, 4),
                "defense": random.randint(0, 2)
            },
            "boss": {
                "name": "Dämonenlord",
                "hp": 30,
                "attack": random.randint(5, 8),
                "defense": random.randint(2, 4)
            }
        }
        npc_stats = stats[type]

        self.name = npc_stats["name"]
        self.hp = npc_stats["hp"]
        self.attack = npc_stats["attack"]
        self.defense = npc_stats["defense"]



class Treasure:
    def __init__(self,type,inside):
        self.type = type
        self.inside = []
