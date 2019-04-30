print("this is loops module")

def printLoop():
    print("Printing Loop!")

def printLoop2():
    print("Printing Loop 2!")

def printNumpattern(count):
    temp=a=b= count
    while a >= 1:
        b=temp
        while b >= a:
            print(b,end=" ")
            b = b-1
        a = a-1
        print()