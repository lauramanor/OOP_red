class Feline():
    family = "Felidae"

    def __init__(self, name, bff):
        self.name = name
        self.best_friend = bff

    # def description(self):
    #     return self.name + "'s best friend is" + self.best_friend


class Lion(Feline):
    species = "P. leo"


class Tiger(Feline):
    species = "P. tigris"


class Cat(Feline):
    species = "F. catus"


hobbes = Feline("Hobbes", "Calvin")

pluto = Cat("Pluto", "Ms. Manor")
