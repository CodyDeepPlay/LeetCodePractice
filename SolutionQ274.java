package LeetcodePractice;
import java.util.Arrays;

public class SolutionQ274 {
	
	
	/* Q274
	 * Solution 2
	 * 1. sort the array 
	 * 2. use binary search to look for H index, 
	 * 	at a certain location, when the citation is bigger than the location, 
	 * 	then the location is a hindex. 	
	*/
    public static int hIndex2(int[] citations) {
    	
    	
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
   public static int hIndex22(int[] citations) {
    	
    	
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
    public static int hIndex3(int[] citations) {
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

	
	
	// END OF MY SOLUTION
	// Below are running my solutions
    
    public static void main(String arg[]) {
		
		//int[] citations = {1, 2, 2, 2};
		//int[] citations = {0,0,4,4};
		//int[] citations = {3,0,6,1,5};
		//int[] citations = {7,7,7,7,7,7,7};
		int[] citations = {0,0,0};
        
		int hindex = hIndex22(citations);
		
		//System.out.println(Arrays.toString(myList.toArray()));  // first need convert ArrayList into Array
		
	    //System.out.println(Arrays.toString(output));
		System.out.println("My citation is " + hindex);
				
	
	}	
		

}
