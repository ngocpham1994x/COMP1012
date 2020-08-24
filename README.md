# :school: COMP1012 Computer Programming for Scientists and Engineers
The course was taught in Python language and it used IDE Spyder Python 3.8.3 64-bit from Anaconda3.

This course was taken in Summer 2020.

The course repo contains my own lines of code for laboratory and assginments.

## Timeline: :date:
- Week 1:
  - Introduction and familiarize with IDE
  - Terminologies
- Week 2: 
  - String, slicing string, iterate through and access string elements
  - Format output
- Week 3:
  - File handling: open/close file, read file ( `open()`, `.read`, `.readline`, `.readlines` )
  - `split()` command. `strip()` command.
  - `for...in...` loop
- Week 4:
  - List, iterate through and access list elements
  - `for items in list:` vs `for x in range(len(list)):`
  - `range()` function
  - Series calculation: Fibonaci, Factorial, Sum of odd/even numbers
  - Prime number checking
  - Nested loop
  - Relational & Logical Operators
  - Short circuit evaluation in Python
  - String comparison
  - `If...`, `If...else...`, `If...elif...elif...else...` statements
  - `while...`loop
- Week 5:
  - Dictionary & Tuple
  - Iterate through and access sequence elements
  - `for key in dict-name.keys():`
  - `for value in dict-name.values():`
  - `for key,value in dict-name.items():`
  - Functions: variables, return statement, calling functions & assign variables/multiple variables
  - Modules: **calling module, calling functions in the module** after creating to run an instance
- Week 6: Functions
  - Arguments in function. Pass by value & Pass by reference
  - Default values for parameters
  - Local variables. Global variables. Scope
- Week 7: Random number
  - Commenting in function (docstring)
  - Passing a function to a function
  - Random number: generate random numbers using random library, shuffle random numbers, select (choice) a random element from a list
  - Seeding a random number
  - Simulation using Random number: Monte Carlo simulation, Drawing balls from urn, Rolling dice, Estimate π
- Week 8: Array & Vectorization
  - Array: create arrays (1D, 2D, arrays with ones, arrays with zeros, etc) 
  - numpy arrays: create arrays using numpy library (random numbers using numpy array)
  - numpy vector operations: math operators, comparison operators, scalars, numpy math functions, numpy logical operations
- Week 9: Multi-dimensional arrays
  - Array: create multi-dimensional array using nested list or tuple, numpy random numbers with size, etc
  - `array.size` and `array.shape`
  - `numpy.shape()` and `numpy.len()`
  - accessing elements in multi-dimensional array
  - sum all elements in row or column order, accessing odd or even indices in array
  - pixel image modifying: greyscale, blackout circle, blur

- Week 10: Object
  - Object and `class`. Functions in class
  - `self` variable in class and in functions
  - Accessing variables and functions in class
  - `__init__` and `__str__`
  - create multiple objects from same class
  - **calling class, calling functions in class** after creating to run an instance
  - Pass by reference in object



## Python Cheatsheet::scroll:

| commands | functionality |
| ---| --- |
| **Ranges** <br />`range(x)` <br />`range(x, y)` <br />`range(x, y, z)` |<br /># range from 0 up to and not including x <br /># range from x up to and not including y <br /># range from x up to and not including y, counting up by z |
| **Lists** <br />`my_list = list(collection)`<br /><br />`my_list.append(d)`<br />`my_list.sort()`<br />`sorted(my_list)`<br /><br />`max(my_list)`<br />`min(my_list)`<br />`sum(my_list)`<br /><br />`my_list.pop(el)`<br />  `my_list.remove(i)`<br />`len(my_list)`<br />`del my_list[0]` <br /><br />`my_list[start_ind:stop_ind:step]`		|		<br /># convert sequence to list<br /><br /># Append data d to the list<br /> # sort my_list (ascending)<br /> # sort my_list (ascending)<br /><br /># the maximum value in the list<br /> # the minimum value in the list<br /> # sum all items of the current list<br /><br /># Remove and return an element from location el<br /># find and remove the first instance of i<br /># length of a list<br /># delete element at position 0 of the current list<br /><br /># slice a list [start,end)<br />|
| **Dicts** <br />`d = dict()`<br />`d.keys()`<br />`d.values()`<br />`d.items()`<br />`d.clear()`<br /> `d['key'] = v`<br /><br />`key in d`<br />`len(d)`		|		<br /><br /># get a list-like object of all the keys<br /># get a list-like object of all the values <br /># get a list-like object of all the key-value pairs <br /># delete all key-value pairs <br /># set a new key, or overwrite an existing key in the dict<br /><br /># returns TRUE/FALSE to check if key is in dict<br /># length of dictionary<br />|
|**Tuples** <br />`t = tuple([1,5,11])`<br />`t = tuple("hi")`<br /><br />`item in t`<br />`len(td)`		|		<br /># (1,5,11)<br /># ("h","i")<br /><br /># returns TRUE/FALSE to check if item is in tuple<br /># length of tuple|
|**Sets** <br />`s = set()`<br /> `s = set(iterable)`<br /> `s.add(item)`<br /> `s.intersection(s2)`<br />  `s.difference(s2)`<br /> `s.union(s2)`<br /> 		|		<br /><br /><br /># add an item to the set <br /># return a set intersection with set<br /># return a set difference <br /># return a set union<br />|
|**Strings** <br />`my_str = "My mom loves CAKE."`<br /><br /><br />`my_str.upper()` <br />`my_str.lower()`<br />`my_str.strip()`<br /> `my_str.split()`<br />`my_str.split("-")` <br /> `my_str.index('z')`<br />   `my_str.count("m")`  <br />`my_str.replace(x, y)` <br />`my_str.format(args)`<br />`my_str.capitalize()` <br />`my_str.isnumeric()` <br />`my_str.isdecimal()` <br />`my_str.find("s")`<br /><br />`my_str[start_ind:end_ind:step]`<br />		|		<br />All string functions are non-destructive. String functions do not modify the string, but return a transformed copy.<br /><br /># upper-case version <br /># lower-case version <br /># remove whitespace from beginning and end of string <br /># split the string on the space character<br /># split the string on the - character<br /># find first location of 'z', or error if not in string<br /># counts how many of a character is in the string<br /># replace all copies of x with y <br /># format the string (with {}) <br /># upper-case first character, lower-case everything else <br /># True if all characters are numeric (0 to 9) <br /># True if numeric, but allows one . character <br /># return the first index of passed string, or -1 if it is not in my_str<br /><br /># slice a string [start, end)<br />|
|**Format codes**<br />`7.3f`<br /> <br />`-------`<br /> <br /><br /><br /><br /><br /><br />`{data-index:formatcode}.format()`<br /><br />`{0:3d}.format(16)`<br />`{0:<4d}.format(16)`<br /><br />`{0:9.2e}.format(-6.123)`<br />`{0:<12.4e}.format(0.32)`<br /><br />`{0:7.2f}.format(-6.123)`<br />`{0:<8.4f}.format(0.32)`<br /><br />`{0:5s}.format("Hello")`<br />		|		<br /># floating point (type), 3 decimal places (precision)<br /><br /># display up to 7 characters (width) <br /><br />	• type may be any of d (integer), e (floating exponent), f (floating point), or s (string) <br />	• width may be 0 or omitted entirely <br />	• precision may be 0 or omitted entirely<br /><br /><br /><br /># ' 16'<br /># '16  '<br /><br /># '-6.12e+00'<br /># '3.2000e-01  '<br /><br /># '  -6.12'<br /># '0.3200  '<br /><br /># 'Hello'<br />|
|**File handling** <br />`infile = open("aFile.txt", 'r', encoding = 'utf8')`<br /><br />`infile.read()` <br />`infile.readline()`<br />`infile.readlines()`<br />`infile.close()`<br />`infile.write("something")`<br /><br />`input("Enter a num: ")`<br />`int(str)`<br />`float(str)`<br />`str(val)`<br />		|		<br /># open a file <br /><br /><br /># read an entire file <br /># read a single line from the file<br /># read an entire file into a list of lines <br /># close the file for line in f: # read a file line by line<br /># write data to a file<br /><br /># prompt always returns a string<br /># convert string to integer<br /># convert string to floating point<br /># convert any value to string<br /> |

| commands | functionality |
| ---| --- |
|**for-loops**<br />`for eachline in infile:`<br />&nbsp;&nbsp;`parts = eachline.strip().split(",")`<br /><br />`for eachline in infile:`<br />&nbsp;&nbsp;`week, mx, mean, mn = eachline.strip().split(",")`<br /><br /><br />`for eachitem in aList:`<br />&nbsp;&nbsp; `print(eachitem)`<br /><br />`for eachitem in range(len(aList)):`<br />&nbsp;&nbsp;`print(aList[eachitem])`<br /><br />`for eachitem in range(start,stop,step):`<br /><br /><br />`for eachchar in aString:`<br />&nbsp;&nbsp;`print(eachchar)`<br /><br /><br />`for key in dict-name.keys():`<br />`for values in dict-name.values():`<br />`for key,value in dict-name.items():`<br /><br /><br />`for eachitem in tuple-name:`<br />		|		<br /># iterate line-by-line of a file<br /># return a list of strings, remember to convert string to integer<br /><br /><br /># assign each item of a list to a var<br /><br /><br /><br /># iterate item-by-item of a list<br /># eachitem is element of the list<br /><br /># iterate item-by-item of a list using range of length<br /># eachitem is an integer<br /><br /># iterate through a range of numbers. Example: (0,10,2) = 0,2,4,6,8<br /><br /><br /># iterate char-by-char of a string<br /># eachchar is a single character of the string<br /><br /><br /># iterate keys in a dictionary<br /># iterate values in a dictionary<br /># iterate pairs of key-value in a dictionary<br /><br /><br /># iterate items in a tuple |
|**if-statements**<br />`if x == TRUE:`<br /><br />`if...:`<br />`else...:`<br /><br />`if...:`<br />`elif...:`<br />`elif...:`<br />`else...:`	<br />	|		<br /># if-statement can stay alone, doesn't need "else" accompanied<br /><br /><br /># "else" doesn't have to have condition with it<br /><br /><br /># can have many "elif"<br /><br /># last "else" condition is for return output in case none of conditions are TRUE|
|**while-statement**<br />`while x == TRUE:...`<br /><br />`while...:`<br />&nbsp;&nbsp;`if...:`<br />&nbsp;&nbsp;&nbsp;`break`<br /><br />`while...:`<br />&nbsp;&nbsp;`if...:`<br />&nbsp;&nbsp;&nbsp;`continue`<br />		|		<br /># need to know the stop condition<br /><br /><br /><br /># break out of while (parents loop) if needed<br /><br /><br /><br /># continue if needed|

| commands | functionality |
| --- | --- |
|**Function**<br />`def func-name(xx,yy):`<br />&nbsp;&nbsp;    `ss = xx + yy`<br />&nbsp;&nbsp;    `dd = xx - yy`<br />&nbsp;&nbsp;    `return ss,dd`<br /><br />`aa = 10`<br />`bb = 20`<br />`c,d = func-name(aa,bb)`<br />`print(c)`<br /><br />`e = func-name(20,30)`<br /><br /><br />`module-name.var-name`<br />`module-name.function-name`<br /><br /><br />`def myFunc(x,y,z):`<br />&nbsp;&nbsp;	`x = 10`<br />&nbsp;&nbsp;	`y['Bob'] = 10`<br />&nbsp;&nbsp;	`z[0] = 0`<br />&nbsp;&nbsp;	`return`<br />`a = 50`<br />`b = {'Adam':10, 'Bob':15}`<br />`c = [1,3,5]` <br /> `myFunc(a,b,c)`<br />`print(a)` <br />`print(b)`<br />  `print(c)`<br /> <br /><br />`def greeting(msg="Good morning!", name):`<br />&nbsp;&nbsp;	`print("Hello" + name + "," + msg)`<br />`greeting(name="Irene")`<br /><br /><br />`def line(f,a,b):`<br />&nbsp;&nbsp;    `"""`<br />&nbsp;&nbsp;    `This function computes the line y=mx+b`<br />&nbsp;&nbsp;    `passing through (a,f(a)) and (b,f(b))`<br />&nbsp;&nbsp;    `@param f - the function f`<br />&nbsp;&nbsp;    `@param a,b - distinct floats`<br />&nbsp;&nbsp;    `@return the values m,b for the line y=mx+b`<br />&nbsp;&nbsp;    `"""`<br /><br />&nbsp;&nbsp;    `m = (f(b)-f(a))/(b-a) #slope`<br />&nbsp;&nbsp;    `b = f(0)-m*a          #b`<br />&nbsp;&nbsp;    `return m,b            #y=mx+b`<br /><br />`m,b = line(math.exp,0,2) #try other functions here`<br />`print('The line is: {:.3f}x+{:.3f}'.format(m,b))`<br />		|# define function<br /><br /><br /># return statement<br /><br /># pass by value: primitive datatype (int, float, string)<br /># global var<br /># numbers of assigned var equal numbers of return var<br /><br /><br /># return multiple var to single var. Single var is a tuple<br /><br /><br /># calling variable in a module<br /># calling function in a module<br /><br /><br /><br /># local var<br /><br /><br /><br /># passed by value<br /># passed by reference<br /># passed by reference<br /><br /># 50<br /># {'Adam': 10, 'Bob': 10}<br /># [0,3,5]<br /><br /><br /># default values for parameter<br /># "Hello Irene, Good morning!"<br /># default values for parameter<br /><br /><br /># pass a function to a function<br />**# remember to call out function for running an instance**<br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br />	|
|**Object & Class**<br />	`self.var`<br />	`self.func-name`<br /><br />		`obj-name.var`<br />	`obj-name.func-name`<br /><br />	<br />`class myClass:`  <br />  &nbsp;&nbsp;    `def __init__(self,x, y, z):`<br />&nbsp;&nbsp;&nbsp;        `self.a = x`<br />&nbsp;&nbsp;&nbsp;        `self.b = y`<br />&nbsp;&nbsp;&nbsp;        `self.calculate(z)`<br /><br />&nbsp;&nbsp;    `def calculate(self, c):`<br />&nbsp;&nbsp;&nbsp;        `total = self.a + self.b` <br />  &nbsp;&nbsp;&nbsp;        `self.res = total % c` <br />     <br />&nbsp;&nbsp;    `def __str__(self):`   <br />                &nbsp;&nbsp;&nbsp;	      `return 'the result is{}'.format(self.res)`<br /><br />        <br />`obj1 = myClass(10, 20, 7))`<br />`obj2 = obj1`<br />`obj2.a = 20`<br />`obj1.calculate()`		|		<br /># accessing var within current defined class<br /># accessing function within current defined class<br /><br /># accessing var of an object (outside class)<br /># accessing function of an object (outside class)<br /><br /><br /># initialized constructor<br /># first parameter is always referenced to itself (class) as  an instance<br /><br /><br /><br /><br /># total = 30<br /># 30/7 = 4.2857 remainder = 2<br /><br /><br /># __str__ function is declared<br /><br /><br /># best is to do: obj2 = myClass(10,20,8)<br /># obj1 variable a is also changed<br /># object is "passed by reference"<br /># calling function from an object	|
|**Matplotlib**<br />`import matplotlib.pyplot as plt `<br />	`plt.scatter(x, y, c) `<br />`plt.line(x, y, c) `<br />	`plt.plot(x, y, c)  `<br /><br />	# plot a circle <br />	`circle = plt.Circle( (0,0), 3) `<br />	`plt.gca().add_patch(circle) `<br />	`rect = plt.Rectangle( (0,0), 1, 2) `<br />	`plt.gca().add_patch(rect) `		|		<br /><br /># plot a scatter plot of x vs y, coloured with c <br /># plot a line plot of x vs y, coloured with c <br /># plot a line (or scatter) of x vs y, coloured with c<br /><br /><br /># Circle at (0,0), with radius 3 <br /># Plot circle on current plot <br /># rectangle at (0, 0), width 1, height 2<br /># plot rectangle on current plot|
|**Pandas**<br />`import pandas as pd` <br /><br />`pd.DataFrame({"column1":data, "column2":data2})`<br />`pd.read_csv("filename.csv")` <br />`pd.read_excel("filename.xls", sheet="sheetname")`	|	|

| commands | functionality |
| --- | --- |
|**Python Random** <br />`import random`<br /><br />`random.seed(n) `<br />`random.random() `<br />`random.randint(x, y)`<br />`random.randrange(x, y, n)  `<br /><br /><br /><br />`random.choice(list_of_options) `<br />`random.shuffle(list_of_options)`<br /><br />		|		<br /><br /><br /># Seed the random number generator <br /># A single floating random number [0,1) <br /># A single integer random number [x,y]. Both bounds inclusive<br /># A single number between a series x, x+n, x+2n,... b-n. Bound b exclusive<br /><br /># Choose randomly from the given list<br /># shuffle the given list|
|**Numpy**<br />`import numpy as np`<br />`np.array([1,2,3])`<br />`np.array([[1,2,3],[4,5,6]])`<br />`np.array([(1,2,3),(4,5,6)])`<br /><br />`np.arange(y) `<br />`np.arange(x, y, z)` <br /> `np.linspace(x, y, z) ` <br /><br /><br />`np.random.seed(#)` <br /><br />	`np.random.random(n)`<br /> `np.random.random(size=n) `<br /><br />	`np.random.random((n, m)) `<br />`np.random.random(size=(n,m)) `<br /><br />	`np.random.randint(x,y,n) `<br />`np.random.randint(x,y,size=n) `<br /><br />	`np.random.randint(x,y,(n,m)) `<br />`np.random.randint(x,y,size=(n,m)) `<br /><br />	`np.random.choice(list_of_options, n) `<br />`np.random.choice(list_of_options, size=n)  `<br /><br /><br />`np.random.shuffle( array-name )`<br /><br />	`np.zeros(n)  `<br />`np.zeros( (n, m) ) `<br /><br />`np.ones(n)  `<br />`np.ones( (n, m) )  `<br />	`np.full( (n, m), x)`	|		# always need to know size or shape of array when using numpy<br /><br /># Create np array with values from list <br /># Create 2D np array with values from nested list<br /># Create 2D np array with values from nested list from tuple<br /><br /># Count to y, y exclusive<br /># Count from x to y by z, y exclusive<br /># Return z evenly spaced numbers over a specified interval x-y, y inclusive<br /># Seed numpy's random number generator <br /><br /># Create array size n of random data with data [0, 1) <br /># Create array size n of random data with data [0, 1)<br /><br /># Create 2D array size n by m of random data with data [0, 1)<br /># Create 2D array size n by m of random data with data [0, 1)<br /><br /># Create a random array from x to y (y exclusive) of size n<br /># Create a random array from x to y (y exclusive) of size n<br /><br /># Create a random 2D array from x to y (y exclusive) of size n by m <br /># Create a random 2D array from x to y (y exclusive) of size n by m<br /> <br /># Create an array size n filled with random data, Chosen from the passed list<br /># Create an array size n filled with random data, Chosen from the passed list<br /><br /># shuffle n-dimension array<br /><br /># Create an array of n zeros<br /># Create a 2D array of zeros, size n by m <br /><br /># Create an array of n ones<br /># Create an array of n ones, size n by m<br /># Create an array of value x, size n by m	|
|**Numpy** <br />`np.size(array-name)`<br />`arr-name.size`<br /><br />`d = np.shape(array-name)`<br />`arr-name.shape`<br /><br />`len(arr-name)`<br /><br />	`arr[0:n+1,0:n+1]`<br /><br /><br /><br />		|		<br /># Total number of items in array<br /><br /><br /># tuple representation of array shape<br /># d[0]: first dimension (rows), d[1]: 2nd dimension (columns)<br /><br /># single integer representation of first dimension (row)<br /><br /># accessing items in a multi-dimensional array. Higher bound exclusive<br /># colons used for specifying range<br /># comma used for specifying dimensions	|
|**Numpy**<br />	`import numpy as np`<br />`import random`<br /><br />	`a = np.random.randint(0, 10, 10)`<br />`a.sum() `<br />`a.prod()  `<br />`a.mean()  `<br />`a.std()  `<br />`a.abs() `<br /><br />`np.sum(arr, axis = 1)`<br />`np.sum(arr, axis = 0)`<br /><br />`a1 = np.array([0, 1, 2]) `<br /> `a2 = np.array([1, 2, 3]) ` <br /> `rint(np.logical_and(a1, a2))`<br /><br />		|**# no import math in array, because using numpy functions to perform math**<br /><br /><br /><br /># get the sum of the data in the array <br /># get the product of the data in the array<br /># get the mean of the data in the array<br /># get the standard deviation of the data in the array<br /># return an array with the absolute value of the data in a<br /><br /># row sum<br /># column sum<br /><br /># 0 is an empty list/dict/string (represents 0), 1 & 2 are not (represents 1)<br /># all 1, 2, 3 are not empty list/dict./string (represents 1)<br /># [False True True]	|
|**Numpy operations**<br />Math operators: `+, –, *, /, //, %, ** `<br /> Comparison operators:`<, <=, ==, >=, >, != `<br />Also work between arrays and scalars <br /><br />Math functions: Not apply math.sin(arr_name) on array<br />		○`np.sin, np.cos, np.tan`: trignometric functions. <br />		○`np.absolute, np.fabs, np.floor, np.ceil`: rounding functions<br />		○`np.reciprocal, np.floor_divide, np.mod` or `np.remainder` <br />○`np.add, np.subtract, np.multiply`: algebraic functions<br />		○`np.sqrt, np.square, np.power`<br />		○`np.log, np.exp`: exponent (e^x) and logarithm (ln) functions<br />		○`np.maximum, np.minimum, np.sum, np.mean, np.std `<br /><br /> Numpy logical operations:<br />		○`np.logical_not()`<br />		○`np.logical_and()`<br />		○`np.logical_or()`<br />		|		# using symbols to perform math<br /># returns TRUE/FALSE array<br /><br /><br /># using numpy functions to perform math<br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /># return TRUE/FALSE array<br /><br /><br />	|
