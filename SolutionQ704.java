package LeetcodePractice;

import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;
import java.lang.Math;

public class SolutionQ704 {
	
	/*
	 * Given a sorted (in ascending order) integer array nums of n 
	 * elements and a target value, write a function to search target in nums. 
	 * If target exists, then return its index, otherwise return -1.*/
	
	
	
	/*Solution1, 
	 * conduct the search using a for loop*/
    public static int search(int[] nums, int target) {
    	
    	int output = -1;   	
    	for (int i=0; i<nums.length;i++) {
    		
    		if (nums[i]== target) {output=i;break;} 		
    	}  	
    	return output;
        
    }
    
    
    
    /*Solution2, binary search
     * there is a start_idx, end_idx, mid_idx*/
    
    public static int search_binary(int[] nums, int target) {
    	
    	int output    = -1;   
    	int start_idx = 0;
    	int end_idx   = nums.length-1;
    	int mid_idx   = Math.round((start_idx+end_idx)/2); // mid index of ascending array
    	    	
    	/**/
    	while ((end_idx-start_idx)>2) {

        	if      (nums[start_idx]==target) {output=start_idx;return output;} 
        	else if (nums[mid_idx]==target)   {output=mid_idx;return output;} 
        	else if (nums[end_idx]==target)   {output=end_idx;return output;} 
        	 
        	// the target is bigger than the mid_idx element, move end_idx to the mid_idx
    		if (nums[mid_idx]>target) {   			
    			end_idx = mid_idx;
    			mid_idx = Math.round((start_idx+end_idx)/2);}
    		
    		// the target is smaller than the mid_idx element, move start_idx to the mid_idx
    		else if (nums[mid_idx]<target) { 
    			start_idx = mid_idx;
    			mid_idx = Math.round((start_idx+end_idx)/2); }
    		}
    	    		
     	if (nums[start_idx]==target)    {output=start_idx;} 
    	else if (nums[mid_idx]==target) {output=mid_idx;} 
    	else if (nums[end_idx]==target) {output=end_idx;} 
    	
    	return output;
        
    }
    
    
    /*solution 3, brute search in hashable map*/
    
    public static int search_hash(int[] nums, int target) {
        int output = -1;
        //int[] output_array = new int[1]; 
        Map<Integer, Integer> idx_map = new HashMap<>();
     
        
        for (int i=0;i<nums.length;i++) {
        	idx_map.put(nums[i], i);
            
        	if (idx_map.containsKey(target)){
        		output = idx_map.get(target);}	      	
        }
    	
    	return output;
    }
    
    
    
    
    public static void main(String arg[]) {
    	
		int output; 
		
		int[] nums = {-1,0,3,5,9,12};
		int target = 9;
		
		output = search_hash(nums,target);
		
		int[] print_output = new int[1];
		print_output[0] = output;
		
		System.out.println(Arrays.toString(print_output));
	   
		
		int[] nums1 = {-1,0,3,5,9,12};
		int target1 = 4;
		
		output = search_hash(nums1,target1);
		print_output[0] = output;	
		System.out.println(Arrays.toString(print_output));
    	
    	
    }
    
    
	

}
