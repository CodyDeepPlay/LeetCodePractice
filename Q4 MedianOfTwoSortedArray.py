# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 16:58:00 2019

@author: Mingming

Question 4: Median of two sorted array

Example 1: 
nums1 = [1, 3]
nums2 = [2]
The median is 2.0

Example 2:
nums1 = [1, 2]
nums2 = [3, 4]
The median is (2 + 3)/2 = 2.5


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
"""

class Solution:
    def findMedianSortedArrays(self, nums1, nums2): 
        
        # GIVEN A NUMBER, INSERT IT INTO A SORTED ARRAY       
        def inserMyNumber(fix_one_number, nums2):           
            # the fix number is smaller or equal than the smallest element of nums2
            if fix_one_number<=min(nums2):
               nums2.insert(0,fix_one_number) # put it at the beginning
            # if the fix number is bigger or equal than the biggest element in nums2   
            elif fix_one_number>=max(nums2):
               nums2.append(fix_one_number)    # put it at the last            
            # if the fix number is somewhere in between the second array
            else:    
               for id2 in range(1,len(nums2)):   # compare with all the sorted numbers in the second list
                   if (fix_one_number >= nums2[id2-1]) & (fix_one_number < nums2[id2]):
                      insert_id = id2  # bigger or equal than the current value, the put be
                      break  # break the current for loop
               nums2.insert(insert_id,fix_one_number)    # put it at the last           
                  
            return nums2 
      
        #nums1 = [1,2,16]
        #nums2 = [7]
        total_length = len(nums1) + len(nums2)  
        
        # at least one them is empty
        if (not nums1) | (not nums2): 
           if (nums1):      # if nums1 is not empty, this will be the final array
               nums2 = nums1
           else :           # if nums2 is not emtpy or empty, nums2 will be final array
               nums2 = nums2        
        # both least are non-empty     
        else:
        # insert all the number from the 1st list into the 2nd list
            for id1 in range(len(nums1)):    
                fix_one_number = nums1[id1]  # take one number from first list
                inserMyNumber(fix_one_number, nums2)        
    
        if (total_length%2) == 1:   # odd number, take 
            take_ID = (total_length//2 + total_length%2) -1 # -1: python index starts from 0            
            median = nums2[take_ID] 
        elif (total_length%2) == 0:   # even number, take 
            take_ID = (total_length//2 - 1, total_length//2+1 - 1) # -1: python index starts from 0  
            median = (nums2[take_ID[0]] + nums2[take_ID[1]] )/2
        #print(median)
       
        return median
        #print(median)   