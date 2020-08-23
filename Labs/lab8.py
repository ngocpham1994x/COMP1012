# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 07:59:40 2020

@author: Ngoc Pham (7891063)
"""

#--------------------------------------------------------
#Question 1 (Required): Estimating the volume of a Sphere
'''
Estimating the volume of a Sphere
A sphere with a radius of 1 (centered at point the point (0,0,0) ) is given by the equation . 
This unit sphere has volume (4/3)*pi
If you restrict this sphere to non-negative values of x,y,z, then its volume is (pi/6) ,
which is approximately 0.524 (we got this by dividing ((4/3)*pi)/8
So if we were to generate a (uniformly) random point (x,y,z) in the cube [0,1)x[0,1)x[0,1) , 
the point should have about a 52.4 % probability of landing inside the sphere because the unit cube has volume 1. 
This means that we can approximate 𝜋  using the relative frequency of randomly generated points (x,y,z) 
that lie in the sphere multiplied by 6.

You are going to write a script that will estimate 𝜋 by following the following steps:

1. Have a loop that runs TRIALS number of times, where TRIALS is the number of times we will generate points.
For testing use 1,000,000 for TRIALS.
2. Use random.random() to generate uniformly random values from the interval [0.0,1.0). 
Generate one for x, one for y and one for z. This will be a give a random point (x,y,z) belongs to [0,1)x[0,1)x[0,1)
3. With your random  point, see if the points are within the sphere. The point  are in the sphere if 
4. Estimate 𝜋 with 𝜋 = 6*(number of points inside sphere)/(number of trials)
 
Print out your estimation of 𝜋 , and the number of trials you did to get there.

Example, created with seed of 1000, your output should look like:

Estimating pi using (seed=1000)
Number of trials: 1000000, estimation of pi: 3.133602
'''



print("**Question 1: \n")

import math
import random

x = []
y = []
z = []
count = 0
pi = 0

TRIALS = int(input("Enter number of TRIALS: "))
seedNum = int(input("Enter number of seed: "))

random.seed(seedNum)

for iteration in range(TRIALS):
    x.append(random.random())
    y.append(random.random())
    z.append(random.random())
    res = x[iteration]**2 + y[iteration]**2 + z[iteration]**2
    if res < 1:
        count += 1

pi = 6 * count / TRIALS
    
print()
print("Estimating pi using (seed= {})".format(seedNum))
print("Number of trials: {}, estimation of pi: {}".format(TRIALS, pi))
print("|error| =  \n",math.fabs(pi-math.pi))






#--------------------------------------------------------
#Status: incomplete
#Question 1 - Challenge (optional) - automatic precision

# import math

# precision = int(input("How many digits of precision are required? "))

# piRound = round(pi,precision)
# difference = math.pi - pi

# while difference > 0:
#     TRIALS += 1000
#     for iteration in range(TRIALS):
#         x.append(random.random())
#         y.append(random.random())
#         z.append(random.random())
#         res = x[iteration]**2 + y[iteration]**2 + z[iteration]**2
#         if res < 1:
#             count += 1
#     pi = 6 * count / TRIALS


# print()
# print("Estimating pi using (seed= {})".format(seedNum))
# print("Number of trials: {}, estimation of pi: {}\n".format(TRIALS, pi))







#----------------------------------------------------------------
#Question 1 - Super challenge (optional) - fixed-point arithmetic




#--------------------------------------------
#Question 2 (Required): Rock, Paper, Scissors
'''
In general, both players randomly choose a signal from “rock”, “paper” and “scissors”. 
Rock beats scissors, scissors beats paper, paper beats rock. 
If both players choose the same signal, it is a “push”, and neither player wins.
You can simulate a player’s choices by choosing from a list, where each element of the list 
is a string that is either “rock”, “paper” or “scissors”. 
Use random.choice to randomly choose an element from the list of signals.

Create a simulation that runs 100 rounds of “Rock, Paper, Scissors” between 
two players named “Right” and “Left”.
Track how many times the right wins, how many times left wins, and how many pushes there are.

Using the seed 42, your result should be:

Simulating rock, paper, scissors (seed=42)
Trials: 100, Left win %: 40.0, Right win %: 36.0, Push %: 24.0
How would the results change if left only ever uses rock?
'''

print("**Question 2: using list \n")

import random

choiceA = ["rock","paper","scissor"]   #a list
push = 0
leftwin = 0
rightwin = 0


ROUNDS = int(input("Enter number of ROUNDS: "))
seedNum2 = int(input("Enter number of seed: "))

random.seed(seedNum2)

for eachround in range(ROUNDS):
    right = random.choice(choiceA)
    left = random.choice(choiceA)
    if left == right:
        push += 1
    elif left == "rock":
        if right == "paper":
            rightwin += 1
        else:
            leftwin += 1
    elif left == "paper":
        if right == "rock":
            leftwin += 1
        else:
            rightwin += 1   
    elif left == "scissor":
        if right == "rock":
            rightwin += 1
        else:
            leftwin += 1            
                       
            
pushPercent = (push / ROUNDS) * 100
leftPercent = (leftwin / ROUNDS) * 100
rightPercent = (rightwin / ROUNDS) * 100

print()
print("Simulating rock, paper, scissors (seed={})".format(seedNum2))
print("Trials: {}, Left win %: {}, Right win %: {}, Push %: {} \n".format(ROUNDS,leftPercent,rightPercent,pushPercent))

#-----------------------
#Question 2 - Challenge: optimized by using dictionary


print("**Question 2: using dictionary \n")

choiceB = {0: "Rock", 1: "Paper", 2: "Scissors"}    #a dictionary
push = 0
leftwin = 0
rightwin = 0

import random

def compare(left,right):
    
    results = { 
              ('Paper','Scissors') : 0,
              ('Rock','Paper') : 0,
              ('Scissors','Rock') : 0,         
              ('Paper','Rock') : 1,
              ('Rock','Scissors') : 1,
              ('Scissors','Paper') : 1,
              ('Paper','Paper') : 2,
              ('Rock','Rock') : 2,
              ('Scissors','Scissors') : 2  
              }

    return results[(left,right)]

ROUNDS = int(input("Enter number of ROUNDS: "))
seedNum2 = int(input("Enter number of seed: "))

random.seed(seedNum2)

for eachround in range(ROUNDS):
    right = choiceB[random.randint(0,2)]
    left = choiceB[random.randint(0,2)]
    if compare(left,right) == 2:
        push += 1
    if compare(left,right) == 1:
        leftwin += 1
    if compare(left,right) == 0:
        rightwin += 1

pushPercent = (push / ROUNDS) * 100
leftPercent = (leftwin / ROUNDS) * 100
rightPercent = (rightwin / ROUNDS) * 100

print()
print("Simulating rock, paper, scissors (seed={})".format(seedNum2))
print("Trials: {}, Left win %: {}, Right win %: {}, Push %: {} \n".format(ROUNDS,leftPercent,rightPercent,pushPercent))
        

