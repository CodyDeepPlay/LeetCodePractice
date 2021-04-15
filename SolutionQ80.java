package LeetcodePractice;

public class SolutionQ80 {
	
    public int removeDuplicates(int[] nums) {
        
        int n=nums.length;
        int my_duplicate = nums[0];
        int duplicate_twice_check=1; // track if duplicated value appear twice
        int pre_serve_loc = 1;
        
        for (int i=1; i<n;i++){

        	// increment the duplicate tracker
            if (nums[i] == my_duplicate){
                duplicate_twice_check++;
            }
            // if current element is a new one, initialize my_duplicate value and reset my duplicate twice tracker
            else if (nums[i] != my_duplicate){
                my_duplicate = nums[i];  
                duplicate_twice_check = 1; // started a new 2 duplicates check
            }
            
            // track if 2 more repeated value has been reached.
            if (duplicate_twice_check <3) {  // allow two repeated element, so the 3rd repeated element, we need to take some action
                nums[pre_serve_loc] = nums[i];
                pre_serve_loc++;
            }

        }
        
        return pre_serve_loc;
        
        
    }
	
}
