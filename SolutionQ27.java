package LeetcodePractice;
import java.util.*;

public class SolutionQ27 {
	/*Given an array nums and a value val, 
	 * remove all instances of that value in-place and return the new length.
	 * Do not allocate extra space for another array, 
	 * you must do this by modifying the input array in-place with O(1) extra memory.*/
	
	
	
	/*when it is the value to keep, move this value into the pointer location starting from 0, and then increment by 1*/
    public static int removeElement(int[] nums, int val) {
    	
    	//int result=0;
    	int cur_loc_idx=0;  // used to indicate where to put my current value
    	int temp;  // set a temperory buffer to hold the data
    	for (int i=0; i<nums.length;i++) {
    		if (nums[i]!=val) {
    
    			//result++; // if the current value is the one to preserve, then put it into the beginning, and swap this value to that value
    			temp = nums[cur_loc_idx];
    			nums[cur_loc_idx] = nums[i];
    			nums[i]=temp;
    			cur_loc_idx++;
    			
    		};
    	}

    	return cur_loc_idx;
    	
        
    }
    
    
   /*when it is the value to remove, replace the current value with the last value in the array*/ 
   public static int removeElement2(int[] nums, int val) {
    	
	    int i = 0;
	    int n = nums.length;
	    while (i < n) {
	        if (nums[i] == val) {
	            nums[i] = nums[n - 1];
	            // reduce array size by one
	            n--;
	        } else {
	            i++; 
	        }
	    }
	    return n;
    	
        
    }
    
    
    
    public static void main(String arg[]) {
    	
    	int [] nums = {3,2,2,3}; 	int val=3;
    	//int [] nums = {0,1,2,2,3,0,4,2}; int val=2;
    
    	int result = removeElement2(nums, val);
    	
    	System.out.println(result);
    	System.out.println(Arrays.toString(nums));
    	
    }
	
	

}
