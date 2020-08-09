#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Student: Ngoc Pham (7891063)

#-----------------------------
#Exercise 1: Random walk:

import random
# random.seed(10122019)
import numpy
import matplotlib.pyplot as plt
# numpy.random.seed(10122019)

def random_walk_2D(np, ns):
    xpositions = numpy.zeros(np)
    ypositions = numpy.zeros(np)
    # extent of the axis in the plot:
    xymax = 3*numpy.sqrt(ns); xymin = -xymax

    NORTH = 1;  SOUTH = 2;  WEST = 3;  EAST = 4  # constants


# # SOLUTION 1:
#     direction_arr = numpy.random.randint(1,5,size=np*ns)  # 1D array
#     direction_arr.shape = (ns,np)                         # reshape to 2D array
    
#     # print(xpositions)
#     # print(ypositions)
#     # print(direction_arr)
    
#     for eachstep in range(ns):
#         d = direction_arr[eachstep]   # access row
#         # print(d)
#         ypositions += numpy.where(d == NORTH, 1, 0)
#         ypositions += numpy.where(d == SOUTH, -1, 0)        # OR: ypositions -= numpy.where(d == SOUTH, 1, 0)
#         xpositions += numpy.where(d == EAST, 1, 0)
#         xpositions += numpy.where(d == WEST, -1, 0)        # OR: xpositions -= numpy.where(d == SOUTH, 1, 0)
#         # print(xpositions)
#         # print(ypositions)       
        

# # SOLUTION 2:   
#     for step in range(ns):
#         directionX = numpy.random.randint(-1,2,np)
#         directionY = numpy.random.randint(-1,2,np)
#         xpositions += directionX
#         ypositions += directionY



# SOLUTION 3:
    for step in range(ns):
        directions = numpy.random.randint(1,5,size = np)
        
        ypositions += (directions == NORTH)
        ypositions -= (directions == SOUTH)       
        xpositions += (directions == EAST)
        xpositions -= (directions == WEST)

# #SOLUTION 4:
#     for step in range(ns):
#         direction = numpy.random.randint(1,5,np)
        
#         # print(direction)
#         # print(direction==NORTH)
#         # print(ypositions[direction == NORTH])      
        
#         ypositions[direction == NORTH] += 1
#         ypositions[direction == SOUTH] -= 1        
#         xpositions[direction == EAST] += 1
#         xpositions[direction == WEST] -= 1
        
        
        
        
# # SOLUTION 5: (2 for loops, similar to given problem, not too recommended)
        
#     for eachparticle in range(np):
#         step_arr = numpy.random.randint(1,5,size=ns)
#         for eachstep in step_arr:
#             if eachstep == NORTH:
#                 (dx,dy) = (1,0) 
#             if eachstep == SOUTH:
#                 (dx,dy) = (-1,0)            
#             if eachstep == WEST:
#                 (dx,dy) = (0,-1)
#             if eachstep == EAST:
#                 (dx,dy) = (0,1) 
#             xpositions[eachparticle] += dx
#             ypositions[eachparticle] += dy




 
# # BELOW CODES ARE GIVEN FROM PROBLEM:
#     for step in range(ns):
#         for i in range(np):
#             direction = random.randint(1, 4)
#             if direction == NORTH:
#                 ypositions[i] += 1
#             elif direction == SOUTH:
#                 ypositions[i] -= 1
#             elif direction == EAST:
#                 xpositions[i] += 1
#             elif direction == WEST:
#                 xpositions[i] -= 1



# plotting:
    plt.plot(xpositions, ypositions, 'ko')
    plt.axis([xymin, xymax, xymin, xymax])
    plt.title('{particles} particles after {steps} steps'.format(particles=np, steps=ns))
    plt.savefig('tmp_{steps}.pdf'.format(steps=ns))
    
    return xpositions, ypositions


# CALLING FUNCTION:
np        = 100  # number of particles
ns        = 100  # number of steps
x, y = random_walk_2D(np, ns)


#---------------------------------------
#Status: incomplete
#Challenge: multidimensional array:


import random
# random.seed(10122019)
import numpy
import matplotlib.pyplot as plt
# numpy.random.seed(10122019)


def random_walk_2D_2(np, ns):
    
    xymax = 3*numpy.sqrt(ns); xymin = -xymax
    
    coord_arr = numpy.zeros(shape=(np,2)) #array size npx2 , each point has x & y coordinate
    print("The x-y coordinates of particles: \n",coord_arr)

    NORTH = 1;  SOUTH = 2;  WEST = 3;  EAST = 4  # constants    
    
    for step in range(ns):
        step_arr = numpy.random.randint(1,5,np)
        print("The random walk: \n",step_arr)
        coord_arr[:,0] = coord_arr[:,0] + (step_arr==NORTH)
        coord_arr[:,0] = coord_arr[:,0] - (step_arr==SOUTH)
        coord_arr[:,1] = coord_arr[:,1] + (step_arr==EAST)
        coord_arr[:,1] = coord_arr[:,1] - (step_arr==WEST)    

    print("The NEW x-y coordinates of particles: \n",coord_arr)    
    xpositions = numpy.array(coord_arr[:,0])
    ypositions = numpy.array(coord_arr[:,1])
    
    plt.plot(xpositions, ypositions , 'ko')
    plt.axis([xymin, xymax, xymin, xymax])
    plt.title('{particles} particles after {steps} steps'.format(particles=np, steps=ns))
    plt.savefig('tmp_{steps}.pdf'.format(steps=ns))
    
    
    return xpositions, ypositions

np        = 100  # number of particles
ns        = 100  # number of steps
x, y = random_walk_2D_2(np, ns)



#---------------------------------------
#Super challenge: No loop (#D concept)
