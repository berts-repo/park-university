/**
 * @author John Cigas
 * Bert Darnell
 * Professor David  
 * CS352 Unit5
 * 7/9/2023
 *
 * This assignment lets you read data from a file then sort it by two different methods. One is the built-in sort() method, and the other will be your own method that implements a mergeSort algorithm. You will compare the performance of the two implementations.
 */
public class Temperature {
	private String city;
	private String state;
	private int low;
	private int high;

	public Temperature(String city, String state, int low, int high) {
		this.city = city;
		this.state = state;
		this.low = low;
		this.high = high;
	}

	public String getCity() {
		return city;
	}

	public String getState() {
		return state;
	}

	public int getLow() {
		return low;
	}

	public int getHigh() {
		return high;
	}

	public int getDifferential() {
		return high - low;
	}

	/* Add appropriate instance attributes, constructors, and accessor/mutator methods */
}
