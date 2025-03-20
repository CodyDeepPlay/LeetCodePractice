#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 21:16:55 2025

@author: mingmingzhang


Leetcode 1143


Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".
A common subsequence of two strings is a subsequence that is common to both strings.

 
Example 1:
Input: text1 = "abcde", text2 = "ace" 
Output: 3  
Explanation: The longest common subsequence is "ace" and its length is 3.

Example 2:
Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.

Example 3:
Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.




take this example text1 = "abcde", text2 = "ace" 
        a b c d e
      i
   j 
a  0
c  0
e  0





"""








class Solution:
    def yourSolution(self,  ):

        '''
        Tcomments
        '''
        
        # code
        pass
              
        return None
        



#%%

#text1 = "abcde"; text2 = "ace"  # Output: 3 
text1 = "abc"; text2 = "abc"  # output 3

text1 = "abc"; text2 = "def" # output 0


results = Solution()
output = results.yourSolution(text1, text2)      
print(output)





  