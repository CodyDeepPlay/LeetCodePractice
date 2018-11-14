# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 16:47:29 2018

@author: Mingming

Leet code, 
    algorithm, 
    question # 852
    Q852, peak index in a mountain array
---------------------------------------------------------
Let's call an array A a mountain if the following properties hold:

A.length >= 3
There exists some 0 < i < A.length - 1 such that A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1]
Given an array that is definitely a mountain, return any i such that A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1].

Example 1:

Input: [0,1,0]
Output: 1
Example 2:

Input: [0,2,1,0]
Output: 1
Note:

3 <= A.length <= 10000
0 <= A[i] <= 10^6
A is a mountain, as defined above.

"""

#%%
A = [0,1,0]
#A = [0 , 1 , 58 , 95, 56 ,5 ,4 ,0]

import numpy as np

class Solution:
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        diff_seires     = np.diff(A) # get the derevative of the original time series
        incr_diff_index = np.where(diff_seires>0) # if the time series increase, the diff series should be > 0 
       
        if len(incr_diff_index[0])==1:
            mountain_peak_index = incr_diff_index[0] + 1
        else:
            reformat = np.squeeze(incr_diff_index)  # reformat the data to remove unnecessary dimensions
            mountain_peak_index = reformat[-1] + 1  # the last index is the mountain peak index, 
                                                    # +1 return the index from deravative back into orginal time series
        return mountain_peak_index
        
        
index_obj = Solution()   # define an object, belongs to class Solution.

my_index= index_obj.peakIndexInMountainArray(A)

print('my index is ', str(my_index))    
        
        
        
#%% Leet code doesn't like users to import modules.
        
#A = [0 , 1 , 58 , 95, 56 ,5 ,4 ,0]       
A = [0,1,0]   
class Solution:
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """        
        total_num = len(A)        
        index = []
        for i in range(1, total_num):
            if A[i]<A[i-1]:
                index.append(i)  # find all the element that is decreasing
                
        my_peak_index = index[0] - 1  # the one before the first index is the peak index        
        return my_peak_index

  
index_obj = Solution()   # define an object, belongs to class Solution.
my_index  = index_obj.peakIndexInMountainArray(A) # the object can call any function defined wihtin this Class
print('my index is ', str(my_index))    
            
    