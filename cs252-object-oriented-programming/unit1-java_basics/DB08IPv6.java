/*
 *	Bert Darnell
 *	10/23/2022
 *
 *	This program checks if a string is in the correct ipv6 address format
 * 
 */

import java.util.Scanner;

public class DB08IPv6 {

// This methode checks if the string is in the correct ipv6 format.

	public static boolean checkIpv6Format(String address) {
	
		String validFormat = "hhhh:hhhh:hhhh:hhhh:hhhh:hhhh:hhhh:hhhh";
		int i = 1;
		char currentPos;

// Returns false if length of string doesn't match the format.

		if ( address.length() != validFormat.length() ) { return false; }
		while ( i < address.length() ) {
			
			currentPos = address.charAt(i-1);

// Checks if hexidecimal and the colon's index and returns false if invalid.			

			if ( currentPos == ':'){
				if ( i % 5 != 0 ) return false; 
			}
			else if ( currentPos >= 'a' && currentPos <= 'f' ){
				if ( i % 5 == 0 ) return false;
			}
			else if ( currentPos >= 'A' && currentPos <= 'F' ){
				if ( i % 5 == 0 ) return false;
			}
			else if ( currentPos >= '0' && currentPos <= '9' ){
				if ( i % 5 == 0 ) return false;
			}
			
			else return false;
			i++;
	}
		return true;
	}

	public static void main(String[] args) {


// Test strings.		
																	// expected outcomes:
		String test1 = "0123:4567:89ab:cdef:0123:4567:89Ab:cDEf";	// valid
		String test2 = "0000:0000:0000:dddd:eeee:dddd:eeee:ffff";	// valid
		String test3 = "0000:0000:0000:0000:0000:0000:0000:0000";	// valid
		String test4 = "123:4567:89ab:cdef:0123:4567:89ab:cdef0"; 	// invalid
		String test5 = "0000:0000:0000"; 							// invalid
		String test6 = "01hg:4567:89ab:cdef:0123:4567:89ab:cdef"; 	// invalid
		String test7 = "0123:4567::89b:cdef:0123:4567:89ab:cdef";	// invalid
		String test8 = "0000:0000:    :0000:0000:0000:0000:0000";	// invalid
		String test9 = "0000:0000:0000:0000:0000:0000:0000:000$";	// invalid
		String test10 = "0000:0000:1111:0000:0000:0000:0000:0000";	// valid

// Testing and print format.

		System.out.println("Testing started...");

		if ( checkIpv6Format(test1) != true ) System.out.println("test1 " + test1 + " failed"); 
		if ( checkIpv6Format(test2) != true ) System.out.println("test2 " + test2 + " failed"); 
		if ( checkIpv6Format(test3) != true ) System.out.println("test3 " + test3 + " failed"); 
		if ( checkIpv6Format(test4) != true ) System.out.println("test4 " + test4 + " failed"); 
		if ( checkIpv6Format(test5) != true ) System.out.println("test5 " + test5 + " failed"); 
		if ( checkIpv6Format(test6) != true ) System.out.println("test6 " + test6 + " failed"); 
		if ( checkIpv6Format(test7) != true ) System.out.println("test7 " + test7 + " failed"); 
		if ( checkIpv6Format(test8) != true ) System.out.println("test8 " + test8 + " failed"); 
		if ( checkIpv6Format(test9) != true ) System.out.println("test9 " + test9 + " failed"); 
		if ( checkIpv6Format(test10) != true ) System.out.println("test10 " + test10 + " failed"); 

		System.out.println("testing complete.");
	}
}
