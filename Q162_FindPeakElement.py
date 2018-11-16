# -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 09:17:45 2018

@author: Mingming

LeetCode question 162, find peak element

"""
nums = [3,1]
nums = [1,2]
nums = [1,2,3,1]
nums = [1,2,1,3,5,6,4]


# this code returns a list to store all the detected peaks
class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        my_peaks = []  # create a space to store the detected peaks
        for i in range(1, len(nums)-1):  # preserve the first and last data point for calculation
            if nums[i-1]<nums[i] & nums[i]>nums[i+1]:
                my_peaks.append(i)
    
        answer =  my_peaks[0]
        return answer
    

myobject = Solution()
answer = myobject.findPeakElement(nums)
print(answer)


#%% for online submission, it requires one int number,
# if multiple peaks, just return one of the index number

# this code returns a list to store all the detected peaks
class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """        
        my_peaks = 0 # for online python at LeetCode, it requires to define the parameter before use it
        my_peaks_values = nums[0] # take the first value as the initial peak value

        for i in range(0, len(nums)):  # preserve the first and last data point for calculation
            if nums[i]>my_peaks_values:
                my_peaks = i
                my_peaks_values = nums[i]
                   
        return my_peaks
    

nums = [3]
nums = [1,2]
nums = [-2147483648,-2147483647]
nums = [1,2, 3, 4]
nums = [41,22, 13, 4]
nums = [1,2,3,1]
nums = [1,2,1,3,5,6,4]


myobject = Solution()
answer = myobject.findPeakElement(nums)
print(answer)