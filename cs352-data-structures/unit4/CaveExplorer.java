import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;
import java.util.Stack;

public class CaveExplorer {
	private char[][] layout;
	private int row;
	private int col;

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

	public boolean solve(StringBuilder path) {
		row = -1;
		col = -1;

		// Find the starting position marked with 'S'
		for (int i = 0; i < layout.length; i++) {
			for (int j = 0; j < layout[i].length; j++) {
				if (layout[i][j] == 'S') {
					row = i;
					col = j;
					break;
				}
			}
		}
		// Starting position not found
		if (row == -1 || col == -1) {
			return false;
		}

		Stack<int[]> stack = new Stack<>();
		stack.push(new int[]{row, col});

		while (!stack.isEmpty()) {
			int[] current = stack.pop();
			row = current[0];
			col = current[1];

			// Check if current position is the mirror pool
			if (layout[row][col] == 'M') {
				return true;
			}

			// Mark the current position as visited
			layout[row][col] = 'V';


			// Count the number of valid moves from the current position
			int validMoves = 0;

			// Explore all possible directions (north, east, south, west)
			if (isValidMove(row - 1, col)) {  // Move north
				validMoves++;
			}
			if (isValidMove(row, col + 1)) {  // Move east
				validMoves++;
			}
			if (isValidMove(row + 1, col)) {  // Move south
				validMoves++;
			}
			if (isValidMove(row, col - 1)) {  // Move west
				validMoves++;
			}

			// If there are two or more valid moves, push them onto the stack
		if (validMoves >= 2) {
			if (isValidMove(row - 1, col)) {  // Move north
					stack.push(new int[]{row - 1, col});
					path.append('n');
				}
			if (isValidMove(row, col + 1)) {  // Move east
					stack.push(new int[]{row, col + 1});
					path.append('e');
				}
			if (isValidMove(row + 1, col)) {  // Move south
					stack.push(new int[]{row + 1, col});
					path.append('s');
				}
			if (isValidMove(row, col - 1)) {  // Move west
					stack.push(new int[]{row, col - 1});
					path.append('w');
				}
			} else {
				// If there is only one valid move
			if (isValidMove(row - 1, col)) {  // Move north
					stack.push(new int[]{row - 1, col});
					path.append('n');
				} else if (isValidMove(row, col + 1)) {  // Move east
					stack.push(new int[]{row, col + 1});
					path.append('e');
				} else if (isValidMove(row + 1, col)) {  // Move south
					stack.push(new int[]{row + 1, col});
					path.append('s');
				} else if (isValidMove(row, col - 1)) {  // Move west
					stack.push(new int[]{row, col - 1});
					path.append('w');
				}
			}
		}

		return false;  // No path
	}

	private boolean isValidMove(int row, int col) {

		// Check if the move is within the bounds of the cave layout
		if (row >= 0 && row < layout.length && col >= 0 && col < layout[0].length) {

			// Check if the move is valid (not a wall or a visited position)
			char ifValidMove = layout[row][col];
			return ifValidMove != 'R' && ifValidMove != 'V';
		}
		return false;

	} // end isValidMove(int, int)

	// Step 4: getPath method
	public String getPath() {
		StringBuilder path = new StringBuilder();
		solve(path);
		return path.toString();
	}

	// Step 5: One parameter constructor to read from a file
	public CaveExplorer(String fname) throws FileNotFoundException {
		Scanner in = new Scanner(new File(fname));

		// Read the dimensions from the first line
		String firstLine = in.nextLine();
		String[] dimensions = firstLine.split("\\s+");
		int rows = Integer.parseInt(dimensions[0]);
		int cols = Integer.parseInt(dimensions[1]);

		this.row = rows; // NOTE: might not need this
		this.col = cols;

		// Construct cave
		layout = new char[rows][cols];

		// Read the layout from the file
		for (int i = 0; i < rows; i++) {
			String line = in.nextLine();
			layout[i] = line.toCharArray();
		}

		in.close();

	} // end CaveExplorer(String)

	// Step 6: printLayout method to print the layout of the cave
	public void printLayout() {
		for (int i = 0; i < layout.length; i++) {
			for (int j = 0; j < layout[i].length; j++) {
			System.out.print(layout[i][j]);
			}
			System.out.println();
		}
	} // End printLayout()

	public static void main(String[] args) {
		System.out.println("Starting CaveExplorer");

		// Create a CaveExplorer object using the default constructor
		CaveExplorer caveDefault = new CaveExplorer();
		caveDefault.printLayout();

		// Call solve
		StringBuilder defaultPath = new StringBuilder();
		boolean canBeSolvedDefault = caveDefault.solve(defaultPath);
		System.out.println("Can it be solved? " + canBeSolvedDefault);

		// Print the final layout
		String path = defaultPath.toString();
		System.out.println(path);

		// Create a CaveExplorer object by reading from a file
		String fileName = "testdat.txt";
		CaveExplorer caveFromFile = null;  // Declare the variable outside the try block error fix
		try {
			caveFromFile = new CaveExplorer(fileName);
			System.out.println("\nCave layout from file:");
			caveFromFile.printLayout();
			// Call solve
			StringBuilder filePath = new StringBuilder();
			boolean canBeSolvedFile = caveFromFile.solve(filePath);
			System.out.println("Can it be solved? " + canBeSolvedFile);
			// Print the final layout, whether there is a path and if so what it is.
			String pathFromFile = filePath.toString();
			System.out.println(pathFromFile);
		} catch (FileNotFoundException e) {
			System.out.println("Can't find file " + fileName);
		}

		String fileName2 = "testdat2.txt";
		CaveExplorer caveFromFile2 = null;  // Declare the variable outside the try block error fix
		try {
			caveFromFile2 = new CaveExplorer(fileName2);
			System.out.println("\nCave layout from file:");
			caveFromFile2.printLayout();

			// Call solve
			StringBuilder filePath2 = new StringBuilder();
			boolean canBeSolvedFile2 = caveFromFile2.solve(filePath2);
			System.out.println("Can it be solved? " + canBeSolvedFile2);

			// Print the final layout, whether there is a path and if so what it is.
			String pathFromFile2 = filePath2.toString();
			System.out.println(pathFromFile2);
		} catch (FileNotFoundException e) {
			System.out.println("Can't find file " + fileName2);
		}

		String fileName3 = "testdat3.txt";
		CaveExplorer caveFromFile3 = null;  // Declare the variable outside the try block error fix
		try {
			caveFromFile3 = new CaveExplorer(fileName3);
			System.out.println("\nCave layout from file:");
			caveFromFile3.printLayout();
			// Call solve
			StringBuilder filePath3 = new StringBuilder();
			boolean canBeSolvedFile3 = caveFromFile3.solve(filePath3);
			System.out.println("Can it be solved? " + canBeSolvedFile3);
			// Print the final layout, whether there is a path, and if so, what it is.
			String pathFromFile3 = filePath3.toString();
			System.out.println(pathFromFile3);
		} catch (FileNotFoundException e) {
			System.out.println("Can't find file " + fileName3);
		}
		System.out.println("Finished CaveExplorer");
	}

}

