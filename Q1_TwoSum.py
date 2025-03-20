# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 15:11:31 2020

@author: Mingming

Leetcode Q1 two sum

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]

Constraints:

2 <= nums.length <= 103
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
"""

#%% solution 1:  3 for loops speed and is very slow
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
    #def twoSum(self, nums, target):
        
        '''
        The idea is that there are two numbers need to sum together to form the target, 
        As long as we can find the numbers that is less than the half of the target, then we can look for if the the difference between the number we find
        and the target, then this is the solution. 
        '''
        
        output_list = []
                
        half_search_num      = target//2
        half_search_residual = target%2

        
        # if the target is a even number, and the list contain two halves of the even number, then just find these two halves location
        exact_half_number_loc = [loc for loc, val in enumerate(nums) if val==half_search_num]        
        if half_search_residual == 0 and len(exact_half_number_loc)>=2:
            output_list = exact_half_number_loc
               
        
        # other condition
        else:
    
            smaller_than_half_num = [val for loc, val in enumerate(nums) if val<=half_search_num]
  
            # 2. for any given smaller_than_half_num, if the difference to target is in the original nums input list,
            # then this is the solution
            for value in smaller_than_half_num:
                
                if (target-value) in nums and (target-value)!=half_search_num:    # exclude the scenario where the target is even number, and there is half of the target in the nums
                                                       # the program can come to here, mean before it already investigate that the program has no two exact halves
                    
                    output_list.append(nums.index(value))         # add the first half index in the original input list
                    output_list.append(nums.index(target-value))  # add the another half of the target index into the final output list
                    output_list.sort()
              
        return output_list
        
#%% solution 2: two for loops, faster, but still slow

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
    #def twoSum(self, nums, target):
        
        '''
        The idea is that there are two numbers need to sum together to form the target, 
        As long as we can find the numbers that is less than the half of the target, then we can look for if the the difference between the number we find
        and the target, then this is the solution. 
        '''
        
        output_list = []
        exact_half_number_loc = []
        smaller_than_half_num = []
                
        half_search_num      = target//2
        half_search_residual = target%2

        
        # if the target is a even number, and the list contain two halves of the even number, then just find these two halves location

        for loc, val in enumerate(nums):
            if val==half_search_num: exact_half_number_loc.append(loc)
            if val<=half_search_num: smaller_than_half_num.append(val)
                    
        # where the input target is even number, there is two halves in the list
        if half_search_residual == 0 and len(exact_half_number_loc)==2:
            output_list = exact_half_number_loc           
        
        # other condition
        else:

            # 2. for any given smaller_than_half_num, if the difference to target is in the original nums input list,
            # then this is the solution
            for value in smaller_than_half_num:
                
                if (target-value) in nums and (target-value)!=half_search_num:    # exclude the scenario where the target is even number, and there is half of the target in the nums
                                                       # the program can come to here, mean before it already investigate that the program has no two exact halves
                    
                    output_list.append(nums.index(value))         # add the first half index in the original input list
                    output_list.append(nums.index(target-value))  # add the another half of the target index into the final output list
                    output_list.sort()
              
        return output_list
        
#%% solution 3, use the target-"investigated value", and conduct search within 1 for loop, 
# faster, runtime 48ms; less memory, take 14.4 MB memory.

class Solution:
   def twoSum(self, nums: List[int], target: int) -> List[int]:
   #def twoSum(self, nums, target):
        output = []
        for loc, val in enumerate(nums):
            my_compares_list = nums.copy()  # make a copy of the list, so that the original list is not get changed
            my_compares_list.remove(val)      # remove the current value, so that we get the rest of the values in the list
            complement = target-val 
            
            if complement in my_compares_list:
                # location of the picked value
                output.append(loc)  
                
                # lcoation of the residual value of the picked value from target
                new_loc=my_compares_list.index(complement)  # in the orginigal list, find the residual value's location
                if new_loc>=loc: new_loc+=1   # compensate 1 index if the "new_loc" is after "loc" in the originial list
                output.append(new_loc)
                output.sort()
                break      # just need to find one solution, and task is done

        return output


#%%  solution 4, hashmap (map keys to its value pairs),
# even it has two for loops, it takes the same time as the solution3 with one for loop,
# it tells me that the hashable table is faster than list data structure

# run time 48 ms, memory use 14.4 MB.

'''
From CS6400 Database class that I took from OMSCS program: 
    hashing is appling a function to the hash field (key field), and yields
    the address on the disk where the value is saved. 
    
In python, it is implemented through the built-in dictionary data type
'''
        
class Solution:
   #def twoSum(self, nums: List[int], target: int) -> List[int]:
   def twoSum(self, nums, target):

       output    = []
       nums_dict = {}
       # this for loop just convert list into dictionary (a hashable table implemented in python)
       # this will not cost to much time as it is not conduct searching at all
       for loc, val in enumerate(nums):   
           nums_dict.update( {loc: val} )
    
       for key, value in nums_dict.items():       # iterate through the dictionary, hashable table     
           
           complement = target-value  
           temp_dict = nums_dict.copy()
           del temp_dict[key]
                    
           if complement in temp_dict.values():
               
               output.append(key)
               complement_index = list(temp_dict.values()).index(complement)
               
               if complement_index>=key: complement_index+=1
               
               output.append(complement_index) 
               output.sort()
                              
               break

       return output




#%%
'''

Redo the pratice in Feb 2025.

Searching the complement in the residual list
'''

import copy
        
class Solution:
   #def twoSum(self, nums: List[int], target: int) -> List[int]:
   def twoSum(self, nums, target):
       
       
       for i in range(len(nums)):
           
           output = []
           output.append(i)
           diff = None
           temp_list = copy.copy(nums)
                      
           a_num = nums[i]           
           temp_list.pop(i)  # remove the current investigating element
           
           
           diff = target - a_num  # how much diff from current value to target
           
           # if current value is the one we need to find
           if diff in temp_list:
               my_index = temp_list.index(diff)
               output.append(my_index+1)  # because we removed one number, here is to show what the current index in the original array
               return output
               
           # if not the number we need to find,     
           else: 
               
               del output
    
           del temp_list

       return output


#%%

'''

Redo the pratice in Feb 2025.

Searching the complement in the dictionary (hashtable)
'''

import copy
        
class Solution:
   #def twoSum(self, nums: List[int], target: int) -> List[int]:
   '''
   Iterate through the list, for a given i, save the num as the key, and its index as the val
   in the dict. 
   
   For a given num, compute the complement, target-num, if this difference exist in the dict,
   Then, the current num(key) related index(val) and the complement(key) related index(val)
   are the two index we need. 
   
   Return them in a format of a list. 
   
   '''    
       
   def twoSum(self, nums, target):
       
       mydict = {}   
       for i, num in enumerate(nums):
           complement = target-num
      
           if complement in mydict:  # if the complement is one of the keys in the dict        
               output = [mydict[complement], i]         
               return output       
           else:
               mydict.update({num:i}) # update the dict with new {val: index}
                    

       return None

#%%

nums = [2,7,11,15]
target = 9

nums = [2,7,4, 4, 11,15]
target = 8

nums = [3,2,4]
target = 6

nums = [3,3]
target = 6

#nums = [2,7,4, 4, 11,15]
#target = 8

results = Solution()
output = results.twoSum(nums, target)      
print(output)





  