/*
 * Bert Darnell
 * CS252 Unit5 Assignment
 * 11/20/2022
 *
 * This program is an exerercise practicing inheritance and composition.
 * 
 * Derived Classes:
 *
 * DB08Employee
 *   DB08Staff (current)
 *     DB08Manager
 * 
 * DB08TestHR (main)
 *   
 */


import java.time.LocalDate;

public class DB08Staff extends DB08Employee{
	private DB08Manager manager;
		
	// default constructor
	public DB08Staff(){}

	// constructor
	public DB08Staff( String id, String firstName, String lastName,
			String position, LocalDate hiringDate, int annualSalary){

		this.id = id;
		this.firstName = firstName;	
		this.lastName = lastName;
		this.position = position;
		this.hiringDate = hiringDate;
		this.annualSalary = annualSalary;
	}
	// gets the manager for the array list in the manager class
	public DB08Manager getManager(){ 
		return manager;
	}
	
	// sets the manager in derived manager class
	protected void setManager( DB08Manager manager ){
		this.manager = manager;
	}
	
	// returns string from employee super class and concatinates
	public String toString(){

		if (manager != null){
			return super.toString() + " Manager: " + firstName + lastName; 
		}
		else{
			return super.toString() + " Manager: none";
		}
	}
	// returns bonus of 7.5% of annual salary
	public int getAnnualBonus(){ 
		return (int)(annualSalary * 0.075);
	} 
}
