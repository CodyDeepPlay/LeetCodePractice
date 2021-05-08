#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  7 21:57:10 2021

@author: mingmingzhang


387. First Unique Character in a String

Given a string s, return the first non-repeating character in it and return its index.
 
If it does not exist, return -1.

Example 1:

Input: s = "leetcode"
Output: 0
Example 2:

Input: s = "loveleetcode"
Output: 2
Example 3:

Input: s = "aabb"
Output: -1


"""


class Solution:
    
    '''
    Solution 1
    Iterate through each character, check if current character is not in the rest of the characters,
    When it happens, that is the first non-repeating character.
    '''
    
    def firstUniqChar(self, s: str) -> int:
        
        # corner cases
        if s=="":     return -1
        if len(s)==1: return 0
    
        # there are more than two elements in s
        # check if the current characters is not in the rest of the character in the string,
        # whenever it happens the first time, that is the answer
        
        for n in range(0, len(s)):            
            
            # be careful, deal with index=0 is different than the rest of index
            if n==0: 
                if s[n] not in s[n+1:]: return n
            
            elif n!=0:
                if s[n] not in (s[:n]+s[n+1:]): return n
               
        # if you reach the last, means every character has been repeated, so no non-repeat character
        return -1    
    
    
    '''
    Solution 2, use hashmap,(dictionary in python)
    Even with two for loops, this solution is faster !!!
    
    first for loop, track the number of appearance for each string
    second for loop, whenever the current character is only with appearance 1, that is the answer and return its index
    
    '''
    def firstUniqChar2(self, s: str) -> int:
        
        if s=="":     return -1
        if len(s)==1: return 0
    
        # there are more than two elements in s
        mydict={}
        
        for n in range(len(s)):                 
            if s[n] in mydict: mydict[s[n]] +=1
            else: mydict.update( {s[n]: 1 }  )
                
        for n in range(len(s)):         
             if mydict[s[n]]==1: return n
               
        # if you reach the last, means every character has been repeated, so no non-repeat character
        return -1    
    
    
#%%    


#s = "leetcode"
s = "llllllllld"

my = Solution()
result = my.firstUniqChar(s)
print(result)
#print(needle[0:1])