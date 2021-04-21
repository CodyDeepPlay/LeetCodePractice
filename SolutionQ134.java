package LeetcodePractice;
import java.util.*;


public class SolutionQ134 {
	
	/* Solution 1:
	   Using a for loop to check first, which station should be a starting station
	   In order to be a staring station, it must meet gas[i]-cost[i]>=0.
	    	-if no starting station, return final result to be -1;
	    	-if find starting station, iterate to see if it can make back, to the starting station. 
	    	During the trip, the residual gas in the tank can not be less than 0. 
	 */
    public static int canCompleteCircuit(int[] gas, int[] cost) {
    	
    	int final_start = -1; // initialize the final answer to starting gas station
	
    	for (int n=0; n<gas.length;n++) {
    		
    		// for a starting station, the gas amount must be bigger or equal to the cost
    		// in order to make it a starting station
    	    if (gas[n]>=cost[n]) {
        		int investigate_start = n;  // currently, what is the starting gas station we are in
                int k = n; // start a new index to track in the while loop
        		int residual_gas = gas[n]-cost[n];
        		// starting circular iteration to conduct the trip
        		
        		while(residual_gas>=0) {
        			k +=1 ;                        // travel to next station
        			if (k>=gas.length) {k=0;}      // circular iteration
        			if (k==investigate_start) {
        				final_start=investigate_start;
        				return final_start;} // find the answer
        			residual_gas += gas[k]-cost[k];}	    	
    	    } 
	
    	}
	
       return final_start; 
       
    }
	
    
    /* Solution 2,
       -if overall difference summation between the gas and cost is negative,
       then it is not possible to conduct a round trip, return -1;
       
       - then investigate possible starting station, 
         if we iterate through all the gas station, make first gas station as possible starting station, 
         when we come across a negative residual gas (gas[i]-cost[i]), 
         then we will make next gas station as the new starting station, 
         and also reset the redisual gas as 0, and start to add (gas[i]-cost[i]) again. 
       
         By the time we iterate through all the gas stations, the updated starting gas station,
         is the answer. 

     */
	
    public static int canCompleteCircuit2(int[] gas, int[] cost) {
    	
    	int final_start = -1; // initialize the final answer to starting gas station
	    int [] diff_gas= {}; // initialize a new empty array
    	
	    // look at the difference between each gas station amount and the cost to travel to next station
    	for (int n=0; n<gas.length;n++) {    		
    		diff_gas = Arrays.copyOf(diff_gas, diff_gas.length +1);
    		diff_gas[diff_gas.length-1] = gas[n]-cost[n];
    	}
    	
    	int total_gas = Arrays.stream(diff_gas).sum();

    	// if the overall sum of diff gas is <0, then it is not possible to make a round trip
    	if (total_gas<0){return final_start=-1;}
    	
    	// if possible to make a round trip, 
    	// investigate possible starting point one-by-one,
    	else {
    		int residual_gas=0;
    		final_start = 0;
    		for (int n=0; n<gas.length;n++) {
    			residual_gas += gas[n]-cost[n];
    		    
    			// when residual gas is <0, reset next station as the starting station,
    			// also reset the residual gas amount
    			if (residual_gas<0) { 
    				final_start=n+1;
    				residual_gas = 0;}
    		}
    		return final_start;
    	}

       
    }
	
	
	     /**********************************************************
		 *                END OF MY SOLUTION                      *
		 *           Below are running my solutions               *
		 **********************************************************/
	    
	    public static void main(String arg[]) {
			

			int[] gas = {1,2,3,4,5}; int[] cost = {3,4,5,1,2};
			//int[] gas = {2,3,4}; int[] cost = {3,4,3};
			
			
			
			//System.out.println("My result is " + result);	
			

			int result = canCompleteCircuit2(gas, cost);
		    //secret.indexOf(guess.charAt(1));
			//String shorter=secret.substring(0,loc)+secret.substring(loc+1);
		
			//System.out.println(Arrays.toString(myList.toArray()));  // first need convert ArrayList into Array
			
		    //System.out.println(Arrays.toString(output));
			//System.out.println("My result is " + guess.charAt(0));
			//System.out.println("My result is " + guess.substring(1,3));
			System.out.println("My result is " + result);		
		


		}	
	

}
