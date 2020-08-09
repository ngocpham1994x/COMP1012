# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 17:09:54 2020

@author: Ngoc Pham
"""

def readCSVFile(fileName):
    """
    This function reads the given file and returns data as two lists. The given file
    contains data which includes Manitoba daily minimum and maximum temperatures
    from Jan until Sept 17 in 2019.   
    @param fileName - a name of a given file, including file extension, string type  
    @return headings (as a single list, not nested), data (nested list) that the function performs work on
    """
    
    
    infile = open(fileName, encoding = 'UTF-8-sig')
    headings = infile.readline().strip().split(",")
    data = []
    columnNum = len(headings)
    
    for eachInteration in range(columnNum):
        data.append([])  #create two empty lists nested inside a list "data"
    
    for eachLine in infile:
        rowData = eachLine.split(',')   #rowVal = [maxTemp's val, minTemp's val]
        for eachList in range(columnNum):
            data[eachList].append(float(rowData[eachList])) #list1 contains all maxtemp values, list2 contains all mintemp values in data
    
    infile.close()
    return headings, data




def printCSVResults(headings,means, stdDevs, maxs, mins):
    """
    This function returns the headings,means, stdDevs, mins, maxs values of each column. The file 
    contains data which includes Manitoba daily minimum and maximum temperatures
    from Jan until Sept 17 in 2019.   
    @param headings,means, stdDevs, mins, maxs - each is a list, not nested
    @return nothing, but function print the proper requested format 
    """
    
    line0 =        '{0:^14s}|{1:^15s}|{2:^15s}|{3:^15s}|{4:^15s}'    # ^ default center text, s for formatting as string
    iteratedLine0 = '{0:>14s}|{1:>15.2f}|{2:>15.2f}|{3:>15.2f}|{4:>15.2f}' # > default right align
    iteratedLine1 = '-'* 14 + '+' + '-'* 15 + '+' + '-'* 15 + '+' + '-'* 15 + '+' + '-'* 15
    
    print()
    print(line0.format("Column Names","Means","Std Deviation","Highest Score","Lowest Score"))
    print(iteratedLine1)
    for i in range(len(headings)):
        result = iteratedLine0.format(headings[i],means[i],stdDevs[i],maxs[i],mins[i]) +"\n" + iteratedLine1
        print(result)

    
    return




def main():
    import StatisticsCalculation

    meanList = []
    stdDevList = []
    minList = []
    maxList = []
    
    
    fileName = input("Enter file name: ")
    headings, data = readCSVFile(fileName)

    for eachList in range(len(headings)):
        meanVal = StatisticsCalculation.calculateMean(data[eachList])
        meanList.append(meanVal)
        stdDevVal = StatisticsCalculation.calculateStdDev(data[eachList], meanList[eachList])
        stdDevList.append(stdDevVal)
        minVal = StatisticsCalculation.findMin(data[eachList])
        minList.append(minVal)
        maxVal = StatisticsCalculation.findMax(data[eachList],meanList[eachList])
        maxList.append(maxVal)
    

    printCSVResults(headings,meanList,stdDevList,maxList,minList)

        
    return