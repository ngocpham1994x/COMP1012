# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 16:45:45 2020

@author: Ngoc Pham (7891063)
"""


#Exercise 1: Sum of values in a file
print("---Exercise 1: Sum of values in a file---")
print()
count = 0
total = 0
infile = open("lab3text.txt",'r')

for eachline in infile:
    count += 1
    total += int(eachline)


print("Numbers of numbers: {}".format(count))
print("Total: {}".format(total))
infile.close()
print()



#----------------------------------------------
#Exercise 2: sum of digits
print("---Exercise 2: sum of digits---")
countchar = 0
sumchar = 0

number = input("Provide a number: > ")
for eachchar in number:
    countchar += 1
    sumchar += int(eachchar)

print("There are {} digits and the sum of the digits is {}.".format(countchar,sumchar))
print()


#----------------------------------------------
#Optional : Sanitize a string
print("---Optional : Sanitize a string---")
string = input("Please input a string: > ")
stringAfter = string.strip().replace("~","").replace("!","").replace("-","")
print("Sanitized string: > {}".format(stringAfter))
print()



#----------------------------------------------
#Optional: Volume of a cone
print("---Optional: Volume of a cone---")
import math
radius = int(input("What is the radius of your cone (in cm)? > "))
height = int(input("What is the height of your cone (in cm)? > "))
volume = math.pi*math.pow(radius,2)*height/3
print("The volume is {:.2f} cm^2".format(volume))
print()


#----------------------------------------------
#Optional: Binary to Decimal
print("---Optional: Binary to Decimal---")
binaryNum = input("Please input a binary number > ")
countlen = len(binaryNum)
decimal = 0
listDigit = []
order = 0

for eachdigit in binaryNum:
    countlen -= 1
    binaryDigit = binaryNum[countlen]
    listDigit.append(int(binaryDigit))
    decimal += listDigit[order]*2**(order)
    order += 1

print("The number in decimal is {}.".format(decimal))
