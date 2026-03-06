class Item:
    def __init__(self, name, description="", action="", gold_value=0,
                 buff_type=None, buff_value=0, rarity="common", tags=None):
        self.name = name
        self.description = description
        self.action = action
        self.gold_value = int(gold_value)
        self.buff_type = buff_type
        self.buff_value = int(buff_value)
        self.rarity = rarity
        self.tags = list(tags) if tags is not None else []
