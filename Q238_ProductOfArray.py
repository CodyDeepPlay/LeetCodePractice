#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 21:16:55 2025

@author: mingmingzhang


Leetcode Q238

Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
 

Constraints:

2 <= nums.length <= 105
-30 <= nums[i] <= 30
The input is generated such that answer[i] is guaranteed to fit in a 32-bit integer.
 

"""

import math
import copy

#%% solution 1:  3 for loops speed and is very slow
class Solution:
    def yourSolution1(self,  nums):
    #def twoSum(self, nums, target):
        
        '''
        iterate through each list
        This solutions works for general cases.
        
        When the input list is very large, it will error out, because the 
        math.prod() is basically also runing a for loop with complexity of O(n).
        This is within the outer for-loop that I already coded here.
        '''
        
        output = []
        for i in range(len(nums)):
            
            temp_list = copy.copy(nums)
            temp_list.pop(i)
            
            current_product = math.prod(temp_list)
            output.append(current_product)
            
            
            del temp_list
            
        return output
        



    def yourSolution2(self,  nums):
    #def twoSum(self, nums, target):
        
        '''
        pre-fix and sufix product
        
        compute the product from the left and right product
        
        
        Assume we have a list [a, b, c, d]
        n is the length of the list.
        
        initialize our final product, ans=[1,1,1,1]
        
        Let's conduct the forward loop
        initialize, ans1=[1,1,1,1]
        i=1, [1, ans1[i-1]*num[i-1], 1, 1]     
             ans1= [1, a, 1, 1]
        i=2, [1,a, ans1[i-1]*num[i-1], 1]    
             ans1= [1, a, a*b, 1]                
        i=3, [1,a, a*b, ans1[i-1]*num[i-1]]   
             ans1= [1, a, a*b, a*b*c]     
             
             
        
        Let's conduct the backward loop,
        initialize, ans2=[1,1,1,1]
        j=n-i
        j=3, [1,1,ans1[j]*num[j],1]
             ans2= [1,1,d,1] 
        j=2, [1,ans1[j]*num[j],d,1] 
             ans2= [1,c*d,d,1] 
        j=1, [ans1[j]*num[j],c*d,d,1]  
             ans2= [b*c*d,c*d,d,1] 
        
        
               
        Now we can see that     
            ans1=[1,     a,   a*b, a*b*c]
            ans2=[b*c*d,c*d,  d,    1]
            
        final answer, each element is equal to the product of the related element
        in ans1 and ans2
        
        In addition, we can see that j = n-1-i,
        So, the above product can be computed in one for loop.
        
        
        
        '''
        n = len(nums)
        output = [1]*n
        ans1   = [1]*n  # host answers for forward loop
        ans2   = [1]*n # host answers for backward loop

              
        for i in range(1,len(nums)):
            
            # compute forward product
            forward_prod = ans1[i-1]*nums[i-1]            
            ans1[i] = forward_prod
            
            # compute backward prodcut
            j = n-i
            backward_prod = ans2[j]*nums[j] 
            ans2[j-1] = backward_prod
                
            
        #  iterate through each element in forwrad and backward array, and 
        # get the final product              
        for i in range(n):           
           output[i] = ans1[i]*ans2[i]

         
        return output
        



    def yourSolution3(self,  nums):
    #def twoSum(self, nums, target):
        
        '''
        pre-fix and sufix product
        
        Further simply the code for solution2
        
        using a single term 'prefix' to represent "ans1[i-1]"
        using a single term 'sufix' to represent "ans2[j]"
        
        
        '''
        n = len(nums)
        output = [1]*n
        prefix = 1  # track forward product
        sufix  = 1  # track backward product
        
      #  ans1   = [1]*n  # host answers for forward loop
       # ans2   = [1]*n # host answers for backward loop

              
        for i in range(1,len(nums)):
            
            # # compute forward product
            # prefix = prefix*nums[i-1]                       
            # ans1[i] = prefix
            # output[i] = output[i]*ans1[i]
            
            
            # # compute backward prodcut
            # j = n-i
            # sufix = sufix*nums[j]             
            # ans2[j-1] = sufix
            # output[j-1] = output[j-1]*ans2[j-1]
            
            
            # compute forward product
            prefix = prefix*nums[i-1]                       
            output[i] = output[i]*prefix
            
            
            # compute backward prodcut
            j = n-i
            sufix = sufix*nums[j]             
            output[j-1] = output[j-1]*sufix
            
            
            
            
            
            
         
        return output
        




#%%
nums = [1,2,3,4]
#Output: [24,12,8,6]

#nums = [-1,1,0,-3,3]
#Output: [0,0,9,0,0]


results = Solution()
output = results.yourSolution3( nums)      
print(output)





  