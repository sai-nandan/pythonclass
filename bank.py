import random
s = [0,1,2,3,4,5,6,7,8,9]
class Bank:
    def __init__(self):
        print('')

    def create_account(self):
        bank_code = '1319'
        random.shuffle(s)
        i   =   0
        acc =   0
        while i<=6:
            acc = acc*10 + s[i]
            # print(acc)
            i += 1
        if s[0]==0:
            acc = str(acc)
            acc = '0'+ acc
            # print(acc)
        accountNo = bank_code + str(acc)
        print(accountNo)
        def adding_Details(self):
            first_name  =   input('enter your first name: ').upper()
            sur_name    =   input('enter your surname: ').upper()
            date,month,year =  input('enter your date: '), input('enter your month: '), input('enter your year: ')
            print(first_name,' ',sur_name,' ',date,'/',month,'/',year)
        adding_Details(self)

        
        
acc_gen = Bank()
acc_gen.create_account()