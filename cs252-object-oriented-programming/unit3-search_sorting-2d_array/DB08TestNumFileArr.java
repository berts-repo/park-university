/*
 * Bert Darnell
 * 11-4-2022
 * CS252
 * Unit 3 Assignment 2
 *
 * */

// classes used for file i/o and i/o exception
import java.io.IOException;
import java.nio.file.Path;

import java.util.Scanner; // I/O methods
import java.util.Arrays;
import java.util.ArrayList;

public class DB08TestNumFileArr {

  // call method to load data from file and prepare for processing
  public static void main(String[] args) {
    ArrayList<Integer> numList = null; // declare an ArrayList var and initialize to null

    // relative path and file name of data file
    String fileName = "data/records.txt";

    numList = loadFromFile(fileName);  // load data

    System.out.println("Records: " + numList);
	
	// Step 2 
	int[] numArr = null; // to hold data
	int size = 0; // track actual # of elements.
	numArr = toIntArray(numList); 
	size = numList.size();
	System.out.println("Now in arr: " + Arrays.toString(numArr));

	// Step 4
	sort(numArr, size);
	System.out.println("After sorting: " + Arrays.toString(numArr));
	
	// Step 6
	Scanner stdIn = new Scanner(System.in);
	int num;
	for (int i=0; i<2; i++) {
		System.out.print("Enter a number: ");
		num = stdIn.nextInt();
		size = insert(numArr, size, num);
		System.out.printf("After inserting %d: %s\n", num, Arrays.toString(numArr));
	}
	stdIn.close(); // Eclipse requires closing a Scanner object

  } // end main


  // read data from a specified file
  // data will be saved in ArrayList and returned
  private static ArrayList<Integer> loadFromFile(String fileName) {
    Scanner fileIn = null; // scanner object to connect to file
    ArrayList<Integer> list = new ArrayList<>(); // to store data from file

    try { // try-catch-finally used for any exception during file open/read/close
      // open input file
      fileIn = new Scanner( Path.of(fileName) );

      // loop through multiple records
      while (fileIn.hasNextInt()) { // still have numbers to be read?
        // 1. read one record (here each record is just one num)
        int num = fileIn.nextInt();

        // 2. add the record to ArrayList obj
        list.add(num);

        // end one record
      }// end while: reading all records

    } catch (IOException ioe) {
      System.out.println("Error reading \"" + fileName + "\" file: " + ioe);
    } finally { // close file
      if ( fileIn != null) {  // close if was connected to a file
        fileIn.close();
      }
    }
    // end file input

    return list;
  }// end loadFromFile

  // return a partially filled int array with all elements from ArrayList
  // param in the same sequence and 5 extra spots at the end
  private static int[] toIntArray(ArrayList<Integer> list) {
	  
	  int[] intArray = new int[list.size()+5];

	  for ( int i = 0; i < list.size(); ++i){
			intArray[i] = list.get(i); 
	  }
	  return intArray;
	}
  // sort a partially filled array ([0 ~ numOfElements-1]) into
  // ascending order
  // Will return and not modify the arr if arr is null or
  // numOfElements is invalid
  private static void sort(int[] arr, int numOfElements) {
	
	  int temp;      
	  int indexSmallest;
	  
	  // Selection sorts on the else, and returns unsorted if invalid parameters
	  if ( arr == null );
	  else if ( numOfElements < 0 | numOfElements > arr.length );
	  else { 
		  for (int i = 0; i < arr.length - 1 - numOfElements; ++i) {	// NOTE: weird that I had to -1, and +1 for the nested loops.
			  indexSmallest = i;
			  for (int j = i + 1; j < arr.length - numOfElements + 1; ++j) {	// NOTE: j = i + 1 becuase indexSmallest starts at 0

				  if (arr[j] < arr[indexSmallest]) {
					  indexSmallest = j;
				  }
			  }

			  // Swap numbers[i] and numbers[indexSmallest]
			  temp = arr[i];
			  arr[i] = arr[indexSmallest];
			  arr[indexSmallest] = temp;
		  }
	  }
  }
  // insert into a partially filled array ([0~numOfElements-1]) and
  // maintain sorted order (ascending)
  // This method returns number of stored elements at the end.
  // If insert failed (such as arr is null, numOfElements is invalid,
  // or arr is already full), do not modify arr content and return
  // numOfElements
  private static int insert(int[] arr, int numOfElements, int newItem) {

	  if ( arr == null | numOfElements < 0 | numOfElements > arr.length | numOfElements == 0 )
		  return numOfElements;
	  else {
		  arr[ arr.length - numOfElements + 1 ] = newItem;
		  numOfElements--;
		  sort ( arr, numOfElements );
	  } 
 	 return numOfElements;	
  }

} // end class TestNumFile
