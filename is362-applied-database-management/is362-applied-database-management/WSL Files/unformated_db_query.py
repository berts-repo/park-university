"""
DarnellBertAssig05.py
Bert Darnell
IS3362 - John Ciarrochi
Unit 6 - Assignment 6

"""
import mariadb

# Run SQL statements
try:
    userAux = input("Enter user: ")
    passwordAux = input("Enter password: ")

    conn = mariadb.connect(
            user=userAux,
            password=passwordAux,
            host="localhost",
            database="ForAssig06"
        )
    cur = conn.cursor()

    query = """
        SELECT * FROM client
    """
    # Execute the query
    cur.execute(query)

    # Fetch column headers
    column_names = [description[0] for description in cur.description]
    print(column_names)

    # Fetch the records
    rows = cur.fetchall()
    for row in rows:
        print(row)

except mariadb.Error as e:
    print(f"Error: {e}")

conn.close()


