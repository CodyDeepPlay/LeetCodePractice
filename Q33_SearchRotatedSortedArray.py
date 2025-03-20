#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 21:16:55 2025

@author: mingmingzhang


There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
Example 3:

Input: nums = [1], target = 0
Output: -1



"""




class Solution:
    def yourSolution(self, nums, target):

        '''
        
        First, find the pivot, 
            so that anything on the left of the pivot is rotated bigger value;
            anything on the right of the pivot, including the pivot is rotated smaller array.
                
        Second, the pivot indicates the smallest value, only get the left or right side of the 
            array, which includes the target.
            
        Third, conduct binary search for the identified half. Since the identified half is the 
            one including target value; so binary search will end up finding the results that is 
            the target value. 
        
        '''
        
        if target not in nums: return -1
        
        ##### First, find the index of the pivot (index of the smallest value)
       
        # track index for first, middle and last value        
        start=0; end=len(nums)-1; mid=(start+end)//2; 
           
        # when there is only 1 value
        if len(nums)==1:
            if nums[start] == target: return start
        
        # when there are two values
        elif len(nums)==2:
            if   nums[start] == target: return start
            elif nums[end] == target: return end
            else: return -1
            
 #%%          
        # when there are more than 3, including 3 values    
        
        # stricly sorted, non-rotated array, no need to search
        if nums[start]<nums[mid] and nums[mid]<nums[end]:  
            pivot_idx = start
            start = start
            end = end
        
        # a sorted but rotated array
        else:
            # ideally, the pivot is the smallest number
            while not (nums[mid]<nums[mid+1] and nums[mid]>nums[mid+1] ):
              
                # when there are only two numbers in the search
                if start == mid or mid ==end: 
                    if   nums[start] < nums[end]: pivot_idx = start
                    elif nums[end]< nums[start]:  pivot_idx = end
                    break
            
                if    nums[start] < nums[mid]:  start = mid  # look for the right side
                elif  nums[start] > nums[mid]:  end = mid   # look for the left side
                mid=(start+end)//2;    
 
            
 
            start=0; end=len(nums)-1; 
            # now figure out which side has my target.
            if nums[pivot_idx]<=target and target<=nums[end]: # target is on the right side
                start = pivot_idx
            elif nums[pivot_idx]<=target and target<=nums[pivot_idx -1]:  
                end = pivot_idx -1 
                
             
 #%%
        ##### second, binary search on the left or right side of the array
        
        # find the half of the array that I need
        if    target == nums[pivot_idx]:  return pivot_idx
       
        #--- conduct binary search ---#
        mid=(start+end)//2;  # based on the new start and end, update mid
        n = len(nums[start:end+1])  # make sure inlcude the index that is with value "end"
        
        
        if n==1:
            if nums[start] == target: return start
            else: return -1 # the only value is not what I am looking for
        # binary search
        else:
            
            while True:
                # binary search reach to a point there are only two data points left
                if start == mid or mid ==end:
                    if   nums[start] == target: return start
                    elif nums[end] == target: return end
                    else: return -1
                else:
                    if nums[mid]== target: return mid
                    
                    elif nums[mid] > target: end = mid
                    elif nums[mid] < target: start = mid
                    mid = (start+end)//2
                


#%%
nums = [4,5,6,7,0,1,2]; target = 0 # Output: 4
nums = [4,5,6,7,0,1,2]; target = 3 # output:-1
#nums = [1]; target = 0; # output: -1

nums = [4,5,6,7,0,1,2]; target=1 # output: 5
nums = [1,2,3,4,5,6]; target=4 # output: 3
nums = [8,1,2,3,4,5,6,7]; target= 6 # output= 6

nums = [5,1,2,3,4]; target=1  # output=1
nums  = [1]; target=1
#nums = [8,9,2,3,4]; target=9; # output=1
nums = [1,3]; target=3;
nums = [1,3, 5]; target=3;
nums = [3, 5, 1]; target=3;
nums = [1,3, 5]; target=5;
nums = [5,1,3]; target = 3

results = Solution()
output = results.yourSolution(nums, target )      
print(output)





  