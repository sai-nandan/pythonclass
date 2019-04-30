print("This is pattern Module")

def printPattern():
    print("Printing Pattern!")

def printPattern2():
    print("Printing Pattern 2!")

def printTriangle():
    a = eval(input("Enter number of rows :"))
    l = a*2
    temp = a
    while a>=1:
        b = 1
        while b<=l:
            # print("*",end=" ")
            if b>=a and ((a%2==1 and b%2==1) or (a%2==0 and b%2==0)) and b<=temp:
                print("*", end=" ")
            else:
                print(" ",end=" ")
            b = b+1
        print()
        a = a-1
        temp = temp+1