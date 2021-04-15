package LeetcodePractice;

import java.util.Arrays;


public class SolutionQ26 {
	
	/*Given a sorted array nums, remove the duplicates in-place such that each element appears only once and returns the new length.*/
	
    public static int removeDuplicates(int[] nums) {
        
    	 
        int n=nums.length;
        int loc;
        if (n==0){ return loc =0;}
        
        int my_duplicate = nums[0];
        loc = 1;
        for (int i=0;i<n;i++){
            if (nums[i]!=my_duplicate){
                nums[loc]=nums[i];
                loc++;
                my_duplicate = nums[i];}
            
        }
        return loc;
	
	
    }
    
    
    public static void main(String arg[]) {
    	
    	int [] nums = {0,0,1,1,1,2,2,3,3,4}; 
    	//int [] nums = {1,1,2};
    
    	int result = removeDuplicates(nums);
    	
    	System.out.println(result);
    	System.out.println(Arrays.toString(nums));
    	
    }
    

}
