#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  9 22:38:15 2021

@author: mingmingzhang

Leet code 151 Reverse Words in a String


Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

 
Example 1:

Input: s = "the sky is blue"
Output: "blue is sky the"
Example 2:

Input: s = "  hello world  "
Output: "world hello"
Explanation: Your reversed string should not contain leading or trailing spaces.
Example 3:

Input: s = "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.
Example 4:

Input: s = "  Bob    Loves  Alice   "
Output: "Alice Loves Bob"
Example 5:

Input: s = "Alice does not even like bob"
Output: "bob like even not does Alice"
 

Constraints:

1 <= s.length <= 104
s contains English letters (upper-case and lower-case), digits, and spaces ' '.
There is at least one word in s.

"""

class Solution:
    
    '''
    Solution 1,
        Using string split by " ", 
        - then iterate through the last item to the first one, 
        - when the string length is not 0, then find a word, put into the result with space
        - after the last iteration, don't forget to remove the last space at the end, no need for it.      
    '''
    
    def reverseWords(self, s: str) -> str:
        
        s_list = s.split(" ")
        
        # there is only one word.
        if len(s_list)==1: return s_list[0]
        
        # there are more than one words.
        result =""
        for n in range(len(s_list)):
            
            # starting from last the item    
            if len(s_list[-1-n]) !=0: # find a word
                
                result+=s_list[-1-n]
                result+=" " # between words need to separated by space
            
        # don't include the last item, which is the space after the last word  
        return result[0:-1]  



    '''
    Solution 2,
        Using string split by defaul, which is any whitespace, 
        Then reserve the word list, and put white space in-between
   
    '''
    
    def reverseWords2(self, s: str) -> str:
        
        s_list = s.split()   # default separator is any white space. 
        
        result = " ".join(s_list[::-1])  # put " " in between each string element in the list
        
        return result


#%%        
s = "    a good   example   "        
#s = "the sky is blue"
my = Solution()
result = my.reverseWords2(s)
print(result)
#print(needle[0:1])


#%%



#%%
