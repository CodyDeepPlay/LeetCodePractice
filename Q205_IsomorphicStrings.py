#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 13 22:06:55 2021

@author: mingmingzhang

leetcode 205, isomorphic strings, 


Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

 
Example 1:

Input: s = "egg", t = "add"
Output: true
Example 2:

Input: s = "foo", t = "bar"
Output: false
Example 3:

Input: s = "paper", t = "title"
Output: true
 

Constraints:

1 <= s.length <= 5 * 104
t.length == s.length
s and t consist of any valid ascii character.

"""



class Solution:
    '''
    Solution 1,
    
    Use hash map (dictionary in python) to track the appearance of a given character.
        If a character never appears, make previous location -1, and record its current location
        If a character appeared before, get it is previous appearance location. 
        
    Each time when we check a given character, the result has to match.     
    '''
    
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        tracks = {} # initialize a track in dict format
        trackt = {} # initialize a track in dict format
        
        for n in range(len(s)):
            
            # track a given character in s
            if s[n] in tracks: 
                loc_s = tracks[s[n]] # if current character is repeated before, find last time appareance
                tracks[s[n]] = n  # update the current location of this repeated character
            else: # if current character is not appearing before
                loc_s = -1    # use -1 to indicate this character is not appearing before
                tracks[s[n]] = n  # record its first appearing location
            
            # track a given character in t    
            if t[n] in trackt: 
                loc_t = trackt[t[n]] # if current character is repeated before, find last time appareance
                trackt[t[n]] = n  # update the current location of this repeated character
            else: # if current character is not appearing before
                loc_t = -1    # use -1 to indicate this character is not appearing before
                trackt[t[n]] = n  # record its first appearing location   
                
            # any time, loc_s and loc_t are not the same, s and t are not isomorphic
            if loc_s != loc_t: 
                return False
         
        # if s and t survived all the checks above, they are isomorphic
        return True
    
    
    
    '''
    Solution 2,
    
    First, if s and t has different length of set of characters, then they are not isomorphic
    Then, iterate through each character in s.
    
    If a character is not in s, then put it in the dict to track: key is the char in s, and value is char in t. 
    if a character is in s, then get the value of the key (char in s), this value should be equal to char in t.
    If not, they are not isomorphic.
    
    After surviving all the checks, they are isomorphic.
    '''
    def isIsomorphic2(self, s: str, t: str) -> bool:
              
        if len(set(s)) != len(set(t)): return False
            
        track = {} # initialize a track in dict format
        for n in range(len(s)):
            
            # track a given character in s
            if s[n] in track:           # if this character in s has appeared before
                if track[s[n]] != t[n]: # the value of the key with character in s, should be equal to the character in t
                                        # If not, s and t are not isomorphic
                    return False
            elif s[n] not in track: # if current character is not appearing before
                track[s[n]] = t[n] # use current character in s as key, store value as character in t
                
        # if s and t survived all the checks above, they are isomorphic
        return True
    
    
    '''
    Solution 3,
    Update from solution 2

    If a character is not in s, then put it in the dict to track: key is the char in s, and value is char in t. 
    if a character is in s, then get the value of the key (char in s), this value should be equal to char in t.
    If not, they are not isomorphic.
    
    After surviving all the checks, they are isomorphic.
    '''
    def isIsomorphic3(self, s: str, t: str) -> bool:
              
            
        track = {} # initialize a track in dict format
        for n in range(len(s)):
            
            # track a given character in s
            if s[n] in track:           # if this character in s has appeared before
                if track[s[n]] != t[n]: # the value of the key with character in s, should be equal to the character in t
                                        # If not, s and t are not isomorphic
                    return False
            elif s[n] not in track: # if current character is not appearing before
                
                # because s[n] is not in the keys of dictionary,never appeared
                # so t[n] should not be in the values of the dictionary, because the key-value pair relationship
                if t[n] not in track.values():  
                    track[s[n]] = t[n] # use current character in s as key, store value as character in t
                else: 
                    return False
        # if s and t survived all the checks above, they are isomorphic
        return True
    
    
    
#%%

mysolution = Solution()

s = "badc"
t = "baba"    
    
result = mysolution.isIsomorphic2(s,t)



