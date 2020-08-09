# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 17:09:40 2020

@author: Ngoc Pham
"""


def calculateMean(data):
    """
    This function computes the mean of each column 
    ontaining data which includes Manitoba daily minimum and maximum temperatures
    from Jan until Sept 17 in 2019.   
    @param data - a list of floating point values, single list & not nested
    @return mean - mean of each column that the function performs calculation on
    """
    sumData = sum(data)
    mean = sumData / len(data)
    return mean



def calculateStdDev(data,mean):
    """
    This function computes the standard deviation of each column 
    containing data which includes Manitoba daily minimum and maximum temperatures
    from Jan until Sept 17 in 2019.   
    @param data - a list of floating point values, single list & not nested
    @para mean - mean of each column 
    @return stdDevs that the function performs calculation on
    """    
    import math
        
    sumSquaredDif = 0
    for eachVal in range(len(data)):
        squaredDifVal = math.pow(data[eachVal]-mean,2)
        sumSquaredDif += squaredDifVal
        
    stdDev = math.sqrt(sumSquaredDif/len(data))
    
    return stdDev



def findMin(data):
    """
    This function return the minimum value of each column 
    containing data which includes Manitoba daily minimum and maximum temperatures
    from Jan until Sept 17 in 2019.   
    @param data - a list of floating point values, single list & not nested
    @return minVal that the function performs calculation on
    """
    minVal = data[0]
    for eachVal in range(len(data)):
        if data[eachVal] < minVal:
            minVal = data[eachVal]
    
    return minVal


def findMax(data,mean):
    """
    This function return the maximum value of each column 
    containing data which includes Manitoba daily minimum and maximum temperatures
    from Jan until Sept 17 in 2019.   
    @param data - a list of floating point values, single list & not nested
    @para mean - passing value, no calculations performed
    @return maxVal that the function performs calculation on
    """
    maxVal = data[0]
    for eachVal in range(len(data)):
        if data[eachVal] > maxVal:
            maxVal = data[eachVal]
   
    return maxVal






