/*
Will check if the inputted first name is in the class roster, it will then print if the search was successful or not. This program will utilize a scene with GridPane, with 2 labels, two fields, and a button. When the search button is pressed it with compare the user-inputted name to the names in class roster, and output that into the result field. This program is case sensitive.
*/

import javafx.application.Application;
import javafx.geometry.Insets;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.control.TextField;
import javafx.scene.layout.GridPane;
import javafx.stage.Stage;

import java.util.Arrays;
import java.util.ArrayList;

public class Check4FirstName extends Application {
        private Label name;                     // Label for name input.
        private Label result;               // Label for search result.
        private TextField inputName;    // Displays input name.
        private TextField searchResult; // Displays the search result.
        private Button searchButton;    // Triggers search.

// Class roster list
        ArrayList<String> nameList = new ArrayList<String>(
            Arrays.asList("Uriel", "Bert", "Kenneth", "Austin",
                                "Eric", "Muhammad", "Nathan", "Megan", "Kartikkumar",
                                "Justin", "Kisha", "Javier", "David"));

// Scene
   @Override
   public void start(Stage applicationStage) {
      Scene scene = null;         // Scene contains all content
      GridPane gridPane = null;   // Positions components within scene

      gridPane = new GridPane();   // Create an empty pane
      scene = new Scene(gridPane); // Create scene containing the grid pane

// Labels
      name = new Label("Enter first name: ");
      result = new Label("Results: ");

// Fields
      searchResult = new TextField();
      searchResult.setPrefColumnCount(15);
      searchResult.setEditable(false);
      searchResult.setText("no search made..");

      inputName = new TextField();
      inputName.setPrefColumnCount(15);
      inputName.setEditable(true);
          inputName.setText("enter text..");
      inputName.setStyle("-fx-background-color: #dcdcdc; ");

// Button
      searchButton = new Button("Search");
          searchButton.setStyle("-fx-background-color: #dcdcdc; ");

// GridPane layout
      gridPane.setPadding(new Insets(10, 10, 10, 10));
          gridPane.setHgap(10);
          gridPane.setVgap(10);

      gridPane.add(name, 0, 0);
          gridPane.add(searchResult, 1, 1);
          gridPane.add(result, 0, 1);
          gridPane.add(inputName, 1, 0);
          gridPane.add(searchButton, 0, 2);

// Event handler
      searchButton.setOnAction(new EventHandler<ActionEvent>() {

                 @Override
         public void handle(ActionEvent event) {
                         String userInput;

                        // Reference variable for user-input
                        userInput = inputName.getText();

                        // Outputs found, if input name is in list
                        for (int i = 0; i < nameList.size(); i++){

                                if ( userInput.equals(nameList.get(i)) == true ){
                                        searchResult.setText("Found: " + userInput);
                                        break;}

                                else {searchResult.setText("No results found.");}
                        }
                 }
                 });

      applicationStage.setScene(scene);
          applicationStage.setTitle("Check4FirstName");
          applicationStage.show();
   }

   public static void main(String [] args) {
      launch(args); // Launch application
   }
}