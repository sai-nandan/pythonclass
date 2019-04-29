def pattern(n):
    a,b=1,1
    while a<=n:
        while b>=a and b<=n:
            print(b,end =" ")
            b=b+1
        a=a+1
        print()
pattern(4)
