
'''
Leet code question 28

Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

'''

class Solution:
    
    '''
    Solution 1, python string built-in method, find
    '''
    def strStr(self, haystack: str, needle: str) -> int:
        
        return haystack.find(needle)

    '''
    Solution 2, each time compare nlen of string in the haystack to see if it matches the needle,
    the nlen here is the length of needle. 
    '''
    def strStr2(self, haystack: str, needle: str) -> int:
        
        if needle =="": return 0
        
        nlen = len(needle) # needle length

        # here need to add 1, 
        # when remove the length of needle, 'nlen' from the len of haystack, 
        # there will be 'len(haystack)-nlen+1' times of iteration where we can compare needle
        # using the same length of elements from haystack
        for n in range(0, len(haystack)-nlen+1):
            if haystack[n:n+nlen]==needle: 
                return n
        
        # if you reach here, means you didn't find a needle
        return -1



#%%

haystack = "a"
needle = "a"

my = Solution()
print(my.strStr2(haystack, needle))
#print(needle[0:1])
