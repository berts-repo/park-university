/*
 *
 *  Bert Darnell
 *  10-30-22
 *  CS252
 *  Unit 2
 *
 *  This program test that a a method takes an ArrayList of Strings, and moves the largest lexicographical
 *  string to the end of the ArrayList. If multiple copies only moves the first.
 *  
 *
 */
import java.util.Arrays;
import java.util.ArrayList;

public class DB08E3Max {

	public static ArrayList<String> maxToEnd( ArrayList<String> list){ 

		String largestString = list.get(0);
		int largestStringIndex = 0;

			// Already set largestString to index 0, so iteration starts at 1.

			for ( int i = 1; i < list.size(); ++i ) {
			String currentString = list.get(i);
			int checkLength = largestString.compareTo( currentString );

			// Checks and stores the largest string compared to the current iteration of ArrayList

			if ( checkLength < 0 ){
				largestString = list.get(i);
				largestStringIndex = i;
			}
			
		}
		list.remove(largestStringIndex);
		list.add(largestString);
		return list;
	
	}

// Provided testing for main

	public static void main(String[] args){
		String[] strArr;  // will be used to convert a list of values to arraylist
		ArrayList<String> strList;
		ArrayList<String> expected;
		
		strArr = new String[] {"the", "best", "day", "ever"};
		strList = new ArrayList<>(Arrays.asList(strArr));
		System.out.println("original: " + strList); // print original
		System.out.println("successful: " + maxToEnd(strList) );
		expected = new ArrayList<>(Arrays.asList(new String[] {"best", "day", "ever", "the"}));
		if ( !strList.equals(expected) ) 
			System.out.println("failed. Result: " + strList);

		strArr = new String[] {"one", "Value"};
		strList = new ArrayList<>(Arrays.asList(strArr));
		System.out.println("original: " + strList); // print original
		System.out.println("successful: " + maxToEnd(strList) );
		expected = new ArrayList<>(Arrays.asList(new String[] {"Value", "one"}));
		if ( !strList.equals(expected) ) 
			System.out.println("failed. Result: " + strList);


		strArr = new String[] {"three", "Two", "three", "four"};
		strList = new ArrayList<>(Arrays.asList(strArr));
		System.out.println("original: " + strList); // print original
		System.out.println("successful: " + maxToEnd(strList) );
		expected = new ArrayList<>(Arrays.asList(new String[] {"Two", "three", "four", "three"}));
		if ( !strList.equals(expected) ) 
			System.out.println("failed. Result: " + strList);

		strArr = new String[] {"four"};
		strList = new ArrayList<>(Arrays.asList(strArr));
		System.out.println("original: " + strList); // print original
		System.out.println("successful: " + maxToEnd(strList) );
		expected = new ArrayList<>(Arrays.asList(new String[] {"four"}));
		if ( !strList.equals(expected) ) 
			System.out.println("failed. Result: " + strList);

	}
}
