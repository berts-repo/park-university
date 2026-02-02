/*
 *   Connects to data source of course sessions and registration records.
 * 
 * Author: Bert Darnell
 * Park University
 * CS252 
 * 12/4/2022
 */
package darnell;
import java.io.IOException;
import java.nio.file.Path;
import java.time.format.DateTimeParseException;
import java.util.ArrayList;
import java.util.Scanner;
import java.time.LocalDateTime;

import darnell.HW7CourseSession;

public class HW7DataSource {

  // Loads course session data from the given file and returns the data
  // in an ArrayList
  public static ArrayList<HW7CourseSession> loadCourseSessionData(String fileName) {
    ArrayList<HW7CourseSession> list = new ArrayList<>(); // to store data from file
    int numOfRecordsInDataSource = 0;

    try (Scanner fileIn = new Scanner(Path.of(fileName))) { // open data file
      // 1st row should be header. skip
      if (fileIn.hasNext())
        fileIn.next();

      // loop through multiple records
      while (fileIn.hasNext()) { // still have records?
        // 1. read one record
        String record = fileIn.next();
        numOfRecordsInDataSource++;

        // 2. extract data:
        // col 0: course number
        // col 1: year
        // col 2: term
        // col 3: section
        // col 4: cap
        String[] cols = record.split(","); // split a comma separated line
        String courseNumber = cols[0].trim().toUpperCase();
        int year = Integer.parseInt(cols[1].trim());
        String term = cols[2].trim().toUpperCase();
        String section = cols[3].trim().toUpperCase();
        int cap = Integer.parseInt(cols[4].trim());

        if (courseNumber.isEmpty())
          throw new IllegalArgumentException("empty course number");
        if (term.isEmpty())
          throw new IllegalArgumentException("empty term");
        if (section.isEmpty())
          throw new IllegalArgumentException("empty section");

        // 3. create an object from the data
        // courseNumber, year, term, section, cap
        HW7CourseSession oneRecord = new HW7CourseSession(courseNumber,
            year,
            term,
            section,
            cap);

        // 4. add to arraylist
        list.add(oneRecord);

        // end one record
      }// end while: reading all records

    } catch (IllegalArgumentException iae) {
        // thrown by course session constructor call
        // will also catch its subtype NumberFormatException from parseInt()
      System.out.println("Invalid course session data: " + iae.getMessage());
      System.out.println("Record #" + numOfRecordsInDataSource + " not added."); // list.add() didn't run for this record
    } catch (IOException ioe) {
      System.out.println("Error reading \"" + fileName + "\" file: " + ioe);
      System.out.println("Records read: " + numOfRecordsInDataSource + "; Records processed: " + list.size());
    }
    // end file input

    return list;
  } // end loadCourseSessionData

  // Loads registration data from the given file and returns the data
  // in an ArrayList
  public static ArrayList<HW7RegistrationRecord> loadRegistrationData(String fileName) {
    ArrayList<HW7RegistrationRecord> list = new ArrayList<>(); // to store data from file
    int numOfRecordsInDataSource = 0;

	try (Scanner fileIn = new Scanner(Path.of(fileName))) { // Open data file.

		if (fileIn.hasNext())
        fileIn.next();
		
		while (fileIn.hasNext()) {
			String record = fileIn.next();
			numOfRecordsInDataSource++;

			// col 0: COURSE_SEC_ID
			// col 1: STUDENT_ID
			// col 2: TIME_OF_REGISTRATION
			String[] cols = record.split(","); // split a comma separated line
			String courseSessionId = cols[0].trim().toUpperCase();
			String studentId = cols[1].trim();
			String timeOfRegistration = cols[2].trim().toUpperCase();

			LocalDateTime dateTime = LocalDateTime.parse(timeOfRegistration);
		    
			if (courseSessionId.isEmpty())
				throw new IllegalArgumentException("empty course session id");
			if (studentId.isEmpty())
				throw new IllegalArgumentException("empty student id");
			if (timeOfRegistration.isEmpty())
				throw new IllegalArgumentException("empty time of registration");
			
			HW7RegistrationRecord oneRecord = new HW7RegistrationRecord(courseSessionId, studentId, dateTime);

			list.add(oneRecord);

		}// end while: reading all records
	} catch (IllegalArgumentException iae) {
		// thrown by course session constructor call
		// will also catch its subtype NumberFormatException from parseInt()
		System.out.println("Invalid course session data: " + iae.getMessage());
		System.out.println("Record #" + numOfRecordsInDataSource + " not added."); // list.add() didn't run for this record
	} catch ( DateTimeParseException dtpe ) {
		System.out.println("datetimeparse exception NOTE: could be data is 2021 and not 2022");
	} catch (IOException ioe) {
		System.out.println("Error reading \"" + fileName + "\" file: " + ioe);
		System.out.println("Records read: " + numOfRecordsInDataSource + "; Records processed: " + list.size());
	}

    return list;
  } // end loadRegistrationData

} // end class HW7DataSource
