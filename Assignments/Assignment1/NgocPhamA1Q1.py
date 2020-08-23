# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 13:49:24 2020

@author: Ngoc Pham (7891063)
"""

#Question 1: Required
print("***Question 1: Required***")

#----------------------------------------------
#Step 1 - Reading file:
headings = [] #["maxTemp","minTemp"]
observations = []  #[[all values in maxTemp column],[all values in minTemp column]]
data = [] #data = [maxTemp's val,minTemp's val]

lineNum=0

reducedweather = open("reducedweather.csv", encoding = 'UTF-8-sig')
headings = reducedweather.readline().strip().split(',')
columnNum = len(headings)


for eachInteration in range(columnNum):
    observations.append([])  #create two empty lists nested inside a list "observations"

for eachLine in reducedweather:
    data = eachLine.split(',')   #data = [maxTemp's val, minTemp's val]
    lineNum += 1
    
    for eachList in range(columnNum):
        observations[eachList].append(float(data[eachList])) #list1 contains all maxtemp values, list2 contains all mintemp values in observations


#----------------------------------------------
#Step 2 - Calculating mean, highest and lowest temperature:
means = [] #[[maxTemp's mean],[minTemp's mean]]
maxVals = [] #maxTemp's maximum value, minTemp's maximum value
minVals = [] #maxTemp's minimum value, minTemp's minimum value

for eachList in range(columnNum):
    sumList = sum(observations[eachList])
    meanList = sumList/len(observations[eachList])
    means.append(meanList)
    maxList = max(observations[eachList])
    maxVals.append(maxList)
    minList = min(observations[eachList])
    minVals.append(minList)



# print(observations)
# print(lineNum)
# print(len(observations[0]))
# print(len(observations[1]))
# print(means)
# print(maxVals)
# print(minVals)


#----------------------------------------------
#Step 3 - Calculating Standard Deviation    
import math
squaredDif = [] # squaredDif = [[maxTemp's list of squared differences],[minTemp's list of squared differences]]
sumSqDif = [] # sumSqDif = [maxTemp's sum of squared dif, minTemp's sum of squared dif]
stdDevs = [] # stdDev = [maxTemp's stddev, minTemp's stddev]

for eachInteration in range(columnNum):
    squaredDif.append([])  #create two empty lists nested inside a list "squaredDif"

for eachList in range(columnNum):
    sumSquaredDif = 0
    for eachVal in range(len(observations[eachList])):
        squaredDifVal = math.pow(observations[eachList][eachVal]-means[eachList],2)
        squaredDif[eachList].append(squaredDifVal)
        sumSquaredDif += squaredDifVal
    sumSqDif.append(sumSquaredDif)    
    stdDevVal = math.sqrt(sumSquaredDif/len(observations[eachList]))
    stdDevs.append(stdDevVal)


#----------------------------------------------
#Step 4 - Printing Output:

line0 =        '{0:^14s}|{1:^15s}|{2:^15s}|{3:^15s}|{4:^15s}'    # ^ default center text, s for formatting as string
iteratedLine0 ='{0:>14s}|{1:>15.2f}|{2:>15.2f}|{3:>15.2f}|{4:>15.2f}' # > default right align
iteratedLine1 = '-'* 14 + '+' + '-'* 15 + '+' + '-'* 15 + '+' + '-'* 15 + '+' + '-'* 15

print()
print(line0.format("Column Names","Means","Std Deviation","Highest Score","Lowest Score"))
print(iteratedLine1)
for eachList in range(columnNum):
    print(iteratedLine0.format(headings[eachList],means[eachList],stdDevs[eachList],maxVals[eachList],minVals[eachList]))
    print(iteratedLine1)

print()
reducedweather.close()




#----------------------------------------------
#Question 2: Optional
'''
Social Insurance Numbers (SINs) are issued by the Canadian Government for administering
various government programs. For example, a SIN is required for reporting of earned income
from employment. A SIN consists of 9 digits (eg. 046454286). Not all 9-digit numbers represent a
valid SIN. There is a simple validation process to determine if a 9-digit number is a valid SIN.
Below, we use an example will illustrate how the validation process works.
Suppose the 9-digit number to be validated is 046454286. Take the number 121212121 and write
it below 046454286 to get
046454286
121212121
Next, for each of the 9 digit positions, multiply the top and bottom digit to get
0 8 6 8 5 8 2 16 6
Next, add up all the digits together (note that 16 contains the digits 1 and 6) to get
0 + 8 + 6 + 8 + 5 + 8 + 2 + 1 + 6 + 6 = 50
If the sum from the previous line is evenly divisible by 10 (that is, no remainder), then the 9-digit
number is a valid SIN. If the sum from the previous line is not evenly divisible by 10, then it is not
a valid SIN. For the example 9-digit number 046454286, it is a valid SIN, since 50 is evenly divisible
by 10.
Write a program that reads in a 9-digit number and determine if it is a valid SIN.
Try your program with various 9-digit numbers including 630308902, 666234872, 056123456.
'''

print("***Question 2: Optional***")

SIN = input("Please enter a SIN number: > ")
number = '121212121'
stringTotal = ''
total = 0
print()

if len(SIN)!=9 or SIN.isdigit() == False:  #check input is 9-digit and input is a number, no chars allowed
    print("You have entered an invalid SIN number. Please check SIN again.")
else:
    for eachDigit in range(len(SIN)):
        digit = int(SIN[eachDigit])
        multiplier = int(number[eachDigit])
        product = digit * multiplier
        stringTotal += str(product)
        
    for eachStringDigit in range(len(stringTotal)):
        value = int(stringTotal[eachStringDigit])
        total += value
        
    if total % 10 == 0:
        print("Congrats! This is a valid SIN number.")
    else:
        print("Unfortunately, after checking, this is NOT a valid SIN number.")



#----------------------------------------------
#Programmed by...
print()
import time
print ("\nProgrammed by Ngoc Pham (Student number: 7891063)")
print ("Date: " + time.ctime())
print ("End of processing")



