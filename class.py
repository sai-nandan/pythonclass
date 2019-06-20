class Cars:
    def __init__(self,car):
        self.name = car
        self.color = "Black"

    def display_car(self):
        print(self.name)
        print(self.color)

    def add_color(self,c):
        self.color = c

mycars = Cars("Audi")
mycars2 = Cars("Merc")

mycars.display_car()
mycars2.display_car()
mycars.add_color("white")
mycars.display_car()
mycars2.display_car()