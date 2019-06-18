class Cars:
    def __init__(self,car):
        self.name = car

    def display_car(self):
        print(self.name)

mycars = Cars("Audi")
mycars2 = Cars("Merc")

mycars.display_car()
mycars2.display_car()