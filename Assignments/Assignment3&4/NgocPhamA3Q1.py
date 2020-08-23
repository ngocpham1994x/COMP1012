# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
# import matplotlib.pyplot as plt



#--------------------------------------------------------------


def generatePoints(aa,bb,interval):
    """
    This function generates points using arange function where:
    @param aa - starting point (inclusive)
    @para bb - ending point (exclusive)
    @para interval - interval, or step between points
    @return xx - an array of values of x
    """
    xx = np.arange(aa,bb,interval)
    return xx


def evalFunction(xx):
    """
    This function takes one parameter as input.
    The input is an array of x values. Each value of x will correspond to
    one value of y, as per a math function: y=f(x)=(2/3)(x-1)^(5/2).
    This function will return an array of corresponding y values.
    @param xx - an array of values of x
    @return yy - an array of values of y
    """
    coefficient = 2/3
    power = 5/2
    shifting = -1
    yy = (coefficient)*(np.power((xx+shifting),power))
    return yy


def calculateSegmentDists(xx,yy):
    """
    This function takes two numpy array as inputs.
    The values in the xx array indicate x-axis and values in yy array indicates y-axis values. 
    It then calcualtes the distance between two neighboring points.
    Then it produces an array of neighboring distances, for the particular segment of x-values
    Here, the neighboring distances are called the "Euclidean distance between the neighboring points".
    This function will return an array of corresponding neighboring distance values,
    of the particular segment, which is |p(i),p(i+1)|.
    For example, an array arr = [1 2 3 4 5], the difference between two neighboring points is
    [2 3 4 5]    # this is arr[1:]
    -
    [1 2 3 4]    # this is arr[0:(len(arr)-1)]
    =
    [1 1 1 1]    # notice size of this array is 1 less than arr array
    @param xx - an array of values of x
    @param yy - an array of values of y 
    @return segDists - an array of neighboring distances of particular segment
    """    
    dx = xx[1:(len(xx))] - xx[0:(len(xx)-1)]
    dy = yy[1:(len(yy))] - yy[0:(len(yy)-1)]       # higher bounds are exclusive
    
    sq_dx = np.square(dx)
    sq_dy = np.square(dy)
    
    segDists = np.sqrt(sq_dx + sq_dy)
    
    return segDists


def calculateCurveLen(segDists):
    """
    This function takes neighboring distances of the particular segment as input and returns the segment length.
    The function sums all neighboring distances within the limits of x-values,
    then produces the length of the particular segment within limits of x-values.
    @param segDists - an array of neighboring distances of particular segment
    @return length - length of the segment on x values
    """  
    length = np.sum(segDists)
    return length


def calculateSurfaceArea(segDists,yy):
    """
    This function takes two numpy array as inputs.
    The values of  neighboring distances of the particular segment and values of functional y.
    Function then calculates the surface area between two neighboring points,
    then function sums all the areas to produce the segment area. 
    Here, the surface area is calculated as frustum. See the link below for details.
    [tutorial.math.lamar.edu/Classes/CalcII/SurfaceArea.aspx].
    For example, an array arr = [1 2 3 4 5], the difference between two neighboring points is
    [2 3 4 5]    # this is arr[1:]
    -
    [1 2 3 4]    # this is arr[0:(len(arr)-1)]
    =
    [1 1 1 1]    # notice size of this array is 1 less than arr array
    @param yy - an array of values of y 
    @param segDists - an array of segment distances between neighboring points
    @return area - area of the segment on x values
    """     
    sumY = yy[1:(len(yy))] + yy[0:(len(yy)-1)]        # higher bounds are exclusive
    
    area_arr = 2*np.pi*((1/2)*sumY)*segDists

    area = np.sum(area_arr)
    
    return area


def printValues(starts,ends,lengths, areas):
    """
    This function prints the output, which contains the data of all segments.
    There are 10 segments total, according to the main() function.
    Each segment will have data of: 
    start/end - which x values for starting point and ending point
    length - length of the particular segment in m
    area - surface area of the particular segment in m^2
    """  
    line0 =        '{0:<11}|{1:^10s}|{2:^10s}'    # default center & left align, s for formatting as string
    iteratedLine0 = '{0:>2d} ... {1:>3d} |{2:<10.3e}|{3:<10.3e}' # default right & left align
    iteratedLine1 = '-'* 11 + '+' + '-'* 10 + '+' + '-'* 10
    
    print()
    print(line0.format("start/end","length (m)","area (m^2)"))
    print(iteratedLine1)
    for i in range(len(starts)):
        result = iteratedLine0.format(starts[i],ends[i],lengths[i],areas[i]) +"\n" + iteratedLine1
        print(result)

    return


def main():
    
    starts = []
    ends = []
    lengths = []
    areas = []
    
    
    # # Extra: Plotting the function y=f(x)    
    # xList = []
    # yList = []
    
    for i in range(1,100,10):   # 1, 11, 21, 31, 41, 51, 61, 71, 81, 91
        xx = generatePoints(i,i+10,1)
        yy = evalFunction(xx)
        segDists = calculateSegmentDists(xx,yy)
        length = calculateCurveLen(segDists)
        area = calculateSurfaceArea(segDists,yy)
        
        # adding item to the lists
        starts.append(i)
        ends.append(i+9)
        lengths.append(length)
        areas.append(area)
        
    # # Extra: Plotting the function y=f(x)        
    #     xxList = list(xx)
    #     xList += xxList
    #     yyList = list(yy)
    #     yList += yyList


    printValues(starts,ends,lengths, areas)
    
    
    
    # # Extra: Plotting the function y=f(x)
    # x_arr = np.array(xList)
    # y_arr = np.array(yList)

    
    # plt.plot(x_arr, y_arr, 'ko')
    # plt.axis([0,10,0,200])
    # plt.title("y = (2/3)(x-1)^(5/2)")

    
    return



#--------------------------------------------------------------

main()


# PROGRAM BY....
import time
print ("\nProgrammed by Ngoc Pham (7891063)")
print ("Date: " + time.ctime())
print ("End of processing")