/*
Bert Darnell
Kenneth Dewey
CS252
Discussion1
10/22/2022
Question 15

This program checks if a user input license number is in the correct Missouri format, by comparing the index of letters and digits
*/
import java.util.Scanner;

public class disc1{

// Returns true if the string parameter contains a valid Missouri license number.
   public static boolean isValid(String checkNumber) {

	String validNumber = "LLDLDL";
	char isDigit = 'D';
	char isLetter = 'L';	
	int validLength = validNumber.length();

   for (int i = 0; i < validLength; i++) {	   

		// indexes the valid license format to a character variable
	char validDigit  = validNumber.charAt(i);
	char validLetter = validNumber.charAt(i);  
		// boolean for user inputed license, is digit or letter
	boolean checkDigit  = Character.isDigit ( checkNumber.charAt(i) );
	boolean checkLetter = Character.isLetter( checkNumber.charAt(i) );

			// checks if digit from valid license format
	if      ( validDigit == 'D' ) { 
		if (checkDigit == true);
		else return false;
       	}
			// checks if letter from valid license format
	else if ( validLetter == 'L' ) {
		if (checkLetter == true);
		else return false;
       	}
   }
   return true;
   } 
	
   public static void main(String[] args) {
	   
		// user inputs license number
    String checkNumber;
    Scanner scnr = new Scanner(System.in);
    checkNumber = scnr.nextLine();
    
		// calls method
    System.out.println( isValid(checkNumber) );
   }
}
