#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 10 23:13:41 2021

@author: mingmingzhang

345. Reverse Vowels of a String

Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both cases.


Example 1:

Input: s = "hello"
Output: "holle"
Example 2:

Input: s = "leetcode"
Output: "leotcede"


"""

class Solution:
    
    '''
    Solution 1,
    
    find the vowels first, and reserve them
    
    '''
    def reverseVowels(self, s: str) -> str:
        vowels = ["a", "e","i", "o", "u", "A", "E","I", "O", "U", ]
        
        # find any possible vowels
        idx_list = []
        for n in range(len(s)):
            if s[n] in vowels: idx_list.append(n)
        
        # no vowel or just 1 vowel found
        if len(idx_list)==0 or len(idx_list)==1: return s
        
        # two or more vowels are found
        left=0; right=len(idx_list)-1;   
        while left<right: 
            temp_left = s[idx_list[left]]
            temp_right = s[idx_list[right]]
            
            # replace the left found vowel
            s = s[0:idx_list[left]] + temp_right + s[idx_list[left]+1:]
            # replace the right found vowel
            s = s[0:idx_list[right]] + temp_left + s[idx_list[right]+1:]
            
            left  +=1
            right -=1
            
        return s    
        
    '''
    Solution 2,
    One for loop starting from beginning, 
    if a vowel found, then starting from the end backwards to conduct next search
        if found a vowel, then swap the previous finding.
        Then continue this process
        
    '''
    def reverseVowels2(self, s: str) -> str:
        
        if len(s)==1 or len(s)==0: return s

        vowels = ["a","e","i","o", "u","A","E","I","O","U"]
        right_end = len(s)-1

        for l in range(right_end+1): # will include 0 to right_end, so plus 1 here to include right_end

            # find vowel on the left side
            if s[l] in vowels: 

                for r in range(right_end, l, -1):  
                    # find vowel on the right side
                    if s[r] in vowels: 
                        temp = s[l]  # extract the left
                        s = s[0:l] + s[r] + s[l+1:] # put right into left
                        s = s[0:r] + temp + s[r+1:] # put left into right

                        right_end = r-1 # already found at vowel in right side, so next iteration will not include this one
                        break # finish one finding, will break the right side search

        return s
    
    
    