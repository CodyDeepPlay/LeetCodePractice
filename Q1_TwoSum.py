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

#%%  fist versin of code, a lot of for loops speed is slow
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
        
#%%


class Solution:
    #def twoSum(self, nums: List[int], target: int) -> List[int]:
    def twoSum(self, nums, target):
        
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
        
        
        # where the input target is even number, there is two halves in the list
        if half_search_residual == 0 and len(exact_half_number_loc)==2:
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
        
        
#%%

nums = [2,7,11,15]
target = 9

nums = [2,7,4, 4, 11,15]
target = 8

nums = [3,2,4]
target = 6

nums = [3,3]
target = 6

nums = [2,7,4, 4, 11,15]
target = 8

results = Solution()
output = results.twoSum(nums, target)      
print(output)





  