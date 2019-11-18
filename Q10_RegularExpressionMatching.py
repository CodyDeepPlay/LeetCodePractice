# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 17:17:06 2019

@author: Mingming


Q 10
Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

Note:

s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z, and characters like . or *.

"""


s = 'aa'
p = 'a'

class Solution:
    def isMatch(self, s, p):
        # if the two inputs are the same, then output is "True"
        if s==p:
           judge = True 
        # if the two inputs are not the same, then conduct further analysis
        else:
           # if two strings has the same length
           if len(s)==len(p):
              
               all_dot  = [counter for counter, value in enumerate(p) if value =='.']               
               all_star = [counter for counter, value in enumerate(p) if value =='*']
               
               # only have '*'
               if len(all_star)==0 & len(all_dot)!=0:
                  judge = True 
               
                # no '.' or '*'   
               elif len(all_star)==0 & len(all_dot)==0: 
                   judge = False 
               # only has '.' 
               elif len(all_star)!=0 & len(all_dot)==0: 
               
               
               p.find('.')   # returns -1 if there is no '.'
           
           
           # if the two strings has different length
           elif len(s)<len(p):
               
               
#%%%%%%%%%%%%%%%%%%%
               
text = ''
pattern = 'a'

hi  ={'.', 'a'}


'''
ONLINE SOLUTION
'''

# WHEN THERE IS NO KLEEN STAR, THE SOLUTION IS AS THE FOLLOWING:
def match(text, pattern):
    
    if not pattern: # only execute if pattern is empty
        return not text # if text is empty, then return true; if text in non-empty, return false
    first_match = bool(text) and pattern[0] in {text[0], '.'}
    return first_match and match(text[1:], pattern[1:])


               
# WHEN THERE IS KLEEN STAR IN PRESENCE, THE SOLUTION IS AS THE FOLLOWING:               
class Solution(object):
    def isMatch(self, text, pattern):
        if not pattern: # if pattern is empty, 
            return not text  # then return True if text is empty, or return false if text is not empty

        first_match = bool(text) and pattern[0] in {text[0], '.'}
        # bool(text): is True if text is non-empty, is false if text is empty
        # if pattern[0] is in dictionary {text[0], '.'}, return True, otherwise Flase.
        
        # if pattern length is more than 2, and the second element is *
        if len(pattern) >= 2 and pattern[1] == '*':
            return (self.isMatch(text, pattern[2:]) or
                    # if text matches the rest of the pattern after the first two elements, then
                    # then the second * could repeat the first element zero time
                    first_match and self.isMatch(text[1:], pattern))
                    # in another condition, first match and the rest of the text matches pattern,
                    # then the * at the second element can also just repeat the first element one time
        
        else:
            return first_match and self.isMatch(text[1:], pattern[1:])


