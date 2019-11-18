# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 19:44:14 2019

@author: Mingming


Leet code Q3, LongestSubstring without repeating characters
"""



class Solution:
    
    """
    Add each element into a set, until the next string is already exist in the current set.
    Then, update the set with the newly extract string.
    """
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        longest = 0   # default the value for longest string.
        pointer = 0   # indicate last time where the repeated string appears
        my_set =set([])  
        
        for count, string in enumerate(s):
             # if the newly extract string is in the set of unique parameters           
            if string in my_set: 
               my_set =set([])   # define a new empty set to store non-repeated strings.                                             
               
               repeat_index_all = [pos for pos, char in enumerate( s[pointer:count]) if char == string] # get all repeated string locations
               repeat_index = repeat_index_all[-1] + pointer # get the latest repeat string location, 
                                                             # find where current string repeats in original strings, by adding pointer onto it
               {my_set.add(s[n]) for n in range(repeat_index+1,count) } # put all non-repeat string into the same sets
               pointer = repeat_index   # update where the repeat string happens
               
            # always add current string into the set, if current string is already within the set, the set will be set to 
            my_set.add(string) # add this string to form a new set of unique parameters
            longest = max( longest, len(my_set) )  # update the new longest string length
            #print(my_set)
        return (longest)
        
          
        s = "pwwkew"
        s = "asjrgapa"
        s = "umvejcuuk"
              

#%%  
class Solution:
    
    """
    Sliding window approach
    """
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        longest = 0
        
        for loc, string in enumerate(s): # starting from each string and conduct the sliding window
             
             non_repeat = ''  # for each new string, default non_repeat string is zero.
             new_s = s[loc:]  # conduct sliding window for this new string
             
             for loc2, string2 in enumerate(new_s): 
                 if string2 not in non_repeat: # if new string is not in the non_repeat string, 
                     non_repeat += string2     # add it to form new non_repeat string
                 else:  # if new string is within the repeat string, break current for loop
                     break
             
             longest = max(len(non_repeat), longest) # update the longest string
             
        return(longest)
        

#%%

        s = "pwwkew"
        s = "asjrgapa"
        s = "umvejcuuk"
        s = ""
        s = " "              
        
class Solution:
    """
    sliding window, but wrapped function into return to simplify the main code
    """
    #def lengthOfLongestSubstring(s):    
    def lengthOfLongestSubstring(self, s: str) -> int:    
        if not s:  # if s is empty
            return 0
        
        non_repeat = ''  # for each new string, default non_repeat string is zero
        for loc2, string2 in enumerate(s): 
            if string2 not in non_repeat: # if new string is not in the non_repeat string, 
                non_repeat += string2     # add it to form new non_repeat string
            else:  # if new string is within the repeat string, break current for loop
                break
             
        longest = len(non_repeat) # update the longest string             
        return  max(longest , self.lengthOfLongestSubstring(s[1:]))          


#%%

answer = lengthOfLongestSubstring(s)
print(answer)