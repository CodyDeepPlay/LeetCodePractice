package LeetcodePractice;

import java.util.Arrays;

public class SolutionQ189 {
	
	
	
public void rotate(int[] nums, int k) {
        
        int n = nums.length;
        int temp=nums[0]; 
        int counter = 0;
        int start=0;
        int idx=start; // initiate starting index.
        int next_idx=idx+k;
        k = k%n; // if k is bigger than n, we just to need look at the residua, that is the real shift       
        if (k==0){return;} // every element shift to back its own position
        

            
        if(n%k==0 & n%2==0){ 
            for (int i=0;i<k;i++){
                 temp = nums[i+k];
                 nums[i+k] = nums[i];
                 nums[i] = temp;}
            }     
            
        else{//(n%k !=0)
        	
        	System.out.println("i am here");
        	
        	while(next_idx!=start){           
            	
            	
                //if (next_idx > n-1) {next_idx = next_idx - n;}
            	//System.out.println(Arrays.toString(nums));	
            	//System.out.println(next_idx);	
            	
            	next_idx = next_idx%n;
                //next_idx = next_idx%n;
 
                temp = nums[next_idx];
                nums[next_idx] = nums[start];
                nums[start] = temp;  // once first element has been moved, this space is empty, and we can use it to store values
   
                idx   = next_idx; // update current idx, 
                next_idx= (idx+k)%n;

              } 

 
              
        
    }


}

}
