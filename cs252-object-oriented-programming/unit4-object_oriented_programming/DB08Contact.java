//==============
// Part 1
//==============

/**
 * Please add proper file prolog comment
 */

public class DB08Contact {
  private String name;
  private String emailAddress;
  
  // Constructs a Contact object with null name and email address
  public DB08Contact() {}
  
  // Constructs a Contact object with the specified name and email address
  // Assume emailAddress represents a valid email address
  public DB08Contact(String name, String emailAddress) {
    this.name = name;
    this.emailAddress = emailAddress;
  }
  
  // Sets email address 
  // Assume emailAddress represents a valid email address
  public void setEmailAddress(String emailAddress) {
    this.emailAddress = emailAddress;
  }

  // Sets contact name 
  // Assume emailAddress represents a valid email address
  public void setName(String name) {
    this.name = name;
  }  
  
  // Gets email address of the calling object
  public String getEmailAddress() {
    return emailAddress;
  }

  // Gets name of the calling object
  public String getName() {
    return name;
  }

  // Returns a string representation of a contact in the format of:
  // name <email address>
  public String toString() {
    return name + " <" + emailAddress + ">"; 
  }
  
  // unit testing
  public static void main(String[] args) {
    DB08Contact p1 = new DB08Contact();
    DB08Contact p2 = new DB08Contact("John Doe", "jdoe@gmail.com");
    
    // toString() of a class will be invoked when its object is 
    // used in print/ln/f or concatenated with a string
    System.out.println(p1); 
    System.out.println(p2); 
    System.out.println(p1); 
 }

}
