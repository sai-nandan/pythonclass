n = int(input(" enter a number: "))
sum = 0
while n>0:
    d = n%10
    sum = sum + (d*d*d)
    n = n//10
print(" sum of cubes of number is: ",sum)