/*
 * Bert Darnell
 * CS252 Unit5 Assignment
 * 11/20/2022
 *
 * This program is an exerercise practicing inheritance and composition.
 *
 * Derived Classes:
 *
 * DB08Employee (current)
 *   DB08Staff 
 *     DB08Manager
 *
 * DB08TestHR (main)
 *
 */

import java.time.LocalDate;

public abstract class DB08Employee {
  protected String id;
  protected String firstName;
  protected String lastName;
  protected String position;
  protected LocalDate hiringDate;
  protected int annualSalary;

  // Default constructor. Set member variables to null or 0
  public DB08Employee() {} 

  // Constructor with parameters to set the protected variables
  public DB08Employee(String id, String firstName, String lastName,
		  String position, LocalDate hiringDate, int annualSalary) {
    this.id           = id;
    this.firstName    = firstName;
    this.lastName     = lastName;
    this.position     = position;
    this.hiringDate   = hiringDate;
    this.annualSalary = annualSalary;
  } 
  
  // Gets the id of this object
  public String getId() {
    return id;
  }

  // Sets the id of this object with the given value
  public void setId(String id) {
    this.id = id;
  }

  // Gets the first name of this object
  public String getFirstName() {
    return firstName;
  }

  // Sets the first name of this object with the given value
  public void setFirstName(String firstName) {
    this.firstName = firstName;
  }

  // Gets the last name of this object
  public String getLastName() {
    return lastName;
  }

  // Sets the last name of this object with the given value
  public void setLastName(String lastName) {
    this.lastName = lastName;
  }

  // Gets the position of this object
  public String getPosition() {
    return position;
  }

  // Sets the position of this object with the given value
  public void setPosition(String position) {
    this.position = position;
  }

  // Gets the hiring date of this object
  public LocalDate getHiringDate() {
    return hiringDate;
  }

  // Sets the hiring date of this object with the given value
  public void setHiringDate(LocalDate hiringDate) {
    this.hiringDate = hiringDate;
  }

  // Gets the annual salary of this object
  public int getAnnualSalary() {
    return annualSalary;
  }

  // Sets the annual salary of this object with the given value
  public void setAnnualSalary(int annualSalary) {
    this.annualSalary = annualSalary;
  }

  // Returns the full name of this object
  public String getFullName() {
    return firstName + " " + lastName;
  }

  // Returns a string representation of this employee
  @Override
  public String toString() {
    return String.format("ID: %s, Name: %s, Position: %s, HiringDate: %s, Salary: $%,d (Bonus: $%,d)", 
        id, getFullName(), position, hiringDate, annualSalary, getAnnualBonus());
  } 
  
  // Ensure each subclass has a getAnnualBonus() method
  public abstract int getAnnualBonus();

} // end class Employee

