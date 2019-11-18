# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 17:43:02 2019

@author: Mingming

Leet code question 8, string to integer
"""
mystr = ' sfagrag -888++99'

#%%
class Solution:
    def myAtoi(self, mystr: str) -> int:
              
        
        ######   RULE OUT SINGLE SOME NON-NUMERIC CHARACTER
        # If the input string is only single string of '+' or '-' or empty, it is not convertable
        if mystr.replace(' ','') == '+' or mystr.replace(' ','') == '-' or mystr.replace(' ','') == '':
           return 0
        
        my_num_str = ['0', '1', '2', '3', '4', '5','6','7','8','9','.'] 
     
        non_empty_str = mystr.replace(' ','') 
        # If the first non-empty string is not number or sign, then consider non-convertabe
        if non_empty_str[0] not in (my_num_str + ['+', '-']): 
            return 0   
        
        ######   TAKE THE FIRST CONSECUTIVE NUMERIC STRING
        # If there is any non-numeric string in between, take the first consecutive numeric string
        locs_org = [loc for loc, val in enumerate(mystr) if val in (my_num_str + ['+', '-'])]
        # if there is any non-numeric string in-between numeric string, take the first part of the numeric strings
        # take the first consecutive numeric string plus '+' and '-'
        
        if len(locs_org) == 1:
            # only one string is a number
            if mystr[locs_org[0]] in my_num_str and mystr[locs_org[0]] != '.':
                return int(mystr[locs_org])
            # only one string is a sign or '.', not convertable
            else:
                return 0
            
        for n in range(1, len(locs_org)):
            # if there is any non-numeric string in between the numeric string take the first consecutive numeric string
            if (locs_org[n]-locs_org[n-1])>1: 
                break_index = locs_org[n-1]+1     
                break
            # numeric strings are all right next to each other
            else:
                break_index = locs_org[n]+1                
        mystr = mystr[locs_org[0]:break_index] ## BY NOW, mystr is more than one element, ONLY CONTAIN CONSECUTIVE NUMERIC, SIGNS STRINGS
        

        # first two strings are all signs, or points not convertable
        if '..' in mystr[0:2] or '-+' in mystr[0:2] or '++' in mystr[0:2] or '--' in mystr[0:2]:
            return 0
        
        
        locs_point = [loc for loc, val in enumerate(mystr) if val in ['.']]  
        if len(locs_point) == 1: # only one fraction point
            return float(mystr)       
        elif len(locs_point) == 0:  # all numbers
            return int(mystr)
        
        elif  len(locs_point) > 1  :
        ?????????????? more than two fraction points
        # remove all the empty strings
        # mystr = mystr.replace(' ','')  # right now, there is only strings for numbers and '+', '-', '.'


        # looking for ONLY number string, but not signs
        locs = [loc for loc, val in enumerate(mystr) if val in my_num_str]  
        # numeric string not in presence, then not convertable, then return 0
        if not locs: 
           return 0
       
        if len(locs) == 1:
            # only one string is a number, location has to be in the first or the second in the string
            if (mystr[locs[0]] in my_num_str) and (mystr[locs[0]] != '.') and locs[0]<2:
                return int(mystr[0:locs[0]+1]) # include the one possible string before, it might be a sign string
            # only one string is a sign or '.', not convertable
            else:
                return 0
        
        for n in range(1, len(locs)):
            # if there is any non-numeric string in between the numeric string take the first consecutive numeric string
            if (locs[n]-locs[n-1])>1: 
                break_index = locs[n-1]+1  
                break
            # numeric strings are all right next to each other
            else:
                break_index = locs[n]+1                
        convert_str = mystr[locs[0]:break_index] ## BY NOW, mystr ONLY CONTAIN CONSECUTIVE NUMERIC, or '.'
        





              
        # WHEN WE KNOW THE STRING IS CONVERTABLE
        if mystr[0] == '-': # if the string before the first number is '-'
           sign = -1          
        else: 
            sign = 1           
        my_answer = int( float(convert_str)//1 ) * sign

        # the input has to be within the range [-2**31, 2**31-1]    
        if my_answer > 2**31 -1:
            my_answer = 2**31 -1
        if my_answer < -2**31:
            my_answer = -2**31
        
        return(my_answer)    
           
           
#%%

mystr = '+-2'
mystr = '          uyy -982'
mystr = '           -'
mystr = '42'
mystr = "4193 with words"
mystr = "words and 987"

mystr = "-91283472332"
mystr = " -+3.14159"
mystr = "  -0012a42"
mystr = " -42"

mystr = "0 -42"
mystr = "0-1"
#%%
answer = Solution()          
answer.myAtoi(mystr = mystr)         
           
           
    
#%%