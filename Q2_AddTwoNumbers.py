# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 20:52:52 2019

@author: Mingming

LeetCode Q2, Add Two Numbers
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
      
#%%       
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None        

class SLinkedList:
    def __init__(self):
        self.headval = None


l1 = ListNode(5)
e2 = ListNode(8) 
#e3 = ListNode(3) 
l1.next = e2
#e2.next = e3


l2 = ListNode(5)

l2 = ListNode(5)
ee2 = ListNode(6) 
ee3 = ListNode(4) 
l2.next = ee2
ee2.next = ee3



def listprint(self):
        printval = self.val
        print (printval)
        nextlist = self.next
        while nextlist is not None:            
            printval = nextlist.val
            print (printval)
            nextlist = nextlist.next
            
listprint(l1)
        
#%%
class Solution:
    def addTwoNumbers(self, l1, l2): 
            
            higher_digit = 0
            value1 = l1.val
            value2 = l2.val
            add_value = value1 + value2 + higher_digit
            if add_value >= 10:
               final_list   =  ListNode(add_value%10)  
               higher_digit =  1  # will be 1, if a+b is bigger than 10           
            else:    
                final_list  =  ListNode(add_value)
                higher_digit = 0            
            
            current_list = final_list
            nextlist1 = l1.next
            nextlist2 = l2.next
         
            # Stopping criteria
            while (nextlist1 != None) | (nextlist2 != None) | (higher_digit == 1) :            
                
                if nextlist1 != None :
                    value1 = nextlist1.val
                    nextlist1 = nextlist1.next
                else: 
                    value1 = 0
                    nextlist1 = None
                    
                if nextlist2 != None :
                    value2 = nextlist2.val
                    nextlist2 = nextlist2.next
                else: 
                    value2 = 0
                    nextlist2 = None

                add_value = value1 + value2 + higher_digit 
                
                if add_value >= 10:
                    current_list.next = ListNode(add_value%10)  
                    higher_digit  =  1  # will be 1, if a+b is bigger than 10                    
                else:    
                    current_list.next = ListNode(add_value) 
                    higher_digit = 0
                    
                current_list = current_list.next # update the current list

            return final_list       
                
                
final_list = Solution()                
hi = final_list.addTwoNumbers(l1, l2) 


#%%

def Linkedlist2list(LikedList):
        mylist = []
        mylist.append(LikedList.val)    
        nextlist = LikedList.next
        while nextlist is not None:            
            mylist.append( nextlist.val)
            nextlist = nextlist.next
        return mylist

mylist1 = Linkedlist2list(l1)
mylist2 = Linkedlist2list(l2)

# l1 = [2,4,3]        
# l2 = [7,0,8]



def addTwoNumbers(l1, l2):
    
    # who has the longer list, who determines length of for-loop, 
    # if same length, use the length they share    
    if len(l1) == len(l2):
        length = len(l1)   
        highest_digit = 0  # when two lists have the same length, they have the same length, 
                           # then set the highest_digit as 0
    elif len(l1) > len(l2):
        length = len(l2)
        highest_digit = l1[0]   # because the list has integers that are with reverse numbers
    
    elif len(l1) < len(l2):
        length = len(l1)
        highest_digit = l2[0]    
                           
    total_sum = 0   # store the final summation    
    for n in range(0, length):       
        (higher_digit, lower_digit)  = addTwoSingle(l1[n],l2[n])       
        total_sum += higher_digit*(10**(n+1))  +  lower_digit*(10**n)
        
    total_sum += highest_digit*(10**(n+1))  # if there is higher bit, don't forget to add it on
    
    return total_sum
 
    
def addTwoSingle(a,b):
    add_result = a+b
    lower_digit  =  add_result%10  
    higher_digit =  add_result//10  # will be 1, if a+b is bigger than 10
    
    return (higher_digit, lower_digit)    
    
    
total_sum = addTwoNumbers(mylist1, mylist2) 






   