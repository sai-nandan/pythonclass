def fibonacci(maxFib):
    a,b,num = 0,1,0
    print(a,b,end=" ")
    while num<maxFib:
        num = a+b
        a,b = b,num
        print(num,end=" ")
    print()
fibonacci(400)
fibonacci(1400)
fibonacci(50)