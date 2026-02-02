/*
 * Bert Darnell
 * 10-25-2022
 * CS252
 * Assignment question #2
 *
 *
 * This program takes an array and returns true if all the odd numbers come before the even numbers.
 *
 */

public class DB08E2OddEven {
	public static boolean isOddEven(int[] list){
		int lastOdd = -1;
		int countEvens = 0; 
		boolean beginEvenCount = false;

		for (int i = 0; i < list.length; ++i){
// Starts counting remaining evens to calcule if last odd.			
			if ( lastOdd == i - 1 )	beginEvenCount = true;
// If even.
			if ( list[i] % 2 == 0){
				if ( beginEvenCount == true )
					countEvens++;
			}
// If odd.
			if ( list[i] % 2 != 0 ) 
				lastOdd = i;
		}
		
// Adds the last odd index to the the even count, to determine if it is same length of the array.		
		if ( lastOdd + countEvens == list.length - 1 )
			return true;
		else 
			return false;
	}
	public static void main(String[] args){

		int[] test1 = {7, 3, 6, 6};
		int[] test2 = {1, 2, -3};
		int[] test3 = {-1};
		int[] test4 = {};
		int[] test5 = {1, 3, 5, 2, 4, 7};

		System.out.println( isOddEven(test1) );
		System.out.println( isOddEven(test2) );
		System.out.println( isOddEven(test3) );
		System.out.println( isOddEven(test4) );
		System.out.println( isOddEven(test5) );

	}
}
