a = eval(input("enter no of rows: "))
l = a*2
temp = a
while a>=1:
    b = 1
    while b<=l:
        if b>=a and ((a%2==1 and b%2==1)or(a%2==0 and b%2==0)) and b<= temp:
            print("*",end=" ")
        else:
            print(" ", end=" ")
        b = b+1
    print()   
    a = a-1
    temp = temp+15
    