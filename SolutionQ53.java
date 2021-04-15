package LeetcodePractice;

public class SolutionQ53 {

	
	/*Given an integer array nums, find the contiguous subarray (containing at least one number) 
	 * which has the largest sum and return its sum.
	 * 
	 * follow up: If you have figured out the O(n) solution, 
	 * try coding another solution using the divide and conquer approach, which is more subtle.
	 * 
	 * */
	
	
	
	
	
	
	/* solution1: 
	 * - first, maxSum and curSum are all initialized with first element in the array
	 * - maxSum will be used to track the maximum of the sum.
	 * - whenever the curSum is negative, if the current Sum is adding with next element,
	 * 		it will not make next element bigger, so set the curSum here as zero.
	 * 		Since maxSum already track the maximum of the sum, we will not lose the information
	 * - next, always compare the maxSum with the curSum when available. */
	public static int maxSubArray(int[] nums) {
		
		if(nums.length ==1) {return nums[0];}
		
		int maxSum=nums[0], curSum=nums[0];
		
		for(int i=1;i<nums.length;i++) {		
        	/* if curSum is negative, adding next value will not 
			 * make next value bigger, so set it to 0	
			 * */
			if(curSum<0) {curSum=0;} 			
			curSum +=nums[i];		
			if(curSum>maxSum) {maxSum=curSum;}	
		}
		
		return maxSum;
        
    }
	
	
	/*solution 2: divide and conqur*/
	public static int maxSubArray_DAC(int[] nums) {
		int maxSum=nums[0];
		

		return maxSum;
        
    }
	
	
	public static void main(String arg[]) {
		
	int[] nums = {-2,1,-3,4,-1,2,1,-5,4};
		
	
	int result = maxSubArray(nums);
	
	System.out.print(result);
	
		
	}
	
	
}
