package LeetcodePractice;

import java.util.*;

public class SolutionQ217 {

	/* Solutino 1: use hashmap with one for loop */
	public boolean containsDuplicate(int[] nums) {
        
    	boolean output=false;
        
        Map<Integer, Integer> myMap = new HashMap<>();
        int n = nums.length;
        
        for (int i=0; i<n; i++) {
        	
        	if(myMap.containsKey(nums[i])) {
        		output = true; return output;
        	}
        	else {myMap.put(nums[i], i);}
        	
        }
        
        return output;
	}
        
      /*Solutino 2: use set to compare if the set size is array length
       * If set size and array length are the same, then there is no duplicate,
       * then there is duplicates*/  
       public boolean containsDuplicate2(int[] nums) {
           

    	   /*
           Set<Integer> mySet = new HashSet<>();
           //mySet.addAll(Arrays.asList(nums)); 
           //mySet.addAll(Arrays.asList(nums));    
           Collections.addAll(mySet, nums);
           if (mySet.size() == nums.length){return false;}
           else{return true;}
           
           */
           return true;
       }
        
        


}
