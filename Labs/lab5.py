# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 23:24:08 2020

@author: Ngoc Pham (7891063)
"""

#----------------------------------
#Exercise 1: Summation of numbers:

sumNum=0
infile=open("lab5.csv")
for eachline in infile:
    num=int(eachline)
    infile.readline()
    sumNum += num
print(sumNum)
infile.close()


