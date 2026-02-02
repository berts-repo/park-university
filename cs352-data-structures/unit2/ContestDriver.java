import java.util.LinkedList;
import java.util.Random;

public class ContestDriver {

    public static void main(String[] args) {


            int numContestants = 43;
            int numRounds = 10000;
            double averagePosition;

            System.out.println("Starting Simulation");

            // This creates a single Contestant and prints its attributes, just to show it can be done
            Contestant ac = new Contestant("Billy", 22);
            System.out.println(ac);

            // Create multiple Contestants and add them to a LinkedList
            LinkedList<Contestant> contestants = new LinkedList<>();
            for (int i = 1; i <= numContestants; i++) {
                    Contestant contestant = new Contestant("Contestant " + i, i * 10);
                    contestants.add(contestant);
            }

            // Print the contestants.
	    for (Contestant contestant : contestants) {
		    System.out.println(contestant);
	    }


            long startTime = System.currentTimeMillis();
	    // Simulate multiple rounds
	    for (int round = 1; round <= numRounds; round++) {
		    System.out.println("Round " + round);

		    boolean isAnswerCorrect;
		    Random random = new Random();
		    int index = 0; // Tracks the next position in object list, as elements are added and removed.

		    for (int i = 0; i < contestants.size(); i++) {
			    Contestant contestant = contestants.get(index);
			    isAnswerCorrect = random.nextBoolean();
			    System.out.println("Coin flip result: " + isAnswerCorrect);

			    // Sort the list according to correct answers in the round
			    if (isAnswerCorrect) {
				    contestants.remove(index);
				    contestants.addFirst(contestant); // Move to the front
			    } else {
				    contestants.remove(index);
				    contestants.addLast(contestant); // Move to the end
				    index--;
			    }
			    index++;
		    }

		    // Update and print the order of contestants at the end of each round
		    int eachRound = 0;
		    System.out.println("Round " + round + " order:");
                    for (Contestant contestant : contestants) {
                            // Update contestant's position
                            contestant.updatePosition(eachRound);
                            System.out.println("contestant: " + contestant  + " Current position: " + contestant.getPosition() + " Total position: " + contestant.getTotalPosition());
                            eachRound++;
                    }
            }

            // Calculate and print average positions
            System.out.println("Average Positions:");
            for (Contestant contestant : contestants) {
                    averagePosition = contestant.getAveragePosition(numRounds);
                    System.out.println(contestant.getName() + ": " + averagePosition);
            }

            long endTime = System.currentTimeMillis();
            long elapsedTime = endTime - startTime;


	    
	    System.out.println("elapsed time: " + elapsedTime );
	    System.out.println("Finished");
    }
}

