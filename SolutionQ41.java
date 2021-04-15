package LeetcodePractice;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;



public class SolutionQ41 {
	
	/*
	 * Given an unsorted integer array nums, find the smallest missing positive integer.
	 * 
	 * Input: nums = [1,2,0]
	   Output: 3
	   
	   Input: nums = [3,4,-1,1]
	   Output: 2
	   
	   Input: nums = [7,8,9,11,12]
	   Output: 1
	   
	 * */
	
	
	
    public static int firstMissingPositive(int[] nums) {
        
        /* Use HashMap to track the results
         
         First, 0 or negative values will not affect our results, as the solution is looking for the 
         smallest POSITIVE missing number.  
          
         !!! Each time, when iterate through the array, if the element is the same as smallest missing int,
         then the smallest missing int should be updated with 1.
         
         !!! At the same time, a Map is created to store the element of the array for every iteration. 
         
         !!! After the smallest missing int is updated, we need to check if the smallest missing int 
         is in the Map or not. 
         	- If it is in the Map, because this higher values may appear before, due to unsorted array
         	Then, we need to continue update the smallest missing int with 1, until we no longer see it is 
         	the Map. 
         	- If it is not in the Map, move to next iteration
          
         By the end of the iterations, we have find our answer.
          
         * */
        
    	int smallest_int=1; // by default, the smallest int is 1. 
    	Map <Integer, Integer> myMap = new HashMap<>();

    	for (int n=0; n<nums.length;n++) {
    		
    		// only investigate elements that are bigger than 0
    		// values are smaller than or equal to 0 is not affecting the results
    		if(nums[n]>0) {    			
    			// key is the value of int array, value is the index of array
    			myMap.put(nums[n], n);  
    			
    			// if current value is the same as smallest_int, then lift the smallest_int by 1
    			if (nums[n]==smallest_int) {smallest_int +=1;}
    			
    			// if the smallest_int is already in the traking map, then update the smallest_int with 1
    			// until the smallest_int is no longer in the map
    			while (myMap.containsKey(smallest_int)) { smallest_int +=1; }

    		}
	
    	}
        
    	return smallest_int;
    }
	
    
    
    /**********************************************************
	 *                END OF MY SOLUTION                      *
	 *           Below are running my solutions               *
	 **********************************************************/
    
    public static void main(String arg[]) {
		
		int[] nums = {1,2,0};
		//int[] nums = {3,4,-1,1};
		//int[] nums = {7,8,9,11,12};
		
		
		int result = firstMissingPositive(nums);
		
		

		//System.out.println(Arrays.toString(myList.toArray()));  // first need convert ArrayList into Array
		
	    //System.out.println(Arrays.toString(output));
		System.out.println("My result is " + result);
				
	
	}	
    
    

}
