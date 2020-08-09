# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 08:59:44 2020

@author: Ngoc Pham (7891063)
"""


#----------------------------------------------
#Exercise 1: Standard deviation
import math
infile = open("lab4.csv")
firstCol = []
secCol = []
thirdCol = []
count = 0

for eachline in infile:
    firstNum,secNum,thirdNum = eachline.strip().split(',')
    firstCol.append(float(firstNum))
    secCol.append(float(secNum))
    thirdCol.append(float(thirdNum))
    count += 1
    
mean1 = sum(firstCol)/ count
mean2 = sum(secCol)/ count
mean3 = sum(thirdCol)/ count

squaredDif1 = 0
squaredDif2 = 0
squaredDif3 = 0

for eachitem in range(len(firstCol)):
    squaredDif1 += math.pow(firstCol[eachitem] - mean1,2)
for eachitem in range(len(secCol)):
    squaredDif2 += math.pow(secCol[eachitem] - mean2,2)
for eachitem in range(len(thirdCol)):
    squaredDif3 += math.pow(thirdCol[eachitem] - mean3,2)


stdDev1 = 0
stdDev2 = 0
stdDev3 = 0

stdDev1 = math.sqrt(squaredDif1/(len(firstCol)-1))
stdDev2 = math.sqrt(squaredDif2/(len(secCol)-1))
stdDev3 = math.sqrt(squaredDif3/(len(thirdCol)-1))

print("The mean of column 1 is {:.2f}, and the standard deviation is {:.2f}".format(mean1,stdDev1))
print("The mean of column 2 is {:.2f}, and the standard deviation is {:.2f}".format(mean2,stdDev2))
print("The mean of column 3 is {:.2f}, and the standard deviation is {:.2f}".format(mean3,stdDev3))
    

#----------------------------------------------
#Exercise 2: Standard deviations from the mean    

num=int(input("Give me a number : > "))

devFromMean1 = abs(mean1-num)/stdDev1
devFromMean2 = abs(mean2-num)/stdDev2
devFromMean3 = abs(mean3-num)/stdDev3

print("This number is {:.4f} standard deviations from the mean for column 1.".format(devFromMean1))
print("This number is {:.4f} standard deviations from the mean for column 2.".format(devFromMean2))
print("This number is {:.4f} standard deviations from the mean for column 3.".format(devFromMean3))

infile.close()





#----------------------------------------------
#Optional: Exercise 1: Standard deviation - Using Nested list

infile = open("lab4.csv")
colNum = 3  #considered this is given from the problem
numList = []
means = []
squaredDif = []
stdDev = []
lineNum = 0

for eachiteration in range(colNum):
    numList.append([])

for eachline in infile:
    data = eachline.strip().split(',')
    lineNum += 1
    
    for eachList in range(colNum):
        numList[eachList].append(float(data[eachList])) 


squaredDifVal = 0

for eachList in range(colNum):
    means.append(sum(numList[eachList])/lineNum)
    for eachitem in range(len(numList[eachList])):
        squaredDifVal += math.pow(numList[eachList][eachitem]-means[eachList],2)    
    squaredDif.append(squaredDifVal)
    stdDev.append(math.sqrt(squaredDifVal/(len(numList[eachList])-1)))

print()
print("Std Dev using Nested List")
print(stdDev)


#----------------------------------------------
#Optional: Exercise 2: Standard deviations from the mean - Using Nested list

devFromMean = []
devFromMeanVal = 0

testnum=int(input("Give me a number : > "))

for eachList in range(colNum):
    devFromMeanVal = abs(means[eachList]-num)/stdDev[eachList]
    devFromMean.append(devFromMeanVal)
    
    
print()
print("Dev From Mean using Nested List") 
print(devFromMean)   

infile.close()