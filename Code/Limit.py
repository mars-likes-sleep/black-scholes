# -*- coding: utf-8 -*-
"""
Created on Sun May 10 21:33:51 2020

@author: marsh
"""
from scipy import *
from math import log

global x
x=Symbol("x")

d1_num = log(250/260) + (.04 - .02 + 0.5 * sqrt(x)) * 0.5
d1_den = x * sqrt(0.5)
f = d1_num/d1_den
print("As sigma approaches 0, d1 approaches " + str(limit(f,x,0)))
print("As sigma approaches oo, d1 approaches " + str(limit(f,x,oo)))

d2_num = log(250/260) + (.04 - .02 - 0.5 * sqrt(x)) * 0.5
d2_den = x * sqrt(0.5)
f = d2_num / d2_den
print("As sigma approaches 0, d2 approaches " + str(limit(f,x,0)))
print("As sigma approaches oo, d2 approaches " + str(limit(f,x,oo)))