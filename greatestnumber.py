a = 4
b = 4
c = 5

if a>b:
    if a>c:
        print("A is great!")
    elif a == c:
        print("A and c are equal and great!")
    else:
        print("C is great!")
elif b>c:
    if b>a:
        print("B is great!")
    else:
        print("A is great!")
elif a == b:
    print("A and B are equal and great!")
elif b == c:
    print("B and c are equal and great!")
else:
    print("C is great!")

