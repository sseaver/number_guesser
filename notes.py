
import random

print (random.randint(1, 20))

sams_age = input("How old are you?")
sams_age = int(sams_age)
sarahs_age = 34

# Boolean

print (sams_age > sarahs_age)

if sams_age > sarahs_age:
    print ("You are older than Sarah.")
elif sams_age == sarahs_age:
    print ("You are the same age as Sarah")
else:
    print ("You are NOT older than Sarah.")
