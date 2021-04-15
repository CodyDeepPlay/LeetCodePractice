
package LeetcodePractice;
import java.util.*;


public class Solution {
	
	
	
	/* Q274
	 * Solution 1
	 * 1. sort the array 
	 * 2. when during loop for comparison, get the element from high to low
	 * 3. each time, if the new element if higher than current hindex, the hindex + 1. 	
	*/
    public int hIndex(int[] citations) {
        int n=citations.length;
    	int hindex = 0;
    
    	Arrays.sort(citations);
    	for(int i=0;i<n;i++) {
    		
    		// reverse the input array, starting to compare the last one
    		if (citations[n-i-1]>hindex) {
    			hindex +=1; } 		
    	}  		
    	return hindex;	 
    }

    // for loop again,
    // because the array has been sorted, so loop from biggest to smallest, 
    // when in a loop value, the citation value < (index+1), we break the loop
    // and previously, the last citation >= index+1, where the (index+1) at that time is the solution hindex
    public int hIndex0(int[] citations) {
        int n=citations.length;
    	int hindex = 0;
    
    	Arrays.sort(citations);

    	for (int i=0;i<n;i++) {
    		
    		//current_hindex = n-i; // reverse the index, 
    		if (citations[n-i-1]>= i+1) {hindex = i+1;}
    		if (citations[n-i-1]< i+1) {break;}

    	}
    	
    	return hindex;	 
    }
 
    
    
    
	/* Q274
	 * Solution 2
	 * 1. sort the array 
	 * 2. use binary search to look for H index, 
	 * 	at a certain location, when the citation is bigger than the location, 
	 * 	then the location is a hindex. 	
	*/
    public int hIndex2(int[] citations) {
    	
    	
        int n=citations.length;
    	int hindex = 0;
        
    	if (n==0) {return hindex=0;} // when there is only 1 paper, and no citation
    	if (n==1 & citations[0] !=0) {return hindex=1;} // where there is only 1 paper, and this paper with some citation
	    if (n==2) { 
	    	if (citations[0]>=2 & citations[1]>=2) {return hindex =2;}
	    	else if (citations[0]==0 & citations[1]==0) {return hindex=0;}
	    	else {return hindex=1;}
	
	    }
    	
    	Arrays.sort(citations);
    	int left=0, middle=0, right=n-1;  // define the two end index for binary search
    	int new_left=left, new_right=right;
    	//int middle = (left+right)/2;   // by default, java is doing round for int divide
    	// if there is at least one element that is not zero
    	if (citations[left] !=0 || citations[right] !=0 ) {hindex=1;}
    	
    	
    	do {
    		// update possible new left and right index
    		left = new_left; right = new_right; 
    		// the middle index of binary search
    		middle = (left+right)/2;   // by default, java is doing round for int divide
    		int possible_hindex = n-middle; // if this one is the solution, what is the possible hindex right now
    		
    		if (citations[middle]==possible_hindex) {
    			 hindex = possible_hindex;
    			 break;}
    		else if (citations[middle]>possible_hindex) {
    			hindex = possible_hindex;
    			new_right = middle;}  // move left   
    		else if (citations[middle]<possible_hindex) {
    			new_left = middle;} // move right  	
    		//middle = (left+right)/2;   // by default, java is doing round for int divide
    		
    	} while (middle != right && middle != left);
    
    	
    	return hindex;	 
    	
    	
    }
    
   
    /*Another solution, binary search
     *  first sort citations from low to high, from left to right
     *  1. special case when length of citations is 0 or 1.
     *  2. binary search when length of citations is 2
     *     start with citations[0] or citations[n-1] if non-zero, hindex=1 start with
     *  
     * 		possible_hindex            n          n-1     ...               2,               1
     * 		          index            0            1     ...             n-2,             n-1
     *  	citation values  citations[0] citations[1]    ...   citations[n-2]   citations[n-1]       
     *      then binary search start with L=0, R=n-1, M =(R+L)/2, in Java, it is rounding
     *      a, if citations[M] == its possible_hindex, job is done, this is hindex we are looking for                       
     *      b, if citations[M] >= its possible_hindex, update hindex = possible_hindex, moving left, make R=M, 
     *      c, if citations[M] < its possible_hindex,  no update hindex, moving right, making L=M
     *      
     *      Stopping criteria, at new calculation M =(R+L)/2, either M==R or M==L, stop the iteration.
     * 
     * */
   public int hIndex22(int[] citations) {
    	
    	
        int n=citations.length;
    	int hindex = 0;
        
    	if (n==0) {return hindex=0;} // when there is only 1 paper, and no citation
    	if (n==1 & citations[0] !=0) {return hindex=1;} // where there is only 1 paper, and this paper with some citation

    	Arrays.sort(citations);
    	int left=0, middle=0, right=n-1;  // define the two end index for binary search
    	int new_left=left, new_right=right;  // used to track new possible index
    	// if there is at least one element that is not zero
    	if (citations[left] !=0 || citations[right] !=0 ) {hindex=1;}
    	
    	
    	do {
    		// update possible new left and right index
    		left = new_left; right = new_right; 
    		// the middle index of binary search
    		middle = (left+right)/2;   // by default, java is doing round for int divide
    		int possible_hindex = n-middle; // if this one is the solution, what is the possible hindex right now
    		
    		if (citations[middle]==possible_hindex) {
    			return hindex = possible_hindex;}
    		else if (citations[middle]>possible_hindex) {
    			hindex = possible_hindex;
    			new_right = middle;}  // move left   
    		else if (citations[middle]<possible_hindex) {new_left = middle;} // move right  	

    	} while (middle != right && middle != left);
    	
    	return hindex;	 
    	
    	
    }
    
    
    /* Q274 
     * Solution 3
     * Use two for loop to solve this problem
     *1. create a separate array to store all possible hindex 
    */
    public int hIndex3(int[] citations) {
        int n=citations.length;
    	int [] hindexList = new int[n];  // all the possible hindex the given citations could have	
    	int hindex=0;
    	
    	for (int i=0; i<n;i++) {
    		// for a citations, add 1 for all the hindex locations, 
    		// the upper limit is the smaller value of current citation or n
    		for (int hloc=0; hloc< Math.min(citations[i],n);hloc++) {
    			hindexList[hloc] +=1;  		
    			// when a given citation track match hindex definition
    			if (hindexList[hloc]>hloc) {
    				hindex = (hloc+1>hindex)?hloc+1:hindex; }	
    		}
    	}
    	return hindex;	 
    
    }

    
    /*Q220  Contains Duplicate III
     * 
     * Given an array of integers, find out whether there are two distinct indices 
     * i and j in the array such that the absolute difference between nums[i] and nums[j] 
     * is at most t and the absolute difference between i and j is at most k.
     * */
    public boolean containsNearbyAlmostDuplicate(int[] nums, int k, int t) {
        

        int n=nums.length;
        
        for (int i=0; i<n;i++){
            
            for (int j=0; j<n;j++){
                if(i!=j){
                    if (Math.abs(nums[i]-nums[j])<=t &&  Math.abs(i-j)<=k ){return true;}  
                }         
            }
            

            }
             
        return false;
    
    }
    
    
    
    
    
}
