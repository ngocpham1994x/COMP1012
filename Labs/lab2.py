# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 13:20:09 2020

@author: Ngoc Pham (7891063)

"""


#Exercise 1:Getting input
question0=input('What is your first name? > ')
question1=input('What is your last name? > ')
question2=input("What is your favourite colour? > ")
print("Your name is {firstName} {lastName}, and your favourite colour is {favColour}".format(firstName=question0,lastName=question1,favColour=question2))


#Exercise 2: Getting numbers
getNum1=input('Please enter number 1: > ')
getNum2=input('Please enter number 2: > ')
getNum3=input('Please enter number 3: > ')
getNum4=input('Please enter number 4: > ')
sum=float(getNum1)+float(getNum2)+float(getNum3)+float(getNum4)
sumInt=int(sum)
average=sum/4
print("Sum: {} ".format(sumInt))
print("Average: {:.4f}".format(average))


#Exercise 3: BMI Calculation
question3=input("What is your weight in kgs? > ")
weight=float(question3)
question4=input("What is your height in cm? > ")
heightC=float(question4)
height=round((heightC*(10**-2)),2)
bmi=weight/(height*height)
print("Your BMI is: {:.2f}".format(bmi))

#Exercise 4: Jump height calculator
a=-9.8
vFinal=0
question5=input("How fast were you when you left the ground,in m/s? > ")
vInit=float(question5)
high1=(vFinal**2-vInit**2)/(2*a)
print("Using ** operator, You have jumped {}m in that jump".format(high1))

import math
high2=(math.pow(vFinal,2)-math.pow(vInit,2))/(2*a)
print("Using math.pow(), You have jumped {}m in that jump".format(high2))


#Bonus Question: Pokémon Damage Calculator
import math
level=int(input("What level is the attacking Pokemon? > "))
attack=int(input("What is the attacking Pokemon's ATK stat? > "))
defense=int(input("What is the defending Pokemon's DEF stat? > "))
basePower=int(input("What is the base power of the attack? > "))
baseDamage=math.floor(2+((((2*level)/5+2)*basePower*attack)/defense)/50)
print("The base damage of the attack (before modifiers) is {}".format(baseDamage))