#Student: Ngoc Pham
#Student ID: 7891063


#This function returns True if and only if s contains at least one numeric digit
def hasNumbers(s):
    return any(ch.isdigit() for ch in s)

#This function returns True if and only if s contains at least one alphabet character
def hasAlpha(s):
    return any(ch.isalpha() for ch in s)

# text = '1234567i'
# if hasAlpha(text):
#     print('true')
# else:
#     print('false')


#-----------------------------
#Question 1: Password checking
print("**Question 1: ")
print()
infile = open('passwords.txt')
data = {}
text1 = 'less than 8 characters'
text2 = 'no digit'
text3 = 'no alphabet character'
lineNum = 1
count = 0

for eachline in infile:
    email, password = eachline.strip().split(',')
    data[email] = password
    
for key,value in data.items():
    if len(value) < 8 and not hasNumbers(value):
        print("{}) {},{}: {}, {}".format(lineNum, key, value , text1, text2))
        count += 1
    elif len(value) < 8 and not hasAlpha(value):
        print("{}) {},{}: {}, {}".format(lineNum, key, value , text1, text3))
        count += 1
    elif len(value) < 8:
        print("{}) {},{}: {}".format(lineNum, key, value , text1))
        count += 1
    elif not hasNumbers(value):
        print("{}) {},{}: {}".format(lineNum, key, value , text2))
        count += 1
    elif not hasAlpha(value):
        print("{}) {},{}: {}".format(lineNum, key, value , text3))
        count += 1
    lineNum += 1

print()
print('There were {} emails with insecure passwords.'.format(count))
print()

infile.close()


#--------------------------      
#Question 2: Deduction Game
print("**Question 2: ")
import random
lowerRange = int(input("Enter lower range of randomization: "))
upperRange = int(input("Enter upper range of randomization: "))
myRandomNum = random.randint(lowerRange,upperRange)
print()
print("Hint: My random number is {}.".format(myRandomNum))
found = False
count = 0


while found == False:
    Q = input("I've picked a number between {} and {}, can you guess it? ".format(lowerRange,upperRange))
    if Q.isnumeric() and int(Q) <= upperRange:
        num = int(Q)
        count += 1
        if num < myRandomNum:
            print("Nope, it's not {}".format(num))
            print("Your guess is too low")
        elif num > myRandomNum:
            print("Nope, it's not {}".format(Q))
            print("Your guess is too high")
        elif num == myRandomNum:
            print("You got it!")
            print("It took you {} guesses.".format(count))
            found = True
    elif (Q.isnumeric() == False) or (int(Q) > upperRange):
        print("Oops, you have entered invalid number! Guess again.")
        count += 1

print()
            
#-----------------------------------------
#Optional: New and Improved Deduction Game
print("**Optional Question: ")
import random
lowerRange = int(input("Enter lower range of randomization: "))
upperRange = int(input("Enter upper range of randomization: "))
myRandomNum = random.randint(lowerRange,upperRange)
print()
print("Hint: My random number is {}.".format(myRandomNum))
found = False
count = 0

tempUpper = upperRange
tempLower = lowerRange

while found == False:
    Q = input("I've picked a number. Range: {} < _ < {}. Your guess: ".format(tempLower,tempUpper))
    if Q.isnumeric() and int(Q) <= upperRange:
        num = int(Q)
        count += 1
        if num < myRandomNum:
            print("Nope, it's not {}".format(num))
            print("Your guess is too low")
            if num > tempLower:
                tempLower = num
        elif num > myRandomNum:
            print("Nope, it's not {}".format(Q))
            print("Your guess is too high")
            if num < tempUpper: 
                tempUpper = num
        elif num == myRandomNum:
            print("You got it!")
            print("It took you {} guesses.".format(count))
            found = True
    elif (Q.isnumeric() == False) or (int(Q) > upperRange):
        print("Oops, you have entered invalid number! It contains invalid characters or out of pre-dertermined range. Guess again.")
        count += 1