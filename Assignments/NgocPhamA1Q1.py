# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 13:49:24 2020

@author: Ngoc Pham (7891063)
"""

#Question 1: Required
print("***Question 1: Required***")


#Step 1 - Reading file:
headings = []
observations = []
data = []

lineNum=0

reducedweather = open("reducedweather1.csv", 'r')
headings = reducedweather.readline().strip().split(',')
colNum = len(headings)


for col in range(colNum):
    observations.append([])  #create two empty lists nested inside a list "observations"

for line in reducedweather:
    data = line.split(',')   #data is [maxtemp,mintemp]
    lineNum += 1
    
    for listIndex in range(colNum):
        observations[listIndex].append(float(data[listIndex]))


#Step 2 - Calculating mean, highest and lowest temperature:
for listIndex in colNum:
    mean = sum(observations[listIndex])/len(observations[listIndex])

print(observations)

#Step 3 - Calculating Standard Deviation    



#Step 4 - Printing Output:


reducedweather.close()
#Question 2: Optional
print("***Question 2: Optional***")





#Programmed by...
import time
print ("\nProgrammed by Ngoc Pham (Student number: 7891063)")
print ("Date: " + time.ctime())
print ("End of processing")



