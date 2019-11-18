# -*- coding: utf-8 -*-
"""
Created on Tue May 14 17:24:37 2019

@author: Mingming


Leetcode question 12: Interger to Roman

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

For example, two is written as II in Roman numeral, just two one's added together. 
Twelve is written as, XII, which is simply X + II. The number twenty seven is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. 
However, the numeral for four is not IIII. Instead, the number four is written as IV. 
Because the one is before the five we subtract it making four. The same principle applies to the number nine, 
which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given an integer, convert it to a roman numeral. Input is guaranteed to be within the range from 1 to 3999.

"""

class Solution:
    def intToRoman(self, num: int) -> str:
        
        # first define the dictionary for all the possible stand alone Roman numbers
        RomanDict = {'I': 1, 'IV': 4 , 'V': 5, 'IX': 9,'X':10, 
                     'XL':40, 'L': 50, 'XC': 90,'C': 100, 'CD': 400,
                     'D': 500, 'CM': 900, 'M': 1000 }
    
        keys  = list(RomanDict.keys())     # get all the keys from the dictionary, the Roman strings, and turn them into python list. 
        values= list(RomanDict.values())   # get all the values from the dictionary, from small to big, and turn them into python list.        
        all_smaller = [val for loc, val in enumerate(values) if val<=num] # a list of numbers that the input number may need to devide
        
        residual = num
        my_roman_str = '' # initialize the space to keep the output all the roman string.
        for n in range(0, len(all_smaller)):
            # check all the number that is smaller than the input number
            current_single_roma = all_smaller[-1-n]       # starting from the last number to the first number
            
            # for the current roma number, if the residual is bigger or equal than it, 
            # then the residual it can be expressed with current roman number
            if residual>=current_single_roma:                
                times    = residual//current_single_roma  # how many singal_roma number does the current residual number has
                residual = residual%current_single_roma   # update the residual number              
                
                current_roman_string = keys[values.index(current_single_roma)]  # return the current roman of a given element in the list
                for n in range(times):    # what is the current roman string, repeat for the number of required times
                   my_roman_str = my_roman_str + current_roman_string 
   
        return(my_roman_str)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        