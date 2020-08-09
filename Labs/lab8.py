# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 07:59:40 2020

@author: Ngoc Pham (7891063)
"""

#--------------------------------------------------------
#Question 1 (Required): Estimating the volume of a Sphere

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
        

