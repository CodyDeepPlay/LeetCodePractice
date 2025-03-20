# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 15:11:31 2020

@author: Mingming

Leetcode Q198 House robber

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.


Example 1:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
Example 2:

Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.
 

Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 400
"""

#%% solution 1:  dynamic programming


class Solution:
   def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        T_i_list = []
        #end_idx_list = []
        
        for i in range(len(nums)):
            
            if i ==0: 
                T_i = nums[i]
                T_i_list.append(T_i)
                end_idx = 0

            if i ==1: 
                T_i = max(nums[i-1], nums[i])
                T_i_list.append(T_i)
                # update ending index
                if   (nums[i-1]>=nums[i]): end_idx =i-1
                elif (nums[i-1]<nums[i]):  end_idx =i

            if i>=2:               
                if end_idx == i-1: # T_i-1 includes p_i-1               
                                      
                    # 1) for index i
                    # figure out current T_i and update ending index
                    if   (nums[i-1]>nums[i]): 
                        end_idx =i-1; 
                        current_T_i = T_i_list[i-1]  
                    elif (nums[i-1]<=nums[i]):  
                        end_idx =i
                        current_T_i = T_i_list[i-1] - nums[i-1] + nums[i]
                                          
                    # 2) for index 0 to i-1
                    # add the current value to previous T_i upto index i-1 
                    T_i_plus = [ a_T_i+nums[i] for a_T_i in T_i_list[0:i-1] ] 
                    previous_max = max(T_i_plus) # with the current valued added, what is the maximum T_i from 1 to i-1. 
                    
                    # also compare with all T_i(s)
                    if previous_max >=current_T_i:  
                        end_idx =i;
                        T_i = previous_max
                    elif previous_max <current_T_i: 
                         T_i = current_T_i  # no change to previous end index, because for current_T_i, end_index was updated.
                    
                    T_i_list.append(T_i)
                elif end_idx != i-1: # T_i-1 not includes p_i-1
                    T_i = T_i_list[i-1] + nums[i]
                    T_i_list.append(T_i)
                    end_idx = i
             
            #end_idx_list.append(end_idx)
            
        return T_i_list[-1]  
    
    
    
   def rob1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
       # T_i_list = []
        #end_idx_list = []
        
        for i in range(len(nums)):
            
            if i ==0: 
                T_i = nums[i]
                T_i_2 = T_i  # the second to last T_i
                end_idx = 0

            if i ==1: 
                T_i = max(nums[i-1], nums[i])
                T_i_1 = T_i  # the current last T_I
                # update ending index
                if   (nums[i-1]>=nums[i]): end_idx =i-1
                elif (nums[i-1]<nums[i]):  end_idx =i

            if i>=2:               
                if end_idx == i-1: # T_i-1 includes p_i-1               
                                      
                    # 1) for index i
                    # figure out current T_i and update ending index
                    if   (nums[i-1]>nums[i]): 
                        end_idx =i-1; 
                        current_T_i = T_i_1 
                    elif (nums[i-1]<=nums[i]):  
                        end_idx =i
                        current_T_i = T_i_1 - nums[i-1] + nums[i]
                                          
                    # 2) the second to last T_i could be added with the p_i, which
                    # may become the newest max sum value
                    previous_max = T_i_2+nums[i]
                    # also compare with all T_i(s)
                    if previous_max >=current_T_i:  
                        end_idx =i;
                        T_i = previous_max
                    elif previous_max <current_T_i: 
                         T_i = current_T_i  # no change to previous end index, because for current_T_i, end_index was updated.
                    
                    
                elif end_idx != i-1: # T_i-1 not includes p_i-1
                    T_i = T_i_1 + nums[i]
                    end_idx = i
             
                T_i_2 = T_i_1
                T_i_1 = T_i
         
        return T_i 
    
    
      
    
     
    
   def rob2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
       # T_i_list = []
        #end_idx_list = []
        
        for i in range(len(nums)):
            
            if i ==0: 
                T_i = nums[i]
                T_i_2 = T_i  # the second to last T_i
                end_idx = 0

            if i ==1: 
                T_i = max(nums[i-1], nums[i])
                T_i_1 = T_i  # the current last T_I
                # update ending index
                if   (nums[i-1]>=nums[i]): end_idx =i-1
                elif (nums[i-1]<nums[i]):  end_idx =i

            if i>=2:               
                if end_idx == i-1: # T_i-1 includes p_i-1               
                                      
                    # 1) for index i
                    # figure out current T_i and update ending index
                    if   (nums[i-1]>nums[i]): 
                        end_idx =i-1; 
                        current_T_i = T_i_1 
                    elif (nums[i-1]<=nums[i]):  
                        end_idx =i
                        current_T_i = T_i_1 - nums[i-1] + nums[i]
                                          
                    # # 2) the second to last T_i could be added with the p_i, which
                    # # may become the newest max sum value
                    # previous_max = T_i_2+nums[i]
                    # # also compare with all T_i(s)
                    # if previous_max >=current_T_i:  
                    #     end_idx =i;
                    #     T_i = previous_max
                    # elif previous_max <current_T_i: 
                    #      T_i = current_T_i  # no change to previous end index, because for current_T_i, end_index was updated.
                    
                    
                elif end_idx != i-1: # T_i-1 not includes p_i-1
                    current_T_i = T_i_1 + nums[i]
                    end_idx = i
             
                
                # 2) the second to last T_i could be added with the p_i, which
                # may become the newest max sum value
                previous_max = T_i_2+nums[i]
                # also compare with all T_i(s)
                if previous_max >=current_T_i:  
                    end_idx =i;
                    T_i = previous_max
                elif previous_max <current_T_i: 
                     T_i = current_T_i  # no change to previous end index, because for current_T_i, end_index was updated.
                
                
              
             
                T_i_2 = T_i_1
                T_i_1 = T_i
         
        return T_i 
    
       
    

#%%

nums = [1,2,3,1]
results = Solution()
output = results.rob(nums)      
print(output)

output = results.rob1(nums)      
print(output)


output = results.rob2(nums)      
print(output)


#%%




  
  
  
  
  
  
  
  
  