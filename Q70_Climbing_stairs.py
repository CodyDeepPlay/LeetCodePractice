#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 21:16:55 2025

@author: mingmingzhang

You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step


"""




class Solution:
    def yourSolution(self, n ):

        '''
        1. base cases
        if n =1, there is only one, just take 1 step
        if n =2, there are two ways, take (1+1) or take (2) steps
        if n =3, there are three ways, take (1+1+1), (1+2), (2+1)
        
        2. Dynamic Programming initialization
        prev1: the number of ways climb to the previous step, initialized to 3
        prev2: the number of ways climb to the step before previous step, initialized to 2
        cur: tracks the current nubmer of ways to climb the current step, initialized to 0
        
        3. iterative calculation
        Assume we have this scenario, 
        previous stair we have 3 ways to get there, 
        prevuous 2 stair we have 2 ways to get there
    
        2  3  ?
        ^  ^  ^
        
        for curreht stair "?", there are only two ways, 
        either: take two step from prev2
        2     ?
        ^ - - ^
        (Thus: from the begining-->prev2--> current step, there are only two ways)
        
        or : take one step from prev1
        2   3   ?
        ^   ^ _ ^
        (Thus: from the begining-->prev1--> current step, there are only three ways)
        
        so the cur = prev1 + prev2, this is the iterative equation. 
        
        '''
        
        # code
        

        if  n<=3: return n
        
        elif n>3:
          
            prev1 = 3
            prev2 = 2
            cur = 0
            
            for i in range(3, n): # here start from at least 4 steps, index is 3 
                cur = prev1 + prev2 # track the current steps, how many ways are there               
                # once done the calculation for current step, update the previous state paramters
                prev2 = prev1
                prev1 = cur
               
            
        return cur
        



#%%

n = 2  # output = 2
#n = 4  # output=5
n = 5  # output=10


results = Solution()
output = results.yourSolution(n )      
print(output)





  