#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 21:16:55 2025

@author: mingmingzhang


Leetcode 215

Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Can you solve it without sorting?

"""

import random


class Solution:
    def yourSolution(self, nums, k ):
        '''
        !!! This method works when I tested on the simple cases,
        It will error out when the length of the list is very large, due to time limit is reached.
        
        The idea of this solution is as following:
            
        Create a empty dictionary to track the kth largest number,
            - each key is the given number instance in the list.
            - each value is the number of appearance of the instance.
        
        When the dictionary has less than the k numbers in it, simply add the new observation into
        the dictionary,
            - if the number is not a duplicate, simple add it in
            - if the number is a duplicate, find the key (the number value) and add 1 to the value
            of the key.
            - keep tracking the minimum value in this dictionary, which is the 
            Kth largest number observed as of now.
        
        When the dictionary has k numbers in it, stop tracking, for each given instance
            - if the current given number is smaller than or equall to the minimum, ignore
            - if the current given number is bigger, 
                ~ decrease the minimum (key) count (value) by 1, if the count (value) is zero,
                then remove this key-val. 
                ~ if the current given number is a new instance, just add it to the dict
                ~ if the current instance is in the dict, add 1 to its key related value
        
        '''
        
        
        n = len(nums)
        k_dict = {}  # create a list tracking the k largest number
        min_  = nums[0]  # track the minimum numbre in the k largest list, initialize with the first number in the input list
        total_track = 0
        
        for i in range(0, n):
            #print("nums[i] is ,",  nums[i])
              
            if total_track!=k:         
                #print("nums[i] is ,",  nums[i])
                total_track = total_track + 1              
                # track duplicate
                if nums[i] in k_dict:           
                    k_dict[nums[i]] = k_dict[nums[i]] + 1     
                # track non-duplicate
                elif nums[i] not in k_dict:                         
                    k_dict.update({nums[i]:1})  # add this number into k largest number
                    
                min_ = min(min_ ,nums[i])  # update the minimum number in the k_list
                #print("I am in step1")
             
            # if we already tracked kth largest value in the dict
            # just do the comparison
            elif total_track == k: 
                #print("nums[i] is ,",  nums[i])
             
                # for a given number that has never seen before            
                if nums[i] <= min_: pass  # smaller than my minimum, don't care
                elif nums[i] > min_:   # bigger than my minimum, 
                        
                    if nums[i] not in k_dict: 
                        k_dict.update({nums[i]: 1}) # add the newly founded member, one of the kth largest number
                    elif nums[i] in k_dict:     
                        k_dict[nums[i]] = k_dict[nums[i]] + 1  
                        
                    # prepare to adjust my minimum
                    k_dict[min_] = k_dict[min_] - 1 
                    # check if min_ is with 0 instance, if so, remove it from the dict
                    if k_dict[min_] == 0:
                        k_dict.pop(min_)  # remove the old smallest number
                      
                min_ = min(k_dict.keys()) # update the latest minimum of the kth largest number
               # print("I am in step2")
            #me = 0
        
        return min_
        



import heapq

class Solution:
    def yourSolution(self, nums, k ):
        '''
        Use a heap (tree based data) structure in python.
        
        using the MAX heap to solve it.
        
        If we can build the max-heap, at each level of the node, the number
        will be the maximum compare to any other number in the heap below that node.
        
        
        Because python heap implementd a minimum heao data structure, so we need to 
        make all the elements the negative of itself.
        
        
        Algs time complexity is O(n + Klogn)
        n is the operation to take the entire arary into a heap.
        Then, each time tranverse the heap, we need log(n) because the size of the heap is n.
        We have to pop the heap for K times. 
        

        '''
        
        for i in range(len(nums)):
            nums[i] = - nums[i]
        
        heapq.heapify(nums) # convert the list into a heap data structure
        
        for j in range(k-1):
            heapq.heappop(nums)  # pop k-1 times
        
        return -heapq.heappop(nums) # pop kth time
        
        
        
class Solution:
    def yourSolution(self, nums, k ):
        
        '''
        Keep build the minimum heap, and only keep k element in the heap,
        
        When it iterate through all the elements, then the top one in the heap is the 
        answer, since the min heap keeps poping the smallest element. 
        
        Algs time complexity is O(N*logK)
        for each heap, we need to use logK, because our heap data only keeps k number
        and we need to iterate through all the array elements. 
        
        '''

        my_heap = [nums[0]]
        
        heapq.heapify(my_heap) # build the defaul heap
        count = 1  # the default heap has one element
        for i in range(1,len(nums)):
            
            print(i)
            
            # if my heap has less than k elements yet, keep adding element
            if count <k:
                heapq.heappush(my_heap, nums[i])
                count +=1
                
            # if the heap has k elements now, just keep the same amount of elements    
            elif count == k:
                heapq.heappush(my_heap, nums[i])  # add the latest element
                heapq.heappop(my_heap)      # remove the top (minimum) element
                 
                
        return heapq.heappop(my_heap)  
      
    

        
class Solution:
    def yourSolution(self, nums, k ):
        '''
        using Quick Select algorithm
        !!! this implementation here has run-time error when submission online.
        
        1) First, randomly pick a value as the pivot, then partition the array so that 
        
        Anything on the left side of the pivot is smaller than,
        and anything on the right side of the pivot is bigger. 
        
        2) Define the lower pointer L: 
            start from index 0, when the corresponding value is smaller than the pivot,
            increase the pointer to next value; When the corresponding value is bigger than
            pivot, stop.
        
        3) Define the higher pointer H: 
            start from the last index, when the corresponding value is bigger than the pivot, 
            decrease the pointer to next value; when the corresponding value is smaller than
            pivot, stop. 
            
        4) Then, swap the L and H corresponded value. then continue to scan. 
        
        5) When the L>=H, stop   
            swap the pivot wit the end index
        
        
        When the pivot pointer is equal to the (n-k), that is the value we need.
        
        
        Average time complexity O(n)

        '''
  
        def partition(nums, L, H):        
            # randomly pick the first element as the pivot, you can pick any value as the pivot
            start = L
            last = H
            pivot_index = L
            pivot = nums[pivot_index]  # randomly pick the first element as the pivot,         
            
            while start< last:                    
                # increase the lower pointer until find bigger than pivot value
                while nums[start] <= pivot:  
                    start = start + 1
                    if start == n-1: break  # reach the last data point
                # decrease the lower pointer until find the smaller than pivot value
                while nums[last] > pivot:
                    last = last - 1 
                    if start == 0: break  # reach the first data point
                
                if start<last:
                    # after find the bigger value that in the lower bound L
                    # and the smaller value that in the higher bound H
                    # swap the value
                    temp = nums[start]
                    nums[start] = nums[last]   
                    nums[last] = temp
                      
            # swap the pivot value with the higher end index corresponding value
            temp = nums[last]
            nums[last] = pivot
            nums[pivot_index]=temp 
            
            loc = last  # update pivot index, loc is the latest pivot index    
            return (nums, loc, L, H) # return the update pivot index, the current L and H that for the current sorted array
        
        
        n = len(nums)
        L = 0   # track the lower index, to find value that is bigger than pivot
        H = n-1 # track the higher index, to find value that is smaller than pivot       
        target_loc = n - k  # kth largest value will have its corresponding index n-k in a sorted array
        loc = None #        
        # recursively partion the array 
        # each time, only partition the portion of the array, where it has the target index location
        # we are looking for
        while loc != target_loc:
            
            (nums, loc, L,  H) = partition(nums, L, H)
            # the target val we are looking for is on the higher side of the current pivot
            if loc < target_loc:      L = loc+1; H = H;
            elif  loc > target_loc:   L = L;     H = loc-1;   
        
        target = nums[loc]     
        return target







        
class Solution:
    def yourSolution(self, nums, k ):
        '''
        using Quick Select algorithm
        redefine the partition function above
        When the pivot pointer is equal to the (n-k), that is the value we need.

        Average time complexity O(n)

        '''
  
        def partition(nums, left, right, pivot_index):
            
            pivot = nums[pivot_index]  # get the pivot value
            # put the pivot value at the very end of the array
            # so we can work on sorting the rest of the array
            nums[pivot_index], nums[right] = nums[right], nums[pivot_index]
            
            # initialize the lowest index to host lower values
            stored_index = left
            for i in range(left, right):
                 # if my current value is samller than pivot
                if nums[i] < pivot:
                    # swap the current value to the value saved in stored index place
                    nums[i], nums[stored_index] = nums[stored_index], nums[i]
                    stored_index += 1 # if swap happens, move-up the index one more clip
               
            # when done with moving smaller than pivot values to the lower end of the array
            # the last step is to make the pivot swap back to the stored index
            #   now the left of the pivot is all smaller, the right of the pivot is all larger        
            nums[right], nums[stored_index] = nums[stored_index], nums[right]
            
            return nums, stored_index
                
        
        n = len(nums)
        L = 0   # track the lower index, to find value that is bigger than pivot
        H = n-1 # track the higher index, to find value that is smaller than pivot       
        target_loc = n - k  # kth largest value will have its corresponding index n-k in a sorted array
        loc = None #        
        # recursively partion the array 
        # each time, only partition the portion of the array, where it has the target index location
        # we are looking for
        while True:
            pivot_index = random.randint(L, H)
            nums, loc = partition(nums, L, H, pivot_index)
            # the target val we are looking for is on the higher side of the current pivot
            if  loc == target_loc: return nums[loc]  
            elif loc < target_loc:    L = loc+1; H = H;
            elif  loc > target_loc:   L = L;     H = loc-1;   
        
  




#%%



#nums = [3,2,1,5,6,4]
#k = 2    #Output: 5



nums = [3,2,3,1,2,4,5,5,6] 
k = 4      #Output: 4


#nums =[2,1]
#k =2  # output =1 

#nums=[-1,2,0]
#k =2   #Output: 0

results = Solution()
output = results.yourSolution(nums, k)      
print(output)




#%%

nums = [6,5,3,2,1,4]

def partition(nums, left, right, pivot_index):
    
    pivot = nums[pivot_index]  # get the pivot value
    # put the pivot value at the very end of the array
    # so we can work on sorting the rest of the array
    nums[pivot_index], nums[right] = nums[right], nums[pivot_index]
    
    # initialize the lowest index to host lower values
    stored_index = left
    for i in range(left, right):
         # if my current value is samller than pivot
        if nums[i] < pivot:
            # swap the current value to the value saved in stored index place
            nums[i], nums[stored_index] = nums[stored_index], nums[i]
            stored_index += 1 # if swap happens, move-up the index one more clip
       
    # when done with moving smaller than pivot values to the lower end of the array
    # the last step is to make the pivot swap back to the stored index
    #   now the left of the pivot is all smaller, the right of the pivot is all larger        
    nums[right], nums[stored_index] = nums[stored_index], nums[right]
    
    return stored_index
        
        
 
left, right = 0, len(nums)-1
pivot_index = 0


stored_index, nums =  partition(nums, left, right, pivot_index)   

    
pivot_index = 2
stored_index, nums =  partition(nums, left, right, pivot_index)           
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        






  