/*********************************************************************************************************************
    Bert Darnell
    8/29/2021
    CS202

    This is a program that tallies votes for 10 candidates. After the votes are displayed it declares the winner.

**********************************************************************************************************************/
#include <iostream>

int main() {
    int validate_number = 0; // variable to determine if the inputed candidate number is in the range 0-90
    int candidate_number; // input candidate
   
    printf("Please enter a integer between 0-90 to generate each candidate: ");
    scanf_s("%d", &candidate_number);
     
    // This block validates if input is in 0-90 range    
    while (validate_number < 1) {
        if (candidate_number < 0 || candidate_number > 90) {
            printf("Invalid number (%d). Please enter a integer between 0-90: ", candidate_number);
            scanf_s("%d", &candidate_number);
        }
        else {
            validate_number++;
        }
    }
    // Sets each candidate to the sequential number
    int candidate1 = candidate_number;
    int candidate2 = candidate_number + 1;
    int candidate3 = candidate_number + 2;
    int candidate4 = candidate_number + 3;
    int candidate5 = candidate_number + 4;
    int candidate6 = candidate_number + 5;
    int candidate7 = candidate_number + 6;
    int candidate8 = candidate_number + 7;
    int candidate9 = candidate_number + 8;
    int candidate10 = candidate_number + 9;

        // Prints all the candidates
    printf("Thank you. Please vote for one of the fallowing candidates: %d %d %d %d %d %d %d %d %d %d\n",
    candidate1, candidate2, candidate3, candidate4, candidate5, candidate6, candidate7, candidate8, candidate9, candidate10);
    
    // sets the votes for each candidate to 0
    int tally1 = 0, tally2 = 0, tally3 = 0, tally4=0, tally5=0, tally6=0, tally7=0, tally8=0, tally9=0, tally10=0;
    int end_tally = 0; //this variable is for ending the votes
    int vote_canidate; //checks if the input matches a candidate
    int vote_counter = -1; //counts total votes

        // Tallies the votes with inputed number associated with each candidate
    while (end_tally > -1) {
        printf("Enter the canidate number to cast a vote. (enter a negative to exit): ");
        scanf_s("%d", &vote_canidate);
        vote_counter++;
        if (vote_canidate < end_tally) { // ends votes with negative number
            end_tally--;
        }
        else if (vote_canidate == candidate1) {
            tally1++;
        }
        else if (vote_canidate == candidate2) {
            tally2++;
        }
        else if (vote_canidate == candidate3) {
            tally3++;
        }
        else if (vote_canidate == candidate4) {
            tally4++;
        }
        else if (vote_canidate == candidate5) {
            tally5++;
        }
        else if (vote_canidate == candidate6) {
            tally6++;
        }
        else if (vote_canidate == candidate7) {
            tally7++;
        }
        else if (vote_canidate == candidate8) {
            tally8++;
        }
        else if (vote_canidate == candidate9) {
            tally9++;
        }
        else if (vote_canidate == candidate10) {
            tally10++;
        }
        else {
            printf("That candidate is not in the range of %d - %d \n", candidate1, candidate10);
            vote_counter--;
        }
    }
    
    // prints total votes for each candidate
    printf("The tallies for the votes are:\n candidate %d with %d\n candidate %d with %d\n candidate %d with %d\n candidate %d with %d\n candidate %d with %d\n candidate %d with %d\n candidate %d with %d\n candidate %d with %d\n candidate %d with %d\n candidate %d with %d\n",
    candidate1, tally1, candidate2, tally2, candidate3, tally3, candidate4, tally4, candidate5, tally5, candidate6, tally6,candidate7, tally7,candidate8, tally8,candidate9, tally9,candidate10, tally10);
    
    int winner; // variable for the winning candidate
    int highest_tally; // variable for the largest inputed tallies

    winner = candidate10;
    highest_tally = tally10;

    if (tally9 >= highest_tally) { //determines the candidate with the most tallies. Decending order, so lowest candidate number wins
        winner = candidate9;       
        highest_tally = tally9;
    }
    if (tally8 >= highest_tally) {
        winner = candidate8;
        highest_tally = tally8;
    }
    if (tally7 >= highest_tally) {
        winner = candidate7;
        highest_tally = tally7;
    }
    if (tally6 >= highest_tally) {
        winner = candidate6;
        highest_tally = tally6;
    }
    if (tally5 >= highest_tally) {
        winner = candidate5;
        highest_tally = tally5;
    }
    if (tally4 >= highest_tally) {
        winner = candidate4;
        highest_tally = tally4;
    }
    if (tally3 >= highest_tally) {
        winner = candidate3;
        highest_tally = tally3;
    }
    if (tally2 >= highest_tally) {
        winner = candidate2;
        highest_tally = tally2;
    }
    if (tally1 >= highest_tally) {
        winner = candidate1;
        highest_tally = tally1;
    }
    // prints the winner
    if (vote_counter <= 0) {
        printf("There were no votes casted\n");
    }
    else {
    printf("Winning candidate is %d with %d votes.\n", winner, highest_tally);
    }

    return 0;
}   