package LeetcodePractice;

import java.util.*;

class SolutionQ167 {
	
	/*Leetcode practice 167, Two Sum II, input array is sorted*/
	
	/*use the complement to solve the problem*/
    public static int[] twoSum(int[] numbers, int target) {
    	
    	Hashtable<Integer, Integer> indexMap = new Hashtable<>(); // create a new Hashable table
    	int a_number;                // define a integer variable to store the value in the numbers array 
    	int[] output = new int[2];   // define an integer array, with a length of 2
    	
    	// for each value in the "numbers" int array, 
    	for (int i =0; i<numbers.length; i++) {
    		int complement_num = target-numbers[i];  // find the complement value for a given value in the numbers array.
    		
    		/* in this hashable table, design to put values in the "numbers" array as index in the table, and the 
    		 * index of "numbers" array as the values in the hashable table. 
    		*/
    		Enumeration myVlaues= indexMap.keys();  // get all the keys in the hashable table, this will be used to store all the values in the "numbers" array
      		while(myVlaues.hasMoreElements()) {     // this function will return True while there are still more elements to extract
    			a_number = (Integer) myVlaues.nextElement();  //  get the next element in this enumeration, convert it into integer, as a_number is defined as integer
    	        
    			/*if complement number is the current element of the enumeration, then we find the solution.
    			 * that is */
    			if (complement_num==a_number) {
    	        	output[0] = indexMap.get(complement_num)+1; // the question requires non-zero index, so plus 1. 
    	        	output[1] = i+1;                            // the question requires non-zero index, so plus 1. 
    	        	Arrays.sort(output);  // the question requires index1 is lower than index2. 
    	        	break;    	          // when find the solution, no need to continue
    	        }
    	      }  
    		
   		
    		indexMap.put(numbers[i], i); // put the the values in "numbers" as key, and index in "numbers" as value in the hashable table
    	}
    	return output;
    
    }
    
    
    
    /*use two pointers to solve the problem*/
    public static int[] twoSum2(int[] numbers, int target) {
    	
    	int[] output = new int[2];   // define the output as a two element array
    	int head=0;                  // track the pointer at the beginning
    	int tail=numbers.length -1;  // track the pointer at the end
    	while (head<tail) {          
    		int curSum = numbers[head] + numbers[tail]; // sum the two values together pointed by the pinter
    		if      (curSum > target) {tail -=1;}            // if the sum value is bigger than the target, then move the end pointer toward the beginning
    		else if (curSum < target) {head+=1;}
    		else { 
    			output[0]=head+1; 
    			output[1]= tail+1;
    			return output;
    		    }
    		
    	}
    	return output;
    
    
    }
    
    

    
    public static void main(String args[]) {
    		
    	int[] output = new int[2]; // initiate an array with the size of 2
     	
    	int [] numbers = {2,7,11,15};  // when you have numbers, how to create the array
    	int target = 9;    	
    	output  = twoSum(numbers, target);
    	System.out.println(Arrays.toString(output)); // Arrays.toString(in[]) method returns a string representation of the contents of specified array 
        	
    	int [] numbers2 = {2,3,4}; 
        int target2 = 6;        
    	output  = twoSum(numbers2, target2);
    	System.out.println(Arrays.toString(output)); // Arrays.toString(in[]) method returns a string representation of the contents of specified array 
     	
        int [] numbers3 = {-1,0};
        int target3 = -1;     
    	output  = twoSum2(numbers3, target3);
    	System.out.println(Arrays.toString(output)); // Arrays.toString(in[]) method returns a string representation of the contents of specified array 
 
    	   
    
    }
    	
    	
    
    	
    	
    	
    
}