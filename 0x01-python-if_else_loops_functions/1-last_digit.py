#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
num = str(number)[-1]
ori = str(number)
if int(num) > 5:
    print("Last digit of " + ori + " is " + num + " and is greater than 5")
elif int(num) == 0:
    print("Last digit of " + ori + " is " + num + " and is 0")
elif int(num) < 6:
    extra = " and is less than 6 and not 0"
    print("Last digit of " + ori + " is " + num + extra)
