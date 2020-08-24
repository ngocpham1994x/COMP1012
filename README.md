# :school: COMP1012 Computer Programming for Scientists and Engineers
The course was taught in Python language and it used IDE Spyder Python 3.8.3 64-bit from Anaconda3.

This course was taken in Summer 2020.

The course repo contains my own lines of code for laboratory and assginments.

## Timeline: 
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



## Python Cheatsheet:

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

