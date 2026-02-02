import mariadb
import sys

def create_table():
    try:
        # Connect to MariaDB
        conn = mariadb.connect(
            user="your_username",
            password="your_password",
            host="localhost",
            port=3306,
            database="your_database"
        )

        # Create a cursor object
        cur = conn.cursor()

        # SQL statement to create the WRITTENBY table
        sql = """
        CREATE TABLE IF NOT EXISTS WRITTENBY (
            JournalistID INT,
            ArticleID INT,
            AuthorRank INT,
            SubmissionDate DATE,
            PRIMARY KEY (JournalistID, ArticleID),
            FOREIGN KEY (JournalistID) REFERENCES Journalist(JournalistID),
            FOREIGN KEY (ArticleID) REFERENCES Article(ArticleID)
        )
        """

        # Execute the SQL statement
        cur.execute(sql)

        # Commit the changes
        conn.commit()

        print("Table created successfully")

    except mariadb.Error as e:
        print(f"Error: {e}")

    finally:
        # Close the connection
        if conn:
            conn.close()

if __name__ == "__main__":
    create_table()
