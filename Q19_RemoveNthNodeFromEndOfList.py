# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 21:51:48 2019

@author: Mingming

Leet code problem 19, Remove Nth Node From End of List:

Given a linked list, remove the n-th node from the end of list and return its head.

Example:

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.

"""

# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    def removeNthFromBegin(self, head: ListNode, n: int) -> ListNode:
        '''
        remove the nth list from the begining of the list
        '''
        # want to remove the list at n stars from 1, 2, 3....
        if n-1 == 0:  # n-1, turn n into the index
            return head.next 
        
        # remove the list at n = 1 from the beginning
        if n-1 == 1:
           the_one_before_remove = head 
           the_one_to_remove     = head.next
           one_after_to_remove   = the_one_to_remove.next  # the one list after the one want to be removed       
           the_one_before_remove.next = one_after_to_remove # delete the given nth list, 
           return head

        # remove the list is located at after n=1      
        nextlist = head.next
        for i in range(1, n):
            if i == n-1:  # the list before the target removing one         
                the_one_before_remove = nextlist  
            
            nextlist = nextlist.next  # get the list for ith list,           
    
        the_one_to_remove     = nextlist       # the one list that want to remove
        one_after_to_remove   = the_one_to_remove.next  # the one list after the one want to be removed       
        the_one_before_remove.next = one_after_to_remove # delete the given nth list, 
        
        return head
    
    
    
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        '''
        remove nth list from the end of the list
        '''
        
        if head.next is None:  # if the current list is only has 1 layer, 
            return head.next   # after removal, it is empty
        
        count = 0
        nextlist = head.next
        # count how deep is this list
        while nextlist is not None:
            nextlist = nextlist.next
            count += 1
        total = count + 1  # add the last list to the total layer of linked list
        
        # want to remove the list at the first list, the last from the end
        if (total-n) == 0:
            return head.next
        
        # remove the list at n = 1 from the beginning
        if (total-n) == 1:
           the_one_before_remove = head 
           the_one_to_remove     = head.next
           one_after_to_remove   = the_one_to_remove.next  # the one list after the one want to be removed       
           the_one_before_remove.next = one_after_to_remove # delete the given nth list, 
           return head

        # remove the list is located at after n=1   
        nextlist = head.next
        for i in range(1, (total-n)):  
            if i == (total-n)-1:  # the list before the target removing one         
                the_one_before_remove = nextlist 
                #print(i)
            nextlist = nextlist.next  # get the list for ith list, 
    
        the_one_to_remove     = nextlist       # the one list that want to remove
        one_after_to_remove   = the_one_to_remove.next  # the one list after the one want to be removed       
        the_one_before_remove.next = one_after_to_remove # delete the given nth list, 
        
        return head
#%%

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None    

# print a linke list
def listprint(self):
        printval = self.val
        print (printval)
        nextlist = self.next
        while nextlist is not None:            
            printval = nextlist.val
            print (printval)
            nextlist = nextlist.next
                        
#%% examples


trial1 = ListNode(1)
trial2 = ListNode(2)
trial1.next = trial2

l2 = ListNode(5)
ee2 = ListNode(6) 
ee3 = ListNode(4) 
ee4 = ListNode(9)
l2.next = ee2
ee2.next = ee3
ee3.next = ee4


mysolution = Solution()   
listprint(trial1)             
begin = mysolution.removeNthFromBegin(trial1, 2)   
listprint(begin) 



mysolution = Solution()   
listprint(trial1)             
begin = mysolution.removeNthFromEnd(trial1, 2)   
listprint(begin) 
            
            
            