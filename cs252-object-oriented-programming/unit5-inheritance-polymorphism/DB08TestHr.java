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
 *     DB08Manager
 *
 * DB08TestHR (main)
 *
 */

import java.time.LocalDate;
public class DB08TestHr{

	public static void main(String[] args){
		
		DB08Staff s1 = new DB08Staff("101", "S1Bert", "Darnell",
				"Technician I", LocalDate.now().minusYears(2), 80000);
		DB08Staff s2 = new DB08Staff("102", "S2Ernie", "Sesseme",
				"Technician I", LocalDate.now().minusYears(1), 80000);
	
		DB08Manager m1 = new DB08Manager("201", "M1Kenneth", "Dewey",
				"Professor", LocalDate.now().minusYears(4), 100000);
		DB08Manager m2 = new DB08Manager("202", "M2Crystal", "Peng",
				"Professor", LocalDate.now().minusYears(10), 150000);

		System.out.println( s1.toString() );
		System.out.println( s2.toString() );
		System.out.println( m1.toString() );
		System.out.println( m2.toString() );
		
	}
}

