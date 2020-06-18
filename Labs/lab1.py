#Student: Ngoc Pham
#Student number: 7891063

#Exercise 3: extract last and second last digit of a num
num = 35607 #enter integer number
num_str = str(num) #convert int to string
numLength = len(num_str) #count length of number
txt1 = "Entered number is {}"
print(txt1.format(num))
txt2 = "Last digit of the number: {}"
print(txt2.format(num_str[numLength-1])) #output last digit of the number
txt3 = "Second last digit of the number: {}"
print(txt3.format(num_str[numLength-2])) #output second last digit of the number

#Exercise 4: extract first digit of a num, using math.log10
import math
num_log = math.log10(num) #perform log10 of num
num_return = 10**num_log #return num to initial value
num_return_str = str(num_return) #string the num
txt4 = "First digit of the number: {}"
print(txt4.format(num_return_str[0])) #extract first digit of num

#Exercise 5: display 3 decimal place number
dec_place = 3
txt5 = "This is the the number in {}-decimal-place: {:.{}f}"
print(txt5.format(dec_place,num,dec_place))


#AreaOfTriangle:
height = 8
base = 1/3
area = (height * base) / 2
txt6 = "Area in 3-decimal-place: {:.3f}"
print(txt6.format(area))