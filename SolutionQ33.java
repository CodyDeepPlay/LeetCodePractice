package LeetcodePractice;

import java.util.Arrays;

public class SolutionQ33 {
	/*You are given an integer array nums sorted in ascending order, and an integer target.

Suppose that nums is rotated at some pivot unknown to you beforehand (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

If target is found in the array return its index, otherwise, return -1.*/
    
	
	
	/*solution1: brutal force, conduct search in the for loop*/
	
	public static int search(int[] nums, int target) {
		
		int output =-1;
        for(int i=0;i<nums.length;i++) {
        	if (nums[i]==target) {output = i;break;}
        }
        return output;
    
    }
	
	
	
	public static void main(String arg[]) {
		int output; 
		
		int[] nums = {4,5,6,7,0,1,2};
		int target = 0;
		
		output = search(nums,target);
		
		int[] print_output = new int[1];
		print_output[0] = output;
		
		System.out.println(Arrays.toString(print_output));
	   
		
		
		
		
		
	}
	
	
	

}
