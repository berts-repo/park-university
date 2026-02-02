/* 
This method creates a masked 2d-array that represents negative numbers with a "0", 
and positive numbers with a "1" which is derived from a sample array that is
passed into the method. It then returns the new masked array.
*/
import java.util.Arrays;
public class discunit3-practice-answer17 {
	public static int[][] getMask ( int origArray[][] ){

		// Initialize the number of rows.
		int[][] maskedArray = new int[origArray.length][];		

		for ( int row = 0; row < origArray.length; ++row ){

			// Initializes the row length for each iteration.
			maskedArray[row] = new int[ origArray[row].length ]; 

			for ( int elem = 0; elem < origArray[row].length; ++elem ){
				if ( origArray[row][elem] > 0 ) 				
					maskedArray[row][elem] = 0;
				else {
					maskedArray[row][elem] = 1;
				}
			}
		}
	  return maskedArray;
	}

	public static void main(String[] args){

		int arr[][] ={{ 1,2,3 }, {-1,-2,-3 }, {1, -1, 1} };
		System.out.println( Arrays.deepToString( getMask(arr) ) );	
	}
}
