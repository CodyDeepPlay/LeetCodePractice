package LeetcodePractice;
import java.util.*;


public class SolutionQ299 {

	/*
	 * Solution 1
	 * 
	 * first iterate through the both secret and guess at the same time to find the bulls,
	 * At the same time, for those non-equal characters in both array, they are potential cows,
	 * we will save them in two separate maps, and count their appearance. 
	 * 
	 * Then, we will iterate through the guess map, to see if a given character is in the
	 * secrete potential cows' map. If so, the smaller number of appearance in guess and secret maps
	 * are the cows. 
	 * Iterate through all the keys in the guess_map, all the cows should be added together. 
	 *
	 * */
    public static String getHint(String secret, String guess) {
             
    	String result;
        int myA=0, myB=0;
        
        Map<Character, Integer> secret_map = new HashMap<>();
        Map<Character, Integer> guess_map   = new HashMap<>();
        
        char [] secret_char = secret.toCharArray();
        char [] guess_char  = guess.toCharArray();
        
        // find bulls
        // when find a bull, will delete it from the shorter version of trackers,
        // they should at the same location
        // when deleted one, don't forget to decrease the index by the deleted amount
        for (int n=0; n<guess_char.length; n++){	
        
            // track the bulls
        	if(secret_char[n] == guess_char[n]) {myA +=1;} 
        	
        	// track the cows
        	// create separate maps to store the potential cows in guess and secret
        	else {     		
        		// track candidate cows in secret
        		if ( secret_map.containsKey(secret_char[n]) ) {
        			// find one potential cow, add 1
        			secret_map.put(secret_char[n], secret_map.get(secret_char[n])+1); }
        		    // first time see a potential cow, assign 1
        		else {secret_map.put(secret_char[n], 1);}
        		      	
        		// track candidate cows in guess
        		if ( guess_map.containsKey(guess_char[n]) ) {
        			// find one potential cow, add 1
        			guess_map.put(guess_char[n], guess_map.get(guess_char[n])+1); }
        		    // first time see a potential cow, assign 1
        		else {guess_map.put(guess_char[n], 1);}	
        	
        	}}
        
 
        // iterate through each key from the guess potential cows map
        for (Character myKey: guess_map.keySet()) {

        	/* If a key in guess_map exist in the secret map, that means we find some cows,
        	 * Here we need to see which map has the lower number of this character, that will be 
        	 * the number of cows for this character
        	 * 
        	 * Do this for all the characters in the guees_map
        	 * */
        	
        	if (secret_map.containsKey(myKey) ) {
        		myB +=Math.min(guess_map.get(myKey), secret_map.get(myKey));}
        }
 
        // prepare the output string
        result = myA+"A" + myB+"B";
        
        return result;
        
    }
    
    
    

    /* Solution 2: 
     * 
     * Using two for-loops
     * 
     * */
    public static String getHint2(String secret, String guess) {
        
	    String result;
        int myA=0, myB=0;
        int loc;      
        int str_len = secret.length();      
        int count;
        int delete_count=0; // track how many chars have been removed
  
        /* create shorter version of 'secret' and 'guess' to track which element has been compared
         * */
        StringBuilder shorter_s = new StringBuilder (secret);
        StringBuilder shorter_g = new StringBuilder (guess);
 
        // find bulls
        // when find a bull, will delete it from the shorter version of trackers,
        // they should at the same location
        // when deleted one, don't forget to decrease the index by the deleted amount
        for (count=0; count<str_len; count++){	
        	// find a bull
        	// when find a bull, remove the char in 'secret' and remove char in 'guess'
        	if(secret.charAt(count)== guess.charAt(count)) {
        		myA +=1;	       		
       		
        		shorter_s.deleteCharAt(count-delete_count); // because we may delete some char before, the index need to remove that amount
        		shorter_g.deleteCharAt(count-delete_count); // because we may delete some char before, the index need to remove that amount

        		delete_count++; } 
        	}
        	
        
        // find cows
        // whatever left in the 'cows' will be re-compare, and delete any found appearance
        int short_len = shorter_s.length();
        for (int k=0; k<short_len;k++){
        	
        	loc =  shorter_s.toString().indexOf(shorter_g.toString().charAt(k) ) ;
        	if (loc !=-1) { 
    			myB +=1;	
    			shorter_s.deleteCharAt(loc);    // remove the cow from 'secret'
			}	  	
        }

        // prepare the output string
        result = myA +"A" + myB + "B";
        
        return result;
    
}
    
    
    
    
    /**********************************************************
	 *                END OF MY SOLUTION                      *
	 *           Below are running my solutions               *
	 **********************************************************/
    
    public static void main(String arg[]) {
		

		//int[] nums = {3,4,-1,1};
		//int[] nums = {7,8,9,11,12};
		//String secret = "1807", guess  = "7810";
    	//String secret = "1", guess  = "2";
		//String secret = "1122", guess  = "1222";
		//String secret = "1807", guess  = "7810";
    	String secret = "011", guess  = "011";
    	//String secret = "1234", guess  = "1234";
		//int loc =2;
		String result = getHint(secret, guess);
		
	    //secret.indexOf(guess.charAt(1));
		//String shorter=secret.substring(0,loc)+secret.substring(loc+1);
	
		//System.out.println(Arrays.toString(myList.toArray()));  // first need convert ArrayList into Array
		
	    //System.out.println(Arrays.toString(output));
		//System.out.println("My result is " + guess.charAt(0));
		//System.out.println("My result is " + guess.substring(1,3));
		System.out.println("My result is " + result);		
	
		//sb.deleteCharAt(0);
		
		//String result2 = sb.toString();
//
//    	int loc =  shorter_s.toString().indexOf(shorter_g.toString().charAt(0) ) ;
//        
//    	for (int k=0; k<shorter_s.length();k++){
//        	
//        	loc =  shorter_s.toString().indexOf(shorter_g.toString().charAt(k) ) ;
//        	System.out.println(loc);	
//        	
//        	if (loc !=-1) { 
//    			shorter_s.deleteCharAt(loc);    // remove the cow from 'secret'
//    			shorter_g.deleteCharAt(k);   
//    			
//    			}	
//        	
//        }

	}	
	
	
	
}
