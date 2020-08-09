# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 19:05:30 2020

@author: Ngoc Pham (7891063)
"""

#------------------------
#Exercise: Error checking:

temp = []
invalid = []
count = 0
avg = 0
sumNum = 0

infile = open("marks.txt")



for eachline in infile:
    data = eachline.strip("\n")
    temp.append(data)
    if data.isnumeric():
        if int(data) >= 0 and int(data) <= 100:
           count += 1
           sumNum += int(data)
           avg = sumNum/count 

        
        
print("Average of good data: {:.2f}".format(avg))
print("Bad data:")

invalid = list(enumerate(temp))

for eachitem in range(len(invalid)):
    if not invalid[eachitem][1].isnumeric():
        msg = "not numeric"
        print("Value '{}' on line {} is bad because '{}'".format(invalid[eachitem][1],invalid[eachitem][0],msg))
    else:
        if int(invalid[eachitem][1]) > 100:
            msg = "too big"
            print("Value '{}' on line {} is bad because '{}'".format(invalid[eachitem][1],invalid[eachitem][0],msg))    
    
    
    

         
