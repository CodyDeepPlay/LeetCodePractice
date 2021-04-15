package LeetcodePractice;

import java.util.*;


//Definition for a binary tree node.
class TreeNode {
       int val;
       TreeNode left;
       TreeNode right;
       TreeNode() {}
       TreeNode(int val) { this.val = val; left=right=null;}
       TreeNode(int val, TreeNode left, TreeNode right) {
	          this.val = val;
	          this.left = left;
	          this.right = right;
      }
  }


public class SolutionQ653 {
	
	
    //public class BinaryTree{
    //	TreeNode root;
    //}
	
	
	// *************************************************************************
	// below are functions of how to create a binary search tree (BST)
	
	
    // using recursive method to create a binary tree
    public static void myAdd(TreeNode root, Integer value) {
    	root = addRecursive(root, value);
    }
    
    private static TreeNode addRecursive(TreeNode currentNode, Integer value) {
    	    	
    	//System.out.println(value);
    	/* when adding values to the node,
    	 * if the current node is null, then just use this given value to create a new node, 
    	 * which is the root of the tree */
    	if (currentNode==null)    {return new TreeNode(value);} //  
    	//if (currentNode.val == 0) {return new TreeNode(value);}  
    	 	
    	/*when value is smaller than the currentNode value, the value is added to the 
    	 * left branch of the currentNode, and update the current left object*/
    	//if (value==null) {return currentNode;}  // if the current value is null, means this node doesn't have this branch.
    	
    	if      (value<currentNode.val ) {currentNode.left =addRecursive(currentNode.left, value); }
    	else if (value>currentNode.val ) {currentNode.right=addRecursive(currentNode.right, value);}
    	//else {return currentNode;}  //value already exist
    	return currentNode;
    
    }
    

    
    // manually create a binary search tree
    public static TreeNode createBinaryTree() {
    	
    	//TreeNode tree = new TreeNode();
    	TreeNode root = new TreeNode(5);
    	
    	root.left      = new TreeNode(3);
    	root.left.left = new TreeNode(2);
    	root.left.right = new TreeNode(4);
    	
    	root.right = new TreeNode(6);
    	root.right.right = new TreeNode(7);
    	
    	
    	return root;
    }
    
    
    
    
    // *************************************************************************
    
    
    
    
    // *************************************************************************
    // Starting here is part of my solution
    // Solution1: traverse binary tree in in-order traversal algorithm

    
    public static void inOrder_justVal(TreeNode node, ArrayList inputList) {
    	//just use inOrder to get the all the elements values in the tree.
    	if (node ==null) {return;}
    	
    	inOrder_justVal(node.left,  inputList);
    	inputList.add(node.val);    // add the node value into the predifined list
    	inOrder_justVal(node.right, inputList);
    	
    } 
    
    
    
    // Solution 1: use two-pointer to conduct the search
    public static boolean findTarget(TreeNode root, int k) {

    	ArrayList<Integer> myList = new ArrayList<Integer>(); // initialize an empty list
    	    	
    	if (root==null) {return false; } // if the node is null, 
    	else if (root.right==null && root.left==null) {return false;} // if the both of the sub node of root node is null, then, this tree is just a root node
    	
    	// only conduct in-order value extraction if the node is not empty
    	else {
   	    	inOrder_justVal(root, myList); // use in-order method to put all values in "root" from small to big into 'myList'
   	    	
	    	int head=0;
	    	int tail=myList.size()-1;
	    	int mySum;
	    	
	    	while(head<tail) {
	    		mySum = myList.get(head) + myList.get(tail);
	    		if      (mySum >k) {tail -=1;}
	    		else if (mySum <k) {head +=1;}
	    		else {return true;}
	        }
        return false;
	    	  	
    	}
    	
        
    }
    
    
    // solution 2: hash able map function
    public static boolean findTarget_map(TreeNode root, int k) {
    
    	ArrayList<Integer> myList = new ArrayList<Integer>(); // initialize an empty list
    	Map<Integer, Integer> myMap = new HashMap<>();
    	
    	
    	if (root==null) {return false; } // if the node is null, 
    	else if (root.right==null && root.left==null) {return false;} // if the both of the sub node of root node is null, then, this tree is just a root node
    	
    	// only conduct in-order value extraction if the node is not empty
    	else {
   	    	inOrder_justVal(root, myList); // use in-order method to put all values in "root" from small to big into 'myList'
   	    	
   	    	for(int i=0;i<myList.size();i++) {
   	    		if ( myMap.containsKey(k-myList.get(i)) ) {return true;} // complement is in my map, find the solution
   	    		else { myMap.put(myList.get(i),i);}  	    	
   	    		}

        return false;
    	
    	}
    	
    }
    

    
    

   
    // ******** end of my solution
    
	public static void main(String arg[]) {
		boolean output; 
		
		Integer[] input= {5,3,6,2,4,null,7}; // 'int' is a primitive, and can not have null; but 'integer' as an object, can have null values
		int target = 9;
		
		// initialize a binary tree node
		TreeNode root = new TreeNode(); 
		System.out.println(root.val);
		
		// put the values into this Binary Search Tree
		for (int i=0;i<input.length;i++) {
			if (input[i]!=null) { myAdd(root, input[i]);}
		}
		
        
		//root = createBinaryTree();
		
		// test my in-order function is correct or not
		ArrayList<Integer> myList = new ArrayList<Integer>(); // initialize an empty list
		inOrder_justVal(root, myList);
		
		System.out.println(Arrays.toString(myList.toArray()));  // first need convert ArrayList into Array
		
		
		// below is testing my solution
		//output = findTarget(root, target);
		output = findTarget_map(root, target);
		
		//output = findTarget_map_inorder(root, target);
	
	    //System.out.println(Arrays.toString(output));
		System.out.println(output);
	
	}
	
	
	
	
}

	
	








