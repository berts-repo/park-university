/*
 *   A simplified system to simulate course registration in one academic term.
 *   Manages course session data and course registration data for the specific
 *   term.
 *
 * Author: Bert Darnell
 * Park University
 * CS252 
 * 12/4/2022
 *
 */
package darnell;
import java.time.LocalDateTime;
import java.util.ArrayList;
import java.util.Collections;


public class HW7RegistrationManager {
  // relative path and file name of default data files
  // Those two files should already exist in a folder named "data".
  // If using an IDE and source code file is put in a default "src" folder (or similar),
  // folder "data" should be at the same location as the "src" folder;
  // otherwise, "data" folder should be at the same location as your .java file
  private final static String defaultCourseDataFileName = "data/courseData.csv";
  private final static String defaultRegistrationDataFileName = "data/registrationData.csv";

  private String courseDataFileName;
  private String registrationDataFileName;

  private ArrayList<HW7CourseSession> courseList;
  private ArrayList<HW7RegistrationRecord> registrationList;

  // Constructs a Registration Manager object with data from the default data source
  public HW7RegistrationManager() {
    this(defaultCourseDataFileName, defaultRegistrationDataFileName);
  }

  // Constructs a Registration Manager object with data from specified source
  public HW7RegistrationManager(String courseDataFileName, String registrationDataFileName) {
    this.courseDataFileName = courseDataFileName;
    this.registrationDataFileName = registrationDataFileName;
    loadData();

    // testing
    System.out.println("# of course session records: " + courseList.size());
    System.out.println("# of registration records: " + registrationList.size());
  }

  // Loads course and registration data.
  // Sort and validate course data for efficient search.
  // Reconstruct class roster for each course session.
  private void loadData() {
    // load course data
    courseList = HW7DataSource.loadCourseSessionData(courseDataFileName);
    Collections.sort(courseList); // easier for constant search
    for (int i=courseList.size()-1; i>0; i--) { // validate data: eliminate duplicates
      if (courseList.get(i).compareTo(courseList.get(i-1))==0) // (i) and (i-1) same course session id
        courseList.remove(i);
    }
// 
//
// NOTE: Area of interest
//
//
    // load registration data
    registrationList = HW7DataSource.loadRegistrationData(registrationDataFileName);

    // reconstruct class roster for each course session from registration data
    for (int i=0; i < registrationList.size(); i++) {
      HW7RegistrationRecord record = registrationList.get(i);

      String courseSessionId = record.getCourseSessionId();
      int index = findCourseSession(courseSessionId);
      if (index >= 0) {
        courseList.get(index).addStudent(record.getStudentId());
      } else { // invalid course session id
        System.out.println("Error loading registration records: invalid course session id " + courseSessionId);
      }
    } // end for loop
  } // end loadData

  // Gets the year of the current registration window
  public int getCurrentRegistrationYear() {
    if (!courseList.isEmpty())
      return courseList.get(0).getYear();

    return 0;
  }

  // Gets the term of the current registration window
  public String getCurrentRegistrationTerm() {
    if (!courseList.isEmpty())
      return courseList.get(0).getTerm();

    return null;
  }

  // Returns the index of the first occurrence of the specified course session in the course list,
 // or -1 if the course list does not contain the element.
  // or -1 if the course list does not contain the element.
  private int findCourseSession(String courseSessionId) {
    for (int i = 0; i<courseList.size(); i++) {
      if (courseList.get(i).getSessionId().equals(courseSessionId))
        return i;
    }
    return -1; // not found
  }

  // Returns the index of the first occurrence of the specified registration record,
  // or -1 if the registration list does not contain the element.
  private int findRegistrationRecord(String courseSessionId, String studentId) {
    for (int i = 0; i<registrationList.size(); i++) {
      HW7RegistrationRecord record = registrationList.get(i);
      if (record.getCourseSessionId().equals(courseSessionId) &&
          record.getStudentId().equals(studentId))
        return i;
    }
    return -1; // not found
  }

  // Returns an ArrayList of course sessions whose course number starts with the given value
  public ArrayList<HW7CourseSession> searchByCourseNumber(String courseNum) {
    String courseNumCopy = courseNum.trim().toUpperCase();
    ArrayList<HW7CourseSession> list = new ArrayList<>();
    for (HW7CourseSession cs : courseList) {
      if (cs.getCourseNumber().startsWith(courseNumCopy))
        list.add(cs);
    }
    return list;
  }

  // Returns a list of course sessions the given student has enrolled in
  public ArrayList<HW7CourseSession> searchByStudentId(String studentId) {
    String studentIdCopy = studentId.trim();
    ArrayList<HW7CourseSession> list = new ArrayList<>();
    for (HW7RegistrationRecord rr : registrationList) {
      if (rr.getStudentId().equals(studentIdCopy)) {
        String courseSessionId = rr.getCourseSessionId();
        int index = findCourseSession(courseSessionId);
        if (index >=0)
          list.add(courseList.get(index));
      }
    }
    return list;
  }

  // Register the given student with the specified course session and return true
  // if the operation succeeded. Return false and this object unchanged if
  // invalid class session id, invalid student id, or if the class is already full
  public boolean addStudentRegistration(String courseSessionId, String studentId) {
    // validate and clean data
    String sessionIdCopy = courseSessionId.trim().toUpperCase();
    String studentIdCopy = studentId.trim();
    int index = findCourseSession(sessionIdCopy);

    if (index < 0 || studentIdCopy.isEmpty()) { // invalid course session or invalid student id
      return false;
    }

    // add to course roster and add a registration record
    if (courseList.get(index).addStudent(studentIdCopy)) {
      HW7RegistrationRecord record = new HW7RegistrationRecord(sessionIdCopy, studentIdCopy, LocalDateTime.now());
      registrationList.add(record);
      return true;
    }

    return false; // not able to add to class. may be full, or student already registered
  } // addStudentRegistration

  // Remove the given student from the specified course session and return true
  // if the operaation succeeded. Return false and this object unchanged if
  // invalid class session id, invalid student id, or if such a registration doesn't exist
  public boolean removeStudentRegistration(String courseSessionId, String studentId) {
    // validate and clean data
    String sessionIdCopy = courseSessionId.trim().toUpperCase();
    String studentIdCopy = studentId.trim();
    int index = findCourseSession(sessionIdCopy);

    if (index < 0 || studentIdCopy.isEmpty()) { // invalid course session or invalid student id
      return false;
    }

    // remove from course roster and remove the registration record
    // ACTURAL COURSE REGISTRATION SYSTEM:
    //   would not remove a registration record, but add a
    // will add a "add" registration record.
    // This is the general principle of all database systems.
    if (courseList.get(index).removeStudent(studentIdCopy)) {
      // should have such a registration record if able to remove from class roster
      int rrIndex = findRegistrationRecord(sessionIdCopy, studentIdCopy);
      if (rrIndex >=0)
        registrationList.remove(rrIndex);
      // else ; // do nothing if not found

      return true;
    }

    return false;
  } // end removeStudentRegistration

  //-----------------------------------------

  // public static void main(String[] args) {
	  // HW7RegistrationManager rm = new HW7RegistrationManager();

	  // String selectStudentId = "1694208";
	  // String selectCourseSecId = "CS130DLF2A2022";

	  // System.out.println("Add " + selectStudentId + " to " + selectCourseSecId);
	  // System.out.println(rm.addStudentRegistration(selectCourseSecId, selectStudentId));
	  // System.out.println(rm.addStudentRegistration(selectCourseSecId, selectStudentId));

	  // System.out.println("Remove " + selectStudentId + " from " + selectCourseSecId);
	  // System.out.println(rm.removeStudentRegistration(selectCourseSecId, selectStudentId));
	  // System.out.println(rm.removeStudentRegistration(selectCourseSecId, selectStudentId));

  // }// end main.


  	
} // end class HW7RegistrationManager
