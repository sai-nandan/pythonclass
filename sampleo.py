print("Hello python team!")

name = input("Enter name :")
score = int(input("Enter score :"))

print(name+" got "+str(score))

if score>75:
    print("Distinction!")
elif score >=60:
    print("First class!")
elif score>55:
    print("Second class!")
elif score>45:
    print("Third class!")
else:
    print("Fail")

print("Completed")