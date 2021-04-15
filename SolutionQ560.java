package LeetcodePractice;

import java.util.HashMap;
import java.util.Map;

public class SolutionQ560 {
	
	
	/*
	 * Given an array of integers nums and an integer k, 
	 * return the total number of continuous subarrays whose sum equals to k. */
	
	
	
    public static int subarraySum(int[] nums, int k) {

    	int curSum = nums[0];
    	int count=0;
    	int drop_begin = 0;
    	
    	for (int i=0;i<nums.length-1;i++) {
    		
    		
    		
    		if(nums[i]==k) {count++;}  // compare all the individual element to the target
    		
    		if (curSum==k) {
    			count++;
    			curSum -= nums[drop_begin]; // when it equals, also remove the first element in this continuous array
    			drop_begin++;          //update the beginning index in the new continuous array
    			curSum +=nums[i+1];}// don't forget to add next element

    		else if (curSum>k) {curSum=0; drop_begin=i; curSum +=nums[i+1];} 		
    		else if (curSum<k) {curSum +=nums[i+1];}
    		//count++;    		
		
    	}
    	
    	if (curSum==k) {count++;}  // the last value
    	
    	
    	return count;
    	
    }
	
    
    
    public static int subarraySumBruteForce( int[] nums, int k) {
    	
    	int count =0;
    	for (int start=0;start<nums.length;start++) {
    		for (int end=start+1;end<=nums.length;end++) {
    			int curSum = 0;
    			for (int i=start;i<end;i++) 
    				curSum +=nums[i];
    			if (curSum==k) 
    				count++;  				
    		}
    	}
        	
    	return count;
    	
    	
    }
    
    
    
    public static int subarraySumCusum( int[] nums, int k) {
    	
    	int count=0;		
    	int start, end;
    	int [] cusum= new int[nums.length+1]; // store cusum
    	cusum[0] =0;
    	int curSum =0;
    
    	for (start=0; start<nums.length;start++) { 		
    		for (end=start+1;end<=nums.length;end++) {
    			cusum[end]=cusum[end-1] + nums[end-1];
    			
    			curSum = cusum[end]-cusum[start];
    			if (curSum==k) count++;
    			
    		}		
    	}
    	    	
    	return count;
    		
    }
    
    
    
    
    /*Solution 2, use the hashable map to trace the complement values*/
    public static int subarraySumCusum_hashmap(int[] nums, int k) {
        /*create a hashmap which is used to store the cumulative sum up to all indices, and 
         * with the times the same sum occurs*/
    	Map<Integer, Integer> map = new HashMap<>();
    	/* put zero complement result into the map, complement value is the "key", and the count 1 is the "value "in map，
    	 * this 0 complement helps to track whether each individual element is equal to the given k value or not.
    	 * */
    	map.put(0, 1);  
    	
    	int cuSum = 0;  // make cumulative sum the first element is zero
    	int res = 0;    // tracking the final results
    	for (int i=0;i<nums.length;i++) {
    		cuSum +=nums[i];   // cuSum add an new element in each iteration 		
    		if (map.containsKey(cuSum-k)) { // if the cuSum complement is in the map
    			res+= map.get(cuSum-k);    // then results will add 1 more count
    		} 
    		
    		/* if there is no "cuSum" key in the map, then set it is value to be 0
    		 * when try to put "cuSum" key, if there is already in it, add it is value one more time
    		 * */
    		map.put(cuSum, map.getOrDefault(cuSum,0)+1); // combine the counts for the same cuSum
    		// in the map, cuSum serves as the key, one key can only have one value in the map. So
    		// when have multiple cuSum happens, we need to add its value with 1 in the map.
    	}
	   	
        return res;
       
    }
    
    
    
    
    
    
	
	
	public static void main(String arg[]) {
		
	//int[] nums = {1,2,3}; int k=3;
	//int[] nums = {1,1,1}; int k=2;
	int[] nums = {-1,-1,1}; int k = 0;
		
	int result = subarraySumCusum_hashmap(nums, k);
	System.out.print(result);
	
		
	}
	
	

}
