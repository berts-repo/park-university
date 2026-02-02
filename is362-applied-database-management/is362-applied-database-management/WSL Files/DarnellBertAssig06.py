"""
DarnellBertAssig05.py
Bert Darnell
IS3362 - John Ciarrochi
Unit 6 - Assignment 6

This script takes a query, determines the length of each column, then outputs the records into a formatted table.
"""
import mariadb

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
        SELECT * FROM trip
        JOIN vehicle ON trip.VehicleAssigned = vehicle.NumberPlate
        JOIN driver ON trip.DriverAssigned = driver.DocumentID
        WHERE driver.CommissionPerTrip > 1
    """
    cur.execute(query)

    # Fetch column headers and initialize the table cell lengths
    column_headers = [description[0] for description in cur.description]
    column_lengths = [len(header) for header in column_headers]

    # Fetch the records and determine column lengths
    rows = cur.fetchall()
    for row in rows:
        for i, field in enumerate(row):
            field_length = len(str(field)) #String for consistency
            column_lengths[i] = max(column_lengths[i], field_length)

    # Calculate total width of the table
    borderDashes = sum(column_lengths) + len(column_headers) * 4

    # Print table borders
    print('-' * borderDashes)
    print('| ', end='')
    # Print headers for each column
    for i, header in enumerate(column_headers):
        max_length = column_lengths[i]
        header = header[:max_length]
        print(header.ljust(max_length), ' | ', end='')
    print()
    print('-' * borderDashes)

    # Print the records (rows)
    for row in rows:
        print('| ' , end='')
        for i, field in enumerate(row):
            str_field = str(field)
            max_length = column_lengths[i]

            if type(field) == str:
                str_field = str_field[:max_length].ljust(max_length)
            elif type(field) in [int, float]:
                f = "{:" + str(max_length) + "}"
                str_field = f.format(str_field).ljust(max_length)
            print(str_field, ' | ', end='')
        print()
        print('-' * borderDashes)

    print('Number of columns found:', len(column_headers))
    print('Number of records found:', cur.rowcount)

except mariadb.Error as e:
    print(f"Error: {e}")

conn.close()

