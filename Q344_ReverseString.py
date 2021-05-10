#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  9 21:46:32 2021

@author: mingmingzhang

Leetcode 344 reverse string


Write a function that reverses a string. The input string is given as an array of characters s.

 

Example 1:

Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
Example 2:

Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
 

Constraints:

1 <= s.length <= 105
s[i] is a printable ascii character.

"""

class Solution:
    
    '''
    Solution 1,
    
    two pointer, iteration: 
        - starting from left=0, right=-1
        - swap left and right pointer values, 
        - after each swap, increase left by 1, and decrease right by 1.
        - when left<right is no longer true, stop search
        
    '''
    
    def reverseString(self, s) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        # if s length is 0 or 1, no need to do anything 
        if len(s)==0 or len(s)==1: pass
        
        left=0; right=len(s)-1
        
        while left<right:      
            temp = s[left]
            s[left] = s[right]
            s[right] = temp           
            left +=1
            right -=1
 
    
    '''
    Solution 1.1,
    
    two pointer, recursion: 
        - starting from left=0, right=-1
        - swap left and right pointer values, 
        - after each swap, increase left by 1, and decrease right by 1.
        - when left<right is no longer true, stop search
        
    '''
    
    def reverseString1_1(self, s) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        def helper(left, right):
            if left<right:      
                temp    = s[left]
                s[left] = s[right]
                s[right] = temp           
                left, right = left+1, right-1
                helper(left, right)
        
        left=0; right=len(s)-1
        helper(left, right)
        
        
        
        

    def reverseString2(self, s) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        s.reverse()
 



#%%

#s = "leetcode"
s = ["h","e","l","l","o"]

my = Solution()
my.reverseString1_1(s)
print(s)
#print(needle[0:1])