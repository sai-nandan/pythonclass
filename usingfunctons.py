#fibanocci numbers
def fabmax(a=0,b=1,num=0,x=0):
        num= int(input("Enter a number: " end=" "))
        while(x<num):
                x = a+b
                a=b
                b=x
                print(x, end=" ")
