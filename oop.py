# object oriented programing
name = input('enter your name: ')
bank = input('enter your bank:')
class Details:

    def __init__(self,name,bank):
        self.name = name
        self.bank = bank

    def display_details(self):
        print (self.name,self.bank)
        # print (self.bank)

c1 = Details(name,bank)
c2 = Details('kanthi','andhra bank')

c1.display_details()
c2.display_details()