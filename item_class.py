import json

ITEMS={}

class Item:
    def __init__(self,id,name, description="", action="", gold_value=0,
                 buff_type=None, buff_value=0, rarity="common", tags=None):
        self.id=id
        self.name = name
        self.description = description
        self.action = action
        self.gold_value = int(gold_value)
        self.buff_type = buff_type
        self.buff_value = int(buff_value)
        self.rarity = rarity
        self.tags = list(tags) if tags is not None else []

    @classmethod
    def from_dict(cls, data):
        return cls(**data)
    @staticmethod
    def from_json(data):
        return Item(
            id=data["id"],
            name=data["name"],
            description=data["description"],
            action=data["action"],
            gold_value=data["gold_value"],
            buff_type=data["buff_type"],
            buff_value=data["buff_value"],
            rarity=data["rarity"],
            tags=data["tags"]
        )







