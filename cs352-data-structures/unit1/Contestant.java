import java.util.ArrayList;
/* Contestant.java:  
 * This class extends Person while adding attributes and methods
 * related to recording performance in the specified contest. 
 *     
 * Author: Name and Student ID
 * Last updated: 
 */
public class Contestant extends Person {
	// A Contestant IS-A Person
	// that also needs needs to keep track of data related to the game
	private int position;
	private int totalPosition;

	public Contestant(String name, int age) {
		super(name, age);
		position = 0;
		totalPosition = 0;
	}

	public int getPosition() {
		return position;
	}

	public int getTotalPosition() {
		return totalPosition;
	}

	public void updatePosition(int newPosition) {
		position = newPosition;
		totalPosition += newPosition;
	}

	public double getAveragePosition(int numRounds) {
		return (double) totalPosition / numRounds;
	}
}

