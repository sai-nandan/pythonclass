import random

class Bank:
    def __init__(self):
        self.s = list(range(10))

    def create_account(self):
        bank_code = '1319'
        random.shuffle(self.s)
        i   =   0
        acc =   0
        while i<=6:
            acc = acc*10 + self.s[i]
            # print(acc)
            i += 1
        if self.s[0]==0:
            acc = str(acc)
            acc = '0'+ acc
            # print(acc)
        accountNo = bank_code + str(acc)
        print(accountNo)
        self.adding_Details()
    
    def adding_Details(self):
        first_name  =   input('enter your first name: ').upper()
        sur_name    =   input('enter your surname: ').upper()
        date,month,year =  input('enter your date: '), input('enter your month: '), input('enter your year: ')
        print(first_name,' ',sur_name,' ',date,'/',month,'/',year)

acc_gen = Bank()
acc_gen.create_account()
