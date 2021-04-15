package LeetcodePractice;

import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

public class MyMainFile {
	
	
	public static void main(String arg[]) {
	Solution mysolution = new Solution();
	
	SolutionQ274 mysolution2 = new SolutionQ274();
	
	//int [] nums = {1,2, 3}; int k=1;
	//int [] nums = {1,2,3,4,5,6,7}; int k=3;
	//int [] nums = {-1,-100,3,99}; int k=2;
	//int [] nums = {1,2,3,4,5,6}; int k=1;
	
	//int[] citations = {1, 2, 2, 2};
	//int[] citations = {0,0,4,4};
	//int[] citations = {3,0,6,1,5};
	//int[] citations = {7,7,7,7,7,7,7};
	//int[] citations = {0,0,0};
	//int[] citations= {0, 1};
	int[] citations= {0, 1, 0};
	
	int [] nums = {-2147483648,2147483647};
	int k=1, t=1;
	
    boolean me = mysolution.containsNearbyAlmostDuplicate(nums, k, t);
	
	//System.out.println(result);
	//int [] new_array=Arrays.copyOfRange(nums, 0, result); 
	//System.out.println(Arrays.toString(citations[0:2]));
	//int me = 13;
	System.out.println(me);
	System.out.println(nums[0]);
	System.out.println(nums[1]);
	System.out.println(-nums[0]+nums[1]);
	
	int anum =  citations[1];
	int [] this_diff = citations;
	
	Arrays.setAll(this_diff, i ->this_diff[i]-2);
    System.out.println(Arrays.toString(this_diff));
	
    
    
    
    
    
    
    
	}

}
