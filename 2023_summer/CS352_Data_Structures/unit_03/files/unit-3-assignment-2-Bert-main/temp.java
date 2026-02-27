import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class CaveExplorer {
	private char[][] layout;
	private StringBuilder path = new StringBuilder();

	// Step 1: Zero parameter constructor to create the specified cave
	public CaveExplorer() {
		layout = new char[][]{
			{'R', 'R', 'R', 'R', 'R', 'R'},
			{'R', '.', '.', 'S', 'R', 'R'},
			{'R', '.', 'R', 'R', 'R', 'R'},
			{'R', '.', 'M', 'R', 'R', 'R'},
			{'R', 'R', 'R', 'R', 'R', 'R'}
		};
	}
	// Step 2: toString method
	@Override
	public String toString() {
		StringBuilder result = new StringBuilder();
		for (int i = 0; i < layout.length; i++) {
			for (int j = 0; j < layout[i].length; j++) {
				result.append(layout[i][j]);
			}
			result.append("\n");
		}
		return result.toString();
	}

	// Step 3: solve method
	// Returns a boolean true if there is a path to the mirror pool, and false if there is not.
	public Boolean solve() {
		int lastRow = -1;
		int lastCol = -1;

		for (int i = 0; i < layout.length; i++) {
			for (int j = 0; j < layout[i].length; j++) {
				if (layout[i][j] == 'S') {
					while (true) {
						if (layout[i][j] == 'M') {
							return true;
						} 

						if (j + 1 < layout[i].length && (layout[i][j + 1] == '.' || layout[i][j + 1] == 'M') && j + 1 != lastCol) {
							lastCol = j;
							j++;
							path.append("e");
						} else if (j - 1 >= 0 && (layout[i][j - 1] == '.' || layout[i][j - 1] == 'M') && j - 1 != lastCol) {
							lastCol = j;
							j--;
							path.append("w");
						} else if (i + 1 < layout.length && (layout[i + 1][j] == '.' || layout[i + 1][j] == 'M') && i + 1 != lastRow) {
							lastRow = i;
							i++;
							path.append("s");
						} else if (i - 1 >= 0 && (layout[i - 1][j] == '.' || layout[i - 1][j] == 'M') && i - 1 != lastRow) {
							lastRow = i;
							i--;
							path.append("n");
						} else {
							break;
						}
					}
				}
			}
		}
		return false;
	}

	// Step 4: getPath method
	public String getPath(){
		return path.toString();
	}	
	
	// Step 5: One parameter constructor to read from a file

	public CaveExplorer (String fname) throws Exception {
		Scanner in = new Scanner(new File(fname));

		int rows = in.nextInt();
		int cols = in.nextInt();  
		String s = in.nextLine(); // Skip newline character

		// Construct cave and populate with rest of data in the file
		layout = new char[rows][cols];

		for (int i = 0; i < rows; i++) {
			String line = in.nextLine();
			layout[i] = line.toCharArray();
		}

		in.close();
	}



	public static void main(String[] args) {
		System.out.println("Starting CaveExplorer");

		// Create a CaveExplorer object and print the starting layout
		CaveExplorer cave = new CaveExplorer();
		System.out.println(cave.toString());

		// Call solve
		System.out.println("Can it be solved? " + cave.solve());

		// Print the final layout, whether there is a path, and if so, what it is.
		String path = cave.getPath();
		System.out.println(path);

		// Step 5/6: Repeat for a different CaveExplorer object read from a file
		String fileName = "testdat.txt";
		CaveExplorer ce2 = null;  // Declare the variable outside the try block
		try {
			ce2 = new CaveExplorer(fileName);
			// Print the final layout, whether there is a path, and if so, what it is.
			ce2.solve();
			String path2 = ce2.getPath();
			System.out.println(path2);
		} catch (FileNotFoundException e) {
			System.out.println("Can't find file " + fileName);
		} catch (Exception e) {
			System.out.println("Other error: " + e.getMessage());
		}

		if (ce2 != null) {
			System.out.println("Can it be solved? " + ce2.solve());
		}

		System.out.println("Finished CaveExplorer");
	}


}

