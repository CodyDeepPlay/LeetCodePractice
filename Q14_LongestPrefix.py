'''
Leet code question 14

Longest Common Prefix

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

'''

class Solution:
    
    '''
    Solution 1: brute force,
        - find the shortest strings in the array, assume it has length of n 
        - iterate from 0 to n
          - for each iteration in n
              iterate through each strings in the array.
              compare if if from 0 to n+1 (python will not include n+1) if all the array are the same
    '''
    def longestCommonPrefix(self, strs) -> str:
        
        # corner CASE 1, 
        # empty string is one element of the string array,
        # then there is no commom prefix
        if "" in strs: return ""
        
        num = len(strs)  # how many strings are in the list
        
        # corner CASE 2, 
        # if there is only one string in the array,
        # then it is the commom prefix
        if num ==1: return strs[0]
        
        # CACSE 3:
        # If there are more than 2 strings in the array
        len_list = [len(a_str) for a_str in strs] # get all the strings' length
        
        pre_fix_track = True
        
        # iterate along the shortest length for all the strings
        for idx in range(0, min(len_list)):
           
           # iterate through each individual strings,
           # each time, compare the consecutive string from the first to the idx th strings are the same
           #    between the previous strings and current strings.
           # Because the tracker of prefix is defaul with True, whenever the tracker 'pre_fix_track'
           # is false, means the prefix search has ended. 
           for n in range(1,num):

                pre_fix_track = (strs[n-1][0:idx+1]==strs[n][0:idx+1]) and pre_fix_track
                
                # if find not equal anytime, 
                if not pre_fix_track: 
                        # if the first element of each string are not the same, then there is no common prefix
                        if idx ==0:  return ""
                        # else, the common prefix is the first to the current one
                        else: return strs[n-1][0:idx]
         
        # you could also reach to the end,
        # that means the shortest strings is the prefix            
        return strs[n-1][0:idx+1]
    
    
                             
    '''
    Solution 1.1: optimize the code for solution 1
        
        brute force,
        - find the shortest strings in the array, assume it has length of n 
        - iterate from 0 to n
          - for each iteration in n
              iterate through each strings in the array.
              compare if if from 0 to n+1 (python will not include n+1) if all the array are the same
    '''
    def longestCommonPrefix1_1(self, strs) -> str:
        
        # corner CASE 1, 
        # empty string is one element of the string array,
        # then there is no commom prefix
        if "" in strs: return ""
        
        num = len(strs)  # how many strings are in the list
        
        # corner CASE 2, 
        # if there is only one string in the array,
        # then it is the commom prefix
        if num ==1: return strs[0]
        
        # CACSE 3:
        # If there are more than 2 strings in the array
        len_list = [len(a_str) for a_str in strs] # get all the strings' length
        
          # here use index 1 because in python, [0:1] only gives the element at index 0
      
        idx = 0  
        pre_fix_track = True
        prefix = strs[0][0]  # initialize the common prefix, by using the first element in the first string
              
        # iterate through each individual strings,
        # each time, compare the consecutive string from the first to the idx th strings are the same
        #    between the previous strings and current strings.
        # Because the tracker of prefix is defaul with True, whenever the tracker 'pre_fix_track'
        # is false, means the prefix search has ended. 
        
        while pre_fix_track:
                 
            idx +=1 # update prefix element by adding one more
             
            # reach the end of shortest string
            if idx > min(len_list): return  prefix
            prefix = strs[0][0:idx]  # update the new prefix with one more element in the string
            

            # iterate starting from 1, becaue 0th string has been picked as common prefix
            for n in range(1,num):    
                 pre_fix_track = strs[n].startswith(prefix) and pre_fix_track
                 
                 # if the current string NOT start with this prefix, 
                 if not pre_fix_track: 
                     if idx ==1: return ""
                     else: 
                         # here needs to remove the last string, 
                         # because this round return a false, that means the current prefix value
                         # is with the last element which is not the real prefix.
                         return prefix[0:-1]
        
        

    
    

    '''
    Solution 2:
        randomly pick the first string as the common string. 
        - itertate through each string in the strings list, if any string is not startswith common string,
            then cut the prefix shorter than 1,
        - if prefix is empty any time, return "", means no common prefix,
        - if by the end of iteration of each string in the list, prefix is nonempty, return prefix.
        
    '''

    def longestCommonPrefix2(self, strs) -> str:
    
        # corner CASE 1, 
        # empty string is one element of the string array,
        # then there is no commom prefix
        if "" in strs: return ""
        
        # corner CASE 2, 
        # if there is only one string in the array,
        # then it is the commom prefix
        if len(strs) ==1: return strs[0]
        
        # CACSE 3:
        # If there are more than 2 strings in the array

        prefix = strs[0]  # randomly pick the first string as a hypothetic common prefix
        
        for n in range(1, len(strs)):
            
            # for a given string, if it is not starting with prefix, then cut the prefix shorter than 1,
            # until the prefix is either empty or we reach the end of the iteration. 
            
            while strs[n].startswith(prefix)==False:
                prefix = prefix[0:-1]
                if prefix=="": return""
            
        
        return prefix    
            
            
            

    
#%%    

#strs = ["ab","a"]
strs = ["flower","flow","flight"]
#strs = ["dog","racecar","car"]

my = Solution()
result = my.longestCommonPrefix1_1(strs)
print(result)
#print(needle[0:1])
