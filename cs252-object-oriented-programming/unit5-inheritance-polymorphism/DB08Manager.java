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
 *   DB08Staff 
 *     DB08Manager (current)
 *
 * DB08TestHR (main)
 *
 */

import java.time.LocalDate;
import java.util.ArrayList;

public class DB08Manager extends DB08Staff{
	
	private ArrayList<DB08Employee> teamMember;

	// default constructor
	public DB08Manager(){
		teamMember = new ArrayList<DB08Employee>();	
			}
	// constructor
	public DB08Manager( String id, String firstName, String lastName,
			String position, LocalDate hiringDate, int annualSalary){
	
		teamMember = new ArrayList<DB08Employee>();	

		this.id = id;	
		this.firstName = firstName;
		this.lastName = lastName;
		this.position = position;
		this.hiringDate = hiringDate;
		this.annualSalary = annualSalary;
	}
//	public boolean addTeamMember( DB08Staff member ){
//		if ( teamMember.equals(member) != true ){ return false; }
//		else {
//			teamMember.add(member);
//			member.setManager();
//			return true;
//		}
//	}

//	public boolean removeTeamMember( DB08Staff member ){
//		if ( teamMember.equals(member) != true ){ return false; }
//		else {
//			teamMember.remove(member);
//			setManager();
//			return true;
//		}
//}
	public String toString(){
		return super.toString() + " Manages: " ; //FIXME no teamMember list 
	}

	public int getAnnualBonus(){ 
		return (int)(annualSalary * 0.1);
	}

}
