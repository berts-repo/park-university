/*
 * Bert Darnell
 * 10/23/2022
 *
 * This program takes user ratings between 0 and 5 and calculates statistics from the inputs.
 *
 *
 */

import java.util.Scanner;

public class DB08InputStats {
public static void main(String[] args) {

	Scanner scnr = new Scanner(System.in);
	int ratingInput = 0;
	int numRatings = 0;
	int positiveRatings = 0;
	int neutralRatings = 0;
	int negativeRatings = 0;
	int invalidRatings = 0;


	System.out.println("Please enter the ratings (end with negative value):");

// This block counts the ratings for each category.

	while ( ratingInput >= 0 ) {
			ratingInput = scnr.nextInt();

			if ( ratingInput > 5 ){
			invalidRatings++;
			}
			else if ( ratingInput >= 4 ){
			positiveRatings++;
			}
			else if ( ratingInput == 3 ){
			neutralRatings++;
			}
			else if ( ratingInput >= 0 ){
			negativeRatings++;
			}

			numRatings++;

	}
	
	numRatings = numRatings - 1;

// This calculates and formats the percentages.	

	double positiveStats = (double) positiveRatings * 100.0/ (double) numRatings;
	double neutralStats  = (double) neutralRatings  * 100.0/ (double) numRatings;
	double negativeStats = (double) negativeRatings * 100.0/ (double) numRatings;
	double invalidStats =  (double) invalidRatings  * 100.0/ (double) numRatings;

	System.out.println("Total # ratings: " + numRatings );
	System.out.printf("Positive ratings (4~5): %d (%.0f%%)\n", positiveRatings, positiveStats);
	System.out.printf("Neutral ratings (3): %d (%.0f%%)\n", neutralRatings, neutralStats);
	System.out.printf("Negative ratings (0~2): %d (%.0f%%)\n", negativeRatings, negativeStats);
	System.out.printf("Invalid ratings (>5): %d (%.0f%%)\n", invalidRatings, invalidStats);

}
}
