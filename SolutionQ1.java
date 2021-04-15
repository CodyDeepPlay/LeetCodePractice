package LeetcodePractice;
import  java.util.*;

/*Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
 * */

public class SolutionQ1 {
		
	
	/* solution 1: 
	 * 	- make the given array sorted first
	 *	- using two pointers, one at the beginning and one at the end to trace the values
	 *		the beginning pointer will increase or the end pointer will decrease depends on the 
	 *		sum value of the two pointers compared to the given target value*/
	
    public static int[] twoSum(int[] nums, int target) {
    	
    	   	
    	int[] output = new int[2];
    	
    	int[] sorted_nums = Arrays.copyOf(nums, nums.length); // make a copy of the array, so that we don't change the original copy
    	Arrays.sort(sorted_nums);
    	
    	int head = 0;
    	int tail = nums.length-1;
    	// the two parts of the values that sum equal to the target
    	int target1=0;
    	int target2=0;
    	
    	boolean target1Found = false;
    	boolean target2Found = false;

    	// in the sorted array, find the two values that sums equal to the target
    	while (head<tail) {
    		int curSum = sorted_nums[head] + sorted_nums[tail];
    		if      (curSum>target) {tail -=1;}
    		else if (curSum<target) {head +=1;}
    		else {target1 = sorted_nums[head];
    			  target2 = sorted_nums[tail];
    			  break; // when find the solution, break the loop
    			}    		   	
    		}	
    	
    	// retrive the index of the found values in the original array
    	for (int i=0; i<nums.length;i++) {
    		if (nums[i]== target1 && target1Found == false) {
    			output[0]=i;
    			target1Found = true; 	
    		}// non-zero index, starting from 1
    		else if (nums[i]== target2 && target2Found == false) {
    			output[1]=i;
    			target2Found = true;
    			}
    		}
    	

    	Arrays.sort(output);  // the question requires sort the final answer
    	
    	return output;
        
    }

    
    /*Solution 2, use the hashable map to trace the complement values*/
    public static int[] twoSum_map(int[] nums, int target) {
    	
	   	
    	int[] output = new int[2];

    	Map<Integer, Integer> indexMap= new HashMap<>();  // create a hashmap
    	
    	for (int i=0; i<nums.length;i++) {
    		int complement=target-nums[i];
    		if (indexMap.containsKey(complement)){  // if indexMap already contain the complement, then that is the solution
    			output[0] = i;
    			output[1] = indexMap.get(complement); //get the value in nums(key in map) related index (value in map)
    			break;
    		}
    		else {
    			indexMap.put(nums[i], i); // add a key-value pair into the hashMap.
    		}
    	}

    	Arrays.sort(output);  // the question requires sort the final answer    	
    	return output;
        
    }
    
    
    
    
    
    public static void main(String args[]) {
    	
    	int[] output = new int[2];
    	int[] nums = {2,7,11,15};
    	int target = 9;
    	
        output=twoSum(nums, target);
        System.out.println(Arrays.toString(output));

    
    	int[] nums1 = {3,3};
    	int target1 = 6;
    	
        output=twoSum(nums1, target1);
        System.out.println(Arrays.toString(output));
        
    
    	int[] nums2 = {2,5,5,11};
    	int target2= 10;
    	
        output=twoSum_map(nums2, target2);
        System.out.println(Arrays.toString(output));
        
    }
    
    
    
}
