/*
 * Bert Darnell
 * CS 252
 * Unit 6 Assignment
 * 11-27-22
 * 
 * This assignment practices GUI. It implements warnings, buttons, text fields and check boxes.
 * The program validates an email and updates the number of participants, according
 * to each check box selected.
 */

package darnell;

import javafx.application.Application;
import javafx.event.ActionEvent;
import javafx.event.EventHandler;
import javafx.geometry.Insets;
import javafx.scene.Scene;
import javafx.scene.control.Alert;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.control.TextField;
import javafx.scene.control.Alert.AlertType;
import javafx.scene.layout.GridPane;
import javafx.stage.Stage;

import java.util.Arrays;

import javafx.scene.control.CheckBox;
import javafx.scene.layout.HBox;

public class DB08EventRegistration extends Application {
	
	private Label eventLabel;
	private Label countLabel;
	private Label selectLabel;
	private Label emailLabel;
	private TextField emailField;
	private Button registerButton;
	
	// Variables to update participants.
	private boolean eventSelect = false;
	String eventList = "";

	// List of events.
	private String[] eventNameList = { "Event 1", "Event 2", "Event 3", "Event 4", "Event 5" };
	private int listSize = eventNameList.length;
	private Label[] listEvents = new Label[listSize];

	private int[] countList = new int[listSize];
	private Label[] countLabelList = new Label[listSize];
	private CheckBox[] checkBoxList = new CheckBox[listSize];

	
// METHOD CALL
// Checks email field if empty and whitespace, and only one instance of '@' but not after '.' 
	private boolean checkEmail() {
		String checkEmailField;
		char pos;
		
		int countAtSymbol = 0;
		int countPeriod = 0;
		int lastAtSymbol = 0;
		int lastPeriod = 0;
		
		
		if ( emailField.getText().isEmpty())
			return false;
		else {
			checkEmailField = emailField.getText();
			for (int i = 0; i < checkEmailField.length(); ++i) {
				pos = checkEmailField.charAt(i);

				if ( Character.isWhitespace(pos) )
					return false;
				
				// Counts and gets index of '@'
				if ( pos == '@') {
					countAtSymbol++;
					lastAtSymbol = i;
				}
				// Counts and gets index of '.'
				if ( pos == '.') {
					countPeriod++;
					lastPeriod = i;
			}}}
		
		// Checks for '@' and '0'
		if ( countAtSymbol > 1 | countAtSymbol < 1 | countPeriod < 1)
			return false;
		if ( lastAtSymbol > lastPeriod) return false;
		
		return true;
	}
// METHOD CALL
// Event helper method that checks for at least one checked box.
	private void processRegistration() {

		if (checkEmail() == true) {
			for (int i = 0; i < listSize; ++i) {
				
				// Checks if check box was selected and updates variables.
				if (checkBoxList[i].isSelected()) {
					countList[i]++;
					checkBoxList[i].setSelected(false);
					eventSelect = true;
					eventList = eventList + "\n" + eventNameList[i];
					
				} 
			}
		} 
		else { 
			// Returns with email format error box.
			Alert alert = new Alert(AlertType.ERROR, "Please enter a valid email address.");
			alert.setTitle("Error");
			alert.setHeaderText("Event Processing");
			alert.showAndWait();

			// Clears fields and check-boxes.
			emailField.clear();
			for (int i = 0; i < listSize; ++i)
				checkBoxList[i].setSelected(false);
				return;
		}
		// Updates the event registration with alert.
		if ( eventSelect == true) {
			
			// Sets the number of participants.
			for (int i = 0; i < listSize; ++i) {
				countLabelList[i].setText(Integer.toString(countList[i]));
                
			}
			Alert alert = new Alert(Alert.AlertType.INFORMATION, emailField.getText() + eventList);
			alert.setTitle("Message");
			alert.setHeaderText("Thanks you for the registration!");
			alert.showAndWait();
			emailField.clear();
			
			eventList = "";
		}
		// Returns with error box if no event was selected.
		else {
			Alert alert = new Alert(AlertType.ERROR, "Please select at least one event.");
			alert.setTitle("Error");
			alert.setHeaderText("Event Processing");
			alert.showAndWait();
			return;
		}
	}
	
	@Override
	public void start(Stage applicationStage) {
		Scene scene = null; // Scene contains all content
		GridPane gridPane = null; // Positions components within scene

		gridPane = new GridPane(); // Create an empty pane
		scene = new Scene(gridPane); // Create scene containing the grid pane

// LABELS
		eventLabel = new Label("Event");
		countLabel = new Label("# of Participants");
		selectLabel = new Label("Select");
		emailLabel = new Label("Enter your email:");
// TEXTFIELD
		emailField = new TextField();
		emailField.setPrefColumnCount(15);
		emailField.setEditable(true);

// BUTTONS
		registerButton = new Button("Register");

// GRIDPANE
		gridPane.setPadding(new Insets(10, 10, 10, 10)); 
		gridPane.setHgap(10); 
		gridPane.setVgap(10); 
		gridPane.add(eventLabel, 0, 0);
		gridPane.add(countLabel, 1, 0);
		gridPane.add(selectLabel, 2, 0);
		gridPane.add(emailLabel, 0, listSize + 1);
		gridPane.add(emailField, 1, listSize + 1);
		gridPane.add(registerButton, 2, listSize + 1);
		
		// Formats layout of lists.
		for (int i = 0; i < listSize; i++) {

			listEvents[i] = new Label(eventNameList[i]);
			countLabelList[i] = new Label(Integer.toString(countList[i]));
			checkBoxList[i] = new CheckBox();
			checkBoxList[i].setStyle("-fx-border-color: lightblue; ");

			gridPane.add(listEvents[i], 0, i + 1);
			gridPane.add(countLabelList[i], 1, i + 1);
			gridPane.add(checkBoxList[i], 2, i + 1);
		}
		
// EVENT CALL
// Checks conditions of email and check boxes when "register" button is pressed.
		registerButton.setOnAction(e -> processRegistration());

		applicationStage.setScene(scene);
		applicationStage.setTitle("DB08 | Event Registration"); 
		applicationStage.show();
	}

	public static void main(String[] args) {
		launch(args); // Launch application
	}
}