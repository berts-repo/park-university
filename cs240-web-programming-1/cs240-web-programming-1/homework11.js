/* Unit 7 */
/***************************************************************************/

class AIApplication {
  constructor(row) {
    this.row = row;               // table's row element and
    this.rowIndex = row.rowIndex; // last selected index
    for (let i=0; i<5; i++) {
      form.elements[i].value = row.childNodes[i].innerHTML;
    }
    // Set the values for yearCreated and shortURL fields
    form.elements[5].value = row.childNodes[5].innerHTML; // Year Created (6th column)
    form.elements[6].value = row.childNodes[6].innerHTML; // Short URL (7th column)
    app = this;
  } // end constructor

  //***************************************************************    
  // Update arrays and displayed table
  replaceApp() {
    for (let i=0; i<5; i++) {
      apps[this.rowIndex-1][i] = form.elements[i].value;
    }
    fillTable(); // resort and repopulate in case address changed
    cancel();
  } // end replaceApp

  // Remove current app from apps array and from table
  deleteApp() {
    table.deleteRow(this.rowIndex); // Remove the row from the table
    apps.splice(this.rowIndex - 1, 1); // Remove the app from the apps array
    cancel(); // Clear the form
    app = ""; // Reset the app variable
  } // end deleteApp
} // end class AIApplication
