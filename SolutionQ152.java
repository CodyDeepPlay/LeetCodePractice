package LeetcodePractice;

import java.util.HashMap;
import java.util.*;

public class SolutionQ152 {
	
	public static int maxProductMap(int[] nums) {
		
		int n = nums.length;
		int[] cuProduct= new int[n]; // cumulative product
		int maxProduct = nums[0];
		cuProduct[0]   = nums[0];
		
		Map<Integer, Integer> myMap = new HashMap<>();
        myMap.put(nums[0], 1);  // the value of cumulative product, and number of times
		
		for (int i=1;i<n;i++) {
			cuProduct[i] = cuProduct[i-1]*nums[i];
			if (cuProduct[i]>maxProduct) {maxProduct=cuProduct[i];};
			
			
			
			
			//if (myMap.containsKey(cuProduct/maxProduct) ) {}
			
			
		}
		
		return maxProduct;
		
		
		
		
		
		
		
	}
	
	
	/*keep track of minimum and maximum of the product,
	 * minimum of the product could be a negative number, if a negative number times a negative number,
	 * then it might have a very big positive number, which might be the max*/
	public static int maxProduct(int[] nums) {
		
		int n = nums.length;
		if (n==0) {return 0;}
		
		int maxProduct = nums[0];
		int current_max=nums[0]; 
		int current_min=nums[0];
			
		for (int i=1;i<n;i++) {
			
			int temp_max=current_max; // if current_max get into some operation, it might get changed
			
			// track the continous product for maximum and the individual unit 
			current_max = Math.max( Math.max(current_max*nums[i], current_min*nums[i]),    // here current_min might be an negative, and num[i] might also be negative, then it will be a very big positive number
								   nums[i] );  // also don't forget to compare with the current element in the array
			// current min is used to check whether if there is any negative number later multiplied by this negative number to give a big positive number
			current_min = Math.min( Math.min(current_min*nums[i], temp_max*nums[i]),  nums[i] ); 
			
			if (current_max>maxProduct) {
				maxProduct = current_max;
			}
		
		}

		return maxProduct;
		
	}
	
	
	public static void main(String arg[] ) {
		
		//int[] nums= {2,3,-2,4};
		int[] nums= {-2, 0, -1, -6,};
		//int[] nums= {-2, 3, 4, 0};
		
		int maxProduct = maxProduct(nums) ;
		
		System.out.println(maxProduct);
		
		
	}
	
	
	
	
	

}
