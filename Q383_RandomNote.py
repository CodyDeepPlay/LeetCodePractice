#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  7 22:46:24 2021

@author: mingmingzhang

Q383 Random note

Given two stings ransomNote and magazine, return true if ransomNote can be constructed from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.


Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false
Example 2:

Input: ransomNote = "aa", magazine = "ab"
Output: false
Example 3:

Input: ransomNote = "aa", magazine = "aab"
Output: true


"""
from collections import Counter

class Solution:
    '''
    Solution 1,
    using two for loops,
    
    The first for loops count the nubmer of appearance for each character in magazine
    
    The second for loops track each individual character in ransomeNode to see if it is in my hashmap.
    If not, the anwser is return False,
    If yes, then subtract the appearance 1 time, until appearnace is negative, then answer is False.
    
    If go through the whole process, no negative appearance, then it is True.
    
    '''
    
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        # Corner cases
        
        # if characters in magazine is less than in ransomNote
        if len(ransomNote)>len(magazine): return False   
        # magazine is space, but ransomNode is non-space string.
        if ransomNote!=" " and magazine == " ": return False 
        # both strings are space
        if ransomNote==" " and magazine == " ": return True

        
        
        mydict = {}
        
        # first for loop tracak the number of appearance for each character
        for n in range(len(magazine)):
            # track each character appearing times
            if magazine[n] in mydict: mydict[magazine[n]] +=1
            else:     mydict.update({magazine[n]: 1 })
                
        # second for loop, check is a single character in 'ransomNote' are in my hashmap,
        # if not, then return False,
        # if yes, substract the appreance 1 times, if anytime the number of appreance is negative, then return False,
        # if the check survives the whole process, then it is True
        for n in range(len(ransomNote)):        
            if ransomNote[n] not in magazine: return False          
            else: 
                mydict[ransomNote[n]] -=1
                if mydict[ransomNote[n]]<0: return False
                
        return True       
    
    
    
    '''
    Solution 2: 
        First use Counter to count the appearance of each character in both magazine and ransomeNote, 
        it will return results in dict format
        
        Then, check each key in ransomeNote to make sure the same key will have more number of appearance in magazine.
    '''
    def canConstruct2(self, ransomNote: str, magazine: str) -> bool:
        
        # Corner cases
        
        # if characters in magazine is less than in ransomeNote
        if len(ransomNote)>len(magazine): return False   
        # magazine is space, but ransomNode is non-space string.
        if ransomNote!=" " and magazine == " ": return False 
        # both strings are space
        if ransomNote==" " and magazine == " ": return True

        
        r = Counter(ransomNote)  # Counter will count the number of appearance, and return them in dict format
        m = Counter(magazine)
        
        
        for key in r:   
            # the key in r is also in m
            if key in m:
                if r[key]>m[key]: return False      
            # r has key that is not in m, so it is False
            else: return False
        
        # if you survive, means every then it is True
        return True
    
    
    
#%%

ransomNote = "aa"
magazine = "ab"


my = Solution()
result = my.canConstruct2(ransomNote, magazine)
print(result)
#print(needle[0:1])