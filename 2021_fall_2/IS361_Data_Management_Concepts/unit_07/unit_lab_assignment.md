# Unit 7: Unit Lab Assignment

**Due:** 2021-12-06T05:59:00Z
**Points Possible:** 10.0
**Submission Types:** online_upload

## Instructions

Purpose

The purpose of this assignment is to explore issues in Data Integration.

Directions

This week you are provided with a two small databases.

 [link: https://canvas.park.edu/courses/64263/files/8477419/download?verifier=FFXDwWr2LU06XmhH2SUawX0VdcnX0wbc9sYhIfRX&wrap=1] Database for Assignment 7.accdb

 [link: https://canvas.park.edu/courses/64263/files/8477424/download?verifier=5qO5XPcq5cnSAyxX6Vw3PvO1cIIhPabJN7GHNmMx&wrap=1] Purchased Books - Excel for Assignment 7.xlsx

The first one is the same Microsoft Access database you were given in Assignment 5, last week. The second one is an Excel file that that contains information about a new batch of books that was recently purchased by the bookstore that handles the first database. It also contains a client list from the old bookstore that was also acquired by the new bookstore. Your job is to integrate the information provided in the Excel file onto the current database file. To do that you must do the following:

All new books in the Excel file should be added to the Book table. If there are books that were already in the table, only the quantity should be updated. All purchased books are new.

Categories for the new books in the Excel file should match existing categories in the current database. Only Accounting, Criminal Justice, Computers, and Finance should be added as new categories that were not previously found in the database.

Book prices in Euros in the Excel file should be converted to prices in USD in the current database. The exchange rate on the purchase date was $1.00 USD per 0.8484EUR.

Author names in the Excel file should be incorporated in the Author table and appropriate references should be included in the Wrote file.

Customers from the Excel file who have all required information by the new database should be incorporated in the Customer table. New customers who were added in the current database and of whom there are purchase records should also be referenced in the Order and OrderLine files. Since no order numbers exist in the Excel File, new order numbers will be created that begin their Order number with the letter ‘Z’: Z001, Z002… etc. OrderDate and OrderDeliveryDate should be ‘12/31/2016’ for all added OrderLine records.

Deliverables

Submit the Microsoft Access database containing all the updated information the Excel file provides.

Due Date

Due by 11:59 p.m., Sunday, CT.

---

## My Submission

**Score:** 8.9/10.0
**Grade:** 8.9
**Submitted:** 2021-12-04T10:44:47Z

### Submitted Files

- **Database for Assignment 7.accdb**
  - Downloaded: `files/Database for Assignment 7.accdb`

### Instructor Feedback

**Bert** (2021-12-04T10:44:48Z):

> Hello Professor,
I ran into some problems on this assignment:
1) On excel line 3, 9  integrated to the Access ‘book’ table, the new books are going into a ‘used’ book attribute. The ‘price’ are different as well. I would propose having another used book table, different prices table, but I could be doing something wrong.
2) There was missing ISBN for the order question 5, 219017
3) There was poor data, including address's
4) I could not figure out how to change the data type for order numbers from number to text, without loosing all my data. I had just spent 4 hours on the assignment struggling

**[INSTRUCTOR] Ph.D.** (2021-12-06T22:09:58Z):

> Books table should have at least 41 records. It has only 40. [-0.1]
Prices in the database should have remain in dollars. They should not have been converted to Euros [-0.5]
Some new Authors were not linked with their books thru the Wrote table [-0.5]
