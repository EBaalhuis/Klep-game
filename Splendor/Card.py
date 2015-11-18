class Card:
    def __init__(self, properties):
        self.rank = properties[0]
        self.gem = properties[1]
        self.costs = {}
        self.costs["white"] = properties[2]
        self.costs["green"] = properties[3]
        self.costs["black"] = properties[4]
        self.costs["blue"] = properties[5]
        self.costs["red"] = properties[6]
        self.points = properties[7]