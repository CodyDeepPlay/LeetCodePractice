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
    
    '''
    Solution 1,
    split the string with " ", which is space
    
    Because the string might have multiple spaces at the end of the non-space string,
    So, after split with space " ", the end results might have multiple "", which is empty or None.
    
    Starting from the last element in the splited results, iterate until the non-empty element, that is the last word.
    If the iteration reach all the way to the first, and no non-empty element is found, that means the input string is just some spaces,
    then there is no last word, will return 0. 
    
    '''
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



    '''
    solution 2,
    Using strip() method to remove any space " " at the beginning and end of the input string,
    Then split by space " ".
    
    If there is any non empty word, the last element of the cleaned list is the last word.
    
    '''
    def lengthOfLastWord2(self, s: str) -> int:
        
        # corner cases, when the input string is empty or space, no last word, 
        if s=="" or s==" ": return 0
        
        # first remove the empty space at the begining and the end of the string, using strip method. 
        # then split this cleaned string with space " ", this will generate a list of potential words.
        clean_s = s.strip().split(" ")
        
        # it is possible that the input are multiple spaces (more than two)
        # using strip will remove all the space at the begining and end of the string, no matter how many are there
        if clean_s[-1]=="": return 0  # this means the original string are several spaces, no last word
        else: return len(clean_s[-1])      # otherwis, the last element is the real last word


        
#%%
        
#s = "Hello World"
#s = "a        "
s = "         "
my = Solution()
result = my.lengthOfLastWord2(s)
print(result)
#print(needle[0:1])
