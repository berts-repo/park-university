/*
 *	Bert Darnell
 *	11-6-22
 *	CS252
 *	Unit 3
 *	Excercise 1
 *
 *
 *	This simulates selecting a rectangle from and area of an image.
 *
 *
 *
 */
import java.util.Arrays;

public class DB08SelectRectanglar {
	public static void main(String[] args){
		int[][] image = new int[][] {
			{0, 1, 2, 3, 4, 5, 6, 7, 8}, 
			{10, 11, 12, 13, 14, 15, 16, 17, 18},
			{20, 21, 22, 23, 24, 25, 26, 27, 28}, 
			{30, 31, 32, 33, 34, 35, 36, 37, 38}, 
			{40, 41, 42, 43, 44, 45, 46, 47, 48}};

		int startRow = 3;
		int startCol = 7;
		int endRow = 1;
		int endCol = 2;

		int[][] select;
		select = SelectRectanglar(image, startRow, startCol, endRow, endCol);

		// Prints returned array if not null
		if ( select != null ){
			for ( int[] row : select ){
				for ( int col : row ){
					System.out.printf("%2d ", col);
				}
				System.out.println("");
			}
		}
		System.out.printf( "(%d, %d) (%d, %d)\n", startRow, startCol, endRow, endCol );
	}
// Returns a full 2d int array with data from the rectangular area 
// specified by startRow, startCol, endRow, and endCol if those 
// four specify a valid area. Otherwise return null. 
// Also return null if image is null or has zero rows or zero cols
	public static int[][] SelectRectanglar(int[][] imageArray,
			int startRow, int startCol,
			int endRow,   int endCol
			){
		
		// Validates the methods passed integers.
		if ( imageArray == null )
			return null;
		else if (startRow < 0)
			return null;
		else if (endRow < 0)
			return null;
		else if (startCol < 0)
			return null;
		else if (endCol < 0)
			return null;
		else if (imageArray.length < 1)
			return null;
		else if (imageArray[1].length < 1)
			return null;

	
		// New array for the rectangle from 'image'
		int[][] select = new int[ Math.abs(endRow - startRow) + 1 ][ Math.abs(endCol - startCol) + 1 ];
		
		boolean inRange = true;
		int rowPos = -1;
		int colPos = -1;

		// Outer nested loop, to iterate through 'image'
		for ( int row = 1; row < imageArray.length; ++row ){

			// Checks if row is in range, and positions 'select' index.
			if ( row < startRow && row < endRow );
			else if ( row > startRow && row > endRow );
			else {
				inRange = true;
				rowPos++;
			}
			// Inner nested loop for 'image'
			for (int col = 1; col < imageArray[row].length; ++col){
				// If row is in range, and if col is in range, creates 'select' from 'image'
				if ( inRange == false );
				else if ( col < startCol && col < endCol );
				else if ( col > startCol && col > endCol );
				else {
					colPos++;
					select[rowPos][colPos] = imageArray[row][col];
				}
			}
			// Resets column index.
			colPos = -1;
		}
		return select;
	}
}
