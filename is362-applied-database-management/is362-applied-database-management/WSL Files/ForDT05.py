''' 
ForDT05.py
Bert Darnell

Assuming it was already created and populated, 
modify all the attributes of one record in the WebPublished table,
except for the primary key.
'''
import mariadb

userAux = input ("Enter user: ")
passwordAux = input("Enter password: ")

conn = mariadb.connect (
    user = userAux,
    password = passwordAux,
    host = "localhost",
    database = "ForDT05"
    )
cur = conn.cursor()

# Article (row) to update
articleID = 'AB00931'

# Modified values for article
newWebsite = 'https://www.newsite.com'
newPublishedDate = '2024-04-11 12:34:56'

# Modify mysql statement
stmt = "UPDATE webpublished SET Website = ?, PublishedDate = ? WHERE ArticleID = ?"


# Run SQL statement
try:
    cur.execute(stmt, (newWebsite, newPublishedDate, articleID))
    print("Record updated successfully.")
except mariadb.Error as e:
    print(f"Error: {e}")

conn.commit()
conn.close()
