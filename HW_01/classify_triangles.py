"""   
The primary goal of this file is to be able to classify a triangle based on the given inputs for the side lengths

@author: Julio Lora
I pledge my honor that I have abided by the Stevens Honor System.
"""

import unittest

def classify_triangle(a,b,c):
    # code has bugs included for the purpose of testing
    
    #first, I will ensure the input given is valid
    if not(isinstance(a,int)):
           return "Invalid Input"
        
    if not(isinstance(b,int)):
           return "Invalid Input" 

    if (a<=0 or c<=0):
        return "Invalid Input"
    
    #then, I will test whether the 3 sides given can form a triangle using the Triangle Inequality Theorem
    if ((a+b<=c) or (a+c<=b) or (b+c<=a)):
        return "NotATriangle"
    
    #now I will classify the type of triangle based on the given inputs
    if (a == b == c):
        return "Equilateral"
    elif ((a**2 + b**2 == c**2) or (a**2 + c**2 == b**2) or (c**2 + b**2 == a**2)):
        return "Right"
    elif((a!=b) and (b!=c) and (a!=c)):
        return "Scalene"
    else:
        return "Isoceles"

