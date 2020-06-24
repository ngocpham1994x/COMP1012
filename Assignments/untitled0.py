# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 23:10:39 2020

@author: Ngoc Pham
"""


doc=open("reducedweather1.csv")
x = doc.read()
for line in x:
    print(line)
