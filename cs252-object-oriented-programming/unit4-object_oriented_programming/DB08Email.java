import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;

public class DB08Email {

	private int idGen = 1000;
	private int id;
	
	DB08Contact from;
	DB08Contact to;
    String subject;
	LocalDateTime timeStamp;
		
	// Default constructor.
	public DB08Email() {
		id = idGen;
	}

	public DB08Email(DB08Contact from, DB08Contact to, String subject ){ 
		idGen++;
		this.from = from;
		this.to = to;
		this.subject = subject;
		timeStamp = LocalDateTime.now();
	}

	public DB08Email( DB08Contact from, DB08Contact to,
			String subject, LocalDateTime timeStamp){

		idGen++;
		this.from = from;
		this.to = to;
		this.subject = subject;

	}
	
	public DB08Contact getFrom(){
		return from;
	}

	public DB08Contact getTo(){
		return to;
	}

	public String getSubject(){
		return subject;
	}

	public LocalDateTime getTimeStamp(){
		return timeStamp;
	}

	public void setFrom( DB08Contact from ){
		this.from = from;
	}

	public void setTo( DB08Contact to ){
		this.to = to;
	} 
	
	public void setSubject( String subject ){
		this.subject = subject;
	}

	public String toString(){ 
		
		// format: Three-letter-month-name, dd, yyyy, hh:mm AM-or-PM
		DateTimeFormatter formatter = DateTimeFormatter.ofPattern(
				"LLL dd, yyyy, hh:mm a");
		String timeStr = timeStamp.format(formatter);
		
		return
			"Subject: " + subject + "\n" +
			"From: " + from + "\n" + 
			"To: " + to + "\n" +
			"Time: " + timeStr + "\n";
	}	

	// main
	public static void main(String[] args){

		DB08Contact me = new DB08Contact("Bert Darnell", "bertdarnell@gmail.com");
		DB08Contact friend = new DB08Contact("Ernie", "sesamestreet@yahoo.com");
		DB08Email t1 = new DB08Email(me, friend, "Some subject");
		
		DB08Email t2 = new DB08Email( friend, me, "Return subject", 
		t1.getTimeStamp().plusHours(1));

		System.out.println(t1);
		System.out.println(t2);	
	}
}

