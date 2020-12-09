# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 12:38:24 2020

@author: Mingming

Leetcode 167:

Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2.

Note:

Your returned answers (both index1 and index2) are not zero-based.
You may assume that each input would have exactly one solution and you may not use the same element twice.
 

"""


#%% for loop very slow,

class Solution:
    #def twoSum(self, numbers: List[int], target: int) -> List[int]:
    def twoSum(self, numbers, target):   
        output = []
        
        for loc, val in enumerate(numbers):
            
            complement = target-val   # get the complement of the investigated value in terms of target value
            other_list = numbers.copy()
            other_list.remove(val) # list.remove will remove the first element that is the same with the given value.
            
            if complement in other_list:
                output.append(loc+1)         # answers require to return non-zero index, starting from 1, so add 1 here
                new_loc = other_list.index(complement)            
                output.append(new_loc+1+1) # add 1 to compensate the list index because remove of the selected value, add another 1 to conduct non-zero index
                break
        
   
        return output
        
        
        
#%%  hashable table, in python is dictionary   

class Solution:
    #def twoSum(self, numbers: List[int], target: int) -> List[int]:
    def twoSum(self, numbers, target):      
        
        numMap = {}
        
        for i, val in enumerate(numbers):
            num = target - val   # the complement value
            if num in numMap.keys():     # design a hashable dictionary, put the number as the key of the dictionary.
                return [numMap.get(num)+1, i+1]   # numMap.get(num) get the value(index) of a given key(number)
                                                  # add 1 to meet the non-zero index requirement
    
            numMap[val] = i       # each time, put the number as a key in the hashable data structure (dictionary in python)
                                    # key-value pair is number-index pair
            
            
            
        
#%%


numbers = [2,7,11,15]
target = 9

numbers = [2,3,4]
target = 6


numbers = [-1,0]
target = -1
 
results = Solution()
output = results.twoSum(numbers, target)      
print(output)