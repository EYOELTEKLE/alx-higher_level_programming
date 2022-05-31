#!/usr/bin/python3
def uppercase(str):
    new = ''
    for i in str:
        temp = ord(i) - 32
        if temp >= 65 and temp <= 90:
            new = new + chr(temp)
        else:
            new = new + i
        print(new)
