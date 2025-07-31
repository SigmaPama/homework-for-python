class Adress:
    def __init__(self, index, town, street, house, room):
        self.index = index
        self.town = town
        self.street = street
        self.house = house
        self.room = room

    def __str__(self):
        return f"{self.index}, {self.town}, {self.street}, {self.house} - {self.room}"