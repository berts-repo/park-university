/*
 * Unit 6
 * Homework 9
 * 9/24/2023
 * */

// Event listener for form submission
document.getElementById("signUpForm").addEventListener("submit", function(event) {
    event.preventDefault(); 
    // Call procces form function
    hw10_processForm(); 
});

// Function to process the form
function hw10_processForm() {
    const form = document.getElementById("signUpForm");
    const firstName = form.elements["firstName"].value;
    const lastName = form.elements["lastName"].value;
    const email = form.elements["email"].value;
    const password = form.elements["password"].value;
    const birthDate = form.elements["birthDate"].value;
    const country = form.elements["country"].value;
    const favoriteColor = form.elements["favoriteColor"].value;

    // Call the validate form function
    if (!hw10_validateForm(form)) {
        return;
    }
    alert("Form submission successful");
    //
    // Call and assign number of days since birthday function
    const daysSinceBirth = hw10_calc(birthDate, new Date());
    
    // Call the display function to add a new row in the table
    hw10_displayResults(firstName, lastName, email, password, birthDate, country, favoriteColor, daysSinceBirth);

    // Reset the form
    form.reset();
}

// Function to validate the form data
function hw10_validateForm(form) {
    // Basic validation for web form variables
    const firstName = form.elements["firstName"];
    const lastName = form.elements["lastName"];
    const email = form.elements["email"];
    const password = form.elements["password"];
    const birthDate = form.elements["birthDate"];
    const country = form.elements["country"];

    if (!firstName.checkValidity()) {
        alert("Invalid first name.");
    } else if (!lastName.checkValidity()) {
        alert("Invalid last name.");
    } else if (!email.checkValidity()) {
        alert("Invalid email.");
    } else if (!password.checkValidity()) {
        alert("Invalid password.");
    }  else if (!birthDate.checkValidity()) {
        alert("Invalid date of birth.");
    } else if (!favoriteColor.checkValidity()) {
        alert("Please select a favorite color.");
    } else if (country.value === "blank") {
        alert("Select a country.");
    } else {
        // Passed validation
        return true;
    }
}

// Function to calculate the number of days between date and current date
function hw10_calc(startDate, endDate) {
    const oneDay = 24 * 60 * 60 * 1000; // Milliseconds in a day
    const start = new Date(startDate);
    const end = new Date(endDate);
    const countDays = Math.round(Math.abs((end - start) / oneDay));
    return countDays;
}

// Function to create and append rows to the table
function hw10_displayResults(firstName, lastName, email, password, birthDate, country, favoriteColor, daysSinceBirth) {
    // Get form to add to the table
    const table = document.getElementById("resultsTable");

    // Create a new row
    const newRow = table.insertRow(-1);

    // Create table cells for each data field
    const cell1 = newRow.insertCell(0);
    const cell2 = newRow.insertCell(1);
    const cell3 = newRow.insertCell(2);
    const cell4 = newRow.insertCell(3);
    const cell5 = newRow.insertCell(4);
    const cell6 = newRow.insertCell(5);
    const cell7 = newRow.insertCell(6);
    const cell8 = newRow.insertCell(7);

    // Fill in the table from form elements
    cell1.innerHTML = firstName;
    cell2.innerHTML = lastName;
    cell3.innerHTML = email;
    cell4.innerHTML = password;
    cell5.innerHTML = birthDate;
    cell6.innerHTML = country;
    cell7.innerHTML = favoriteColor;
    cell8.innerHTML = daysSinceBirth;

    // Changes background color of table from color picker in homework10.html
    table.style.backgroundColor = favoriteColor;
}

/* 
 * Unit 5: homework.js
 * CS240 
 * Bert Darnell
 * 9/10/2023
 * 
 * Updated: 9/25/2023: Added comments and an alert to display variables
 *
 * */

// This function validates the web form for unit5's homework9.html
function processForm(form) {
    // Variables for web form
    var firstName = form.elements["firstName"];
    var lastName = form.elements["lastName"];
    var email = form.elements["email"];
    var password = form.elements["password"];
    var phoneNumber = form.elements["phoneNumber"];
    var birthDate = form.elements["birthDate"];
    var country = form.elements["country"];
    var signUpResult = form.elements["signUpResult"];

    // Basic validation for web form variables
    if (!firstName.checkValidity()) {
        alert("Invalid first name.");
    } else if (!lastName.checkValidity()) {
        alert("Invalid last name.");
    } else if (!email.checkValidity()) {
        alert("Invalid email.");
    } else if (!password.checkValidity()) {
        alert("Invalid password.");
    } else if (!phoneNumber.checkValidity()) {
        alert("Invalid phone number.");
    } else if (!birthDate.checkValidity()) {
        alert("Invalid date of birth.");
    } else if (country.value === "blank") {
        alert("Select a country.");
    } else {
        signUpResult.value = "Successfully signed up!";

        // Create a message to display all variables
        var message = "";
        message += "\nFirst Name: " + firstName.value;
        message += "\nLast Name: " + lastName.value;
        message += "\nEmail: " + email.value;
        message += "\nPassword: " + password.value;
        message += "\nPhone Number: " + phoneNumber.value;
        message += "\nBirth Date: " + birthDate.value;
        message += "\nCountry: " + country.value;
        message += "\nSign Up Result: " + signUpResult.value;

        // Display the message in an alert
        alert("Form Variables:\n" + message);
    }
}
