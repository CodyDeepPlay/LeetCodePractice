#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  6 22:23:29 2021

@author: mingmingzhang


leet code question 58,

Given a string s consists of some words separated by spaces, 
return the length of the last word in the string. If the last word does not exist, return 0.

A word is a maximal substring consisting of non-space characters only.



"""

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        if s=="" or s==" ": return 0
        
        words_list =s.split(" ")
        
        idx=-1
        while words_list[idx]=="":
            idx -=1 
            # reach all the possible words, it is still empty
            #   here pay attention to the negative index
            #   because we start from the very end,
            #    idx=-1 means the last element in a string or array
            #    idx=-n means the first element in a string or array, if n is the length of a array
            # so, the stopping criteria here is -idx > the length of the array
            
            if -idx > len(words_list): return 0   # if you ever reach this if statement, means the all the words are empty 
             
        # if you come out of the loop, means you find the last non-empty word, 
        # then get its length
        return len(words_list[idx])

        
#%%
        
s = "Hello World"
#s = "a        "
#s = "         "
my = Solution()
result = my.lengthOfLastWord(s)
print(result)
#print(needle[0:1])
