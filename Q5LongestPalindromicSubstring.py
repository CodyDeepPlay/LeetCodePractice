# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 17:39:34 2019

@author: Mingming


Leetcode problem No.5 Longest Palindromic Substring

Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.

Example 2:

Input: "cbbd"
Output: "bb"
"""
s = "babad"
s = "bb"
s = 'cwewredbdbd'

s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabcaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
#%%
class Solution:
    
    def isPalindrome(self, string):
            '''
            Given a string input, 
            return if the input is palindrome, True or False; 
            also return the length of the given input string
            ''' 
            # check if the first and last string is the same, then the second the second last is the same ...
            # ... repeat this process until you reach the last check point, which is the middle point of the 
            # original string. 
            check_len = len(string)//2 # check length is half of the string length
            if check_len == 0:
                return True 
            
            else:
                first_half = string[0:check_len]  # first half of the string
                reverse_string   = string [::-1]  # first half of the string
                reverse_2nd_half = reverse_string[0:check_len]
                
                return (first_half == reverse_2nd_half)
 
    
    def longestPalindrome(self, s: str) -> str:
        # if the string is empty, or single string, it will return True
        # or if the string is more than 1 character, but palindrome, it will return True
        palindrome_bool = self.isPalindrome(s)
        if palindrome_bool:
           return s
        
        # take the next longest string within this entire string, until the length of the string is 2
        total_string_len = len(s)
        max_remove_len = total_string_len-2 + 1 # what is the max length of removable characters in this string before it reaches to 2
        for total_remove in range(1,max_remove_len): # each time, what is maximum removable string in this given string
                                                       # increase by 1 in each iteration               
            # each time, when comfirm how much string to remove, this also defines
            # what is the length of the current string
            current_str_len = total_string_len - total_remove 
            num_new_string  = total_remove + 1  # remove one string charactor, will generate one more substring
           
            # when knowing how much string to remove, then slide the window to get all the substrings
            for num_remove in range(num_new_string):  # 
                test_string = s[0 +  num_remove      : current_str_len        + num_remove]
                test_bool = self.isPalindrome(test_string)  
                #print(test_string)
                # if ever come across a palindrome string, taks is done, then break the loop
                if test_bool: 
                    return test_string
                    break
            
        # if after all of this, still not palindrome, then any single charactor is palindrome
        return s[0]
        
        

            
            
#%%            

s = 'abbcbgyi'

me = Solution()
me.longestPalindrome(s)          
            
            
            
            
            
            
            
            