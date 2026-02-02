"""
DarnellBertAssig05.py
Bert Darnell
4-28-2024
IS3362 - John Ciarrochi
Unit 7 - Assignment 7
Script 2 of 3

This script takes a query, determines the length of each column, then outputs the records into a formatted table.
"""
import mariadb

# Execute a specific SQL query
def execute_query(cur):
    """Executes a SQL query to retrieve the records from the database."""

    data = []

    # This query returns the products and supply date, from a specific vendor.
    query = """
SELECT
    supply.RecievedDate, supply.SupplyID, supply.SupplierID,
    supplier.Name AS SupplierName, supplier.Details,
    product.Name AS ProductName, product.Description
FROM supply
JOIN product ON supply.SupplyID = product.Supply
JOIN supplier ON supply.SupplierID = supplier.SupplierID
WHERE supplier.Name = 'Vendor1'
ORDER BY supply.RecievedDate ASC, supply.SupplyID ASC;
    """
    cur.execute(query)

    for row in cur.fetchall():
        data.append(row)

    return data


# Get field info from cursor
def get_field_info(cur):
    """Retrieves the field info associated with a cursor."""

    field_info = mariadb.fieldinfo()

    field_info_text = []

    # Retrieve Column Information
    for column in cur.description:
        column_name = column[0]
        column_type = field_info.type(column)
        column_flags = field_info.flag(column)

        field_info_text.append(f"{column_name}: {column_type} {column_flags}")

    return field_info_text


# Function to print query results
def report_table(column_headers, rows):
    """The report_table function takes a query result table and
    formats the column, by determining the maximum length of each field
    in all the columns. """

    # Determine column lengths
    column_lengths = [len(header) for header in column_headers]
    for row in rows:
        for i, field in enumerate(row):
            field_length = len(str(field))  # Convert to string for consistency
            column_lengths[i] = max(column_lengths[i], field_length)

    # Calculate total width of the table
    border_dashes = sum(column_lengths) + len(column_headers) * 4

    # Print and format query report headers
    print('-' * border_dashes)
    print('| ', end='')
    for i, header in enumerate(column_headers):
        max_length = column_lengths[i]
        print(header.ljust(max_length), ' | ', end='')
    print()
    print('-' * border_dashes)

    # Print and format the record fields
    for row in rows:
        print('| ', end='')
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
        print('-' * border_dashes)


"""Driver"""
try:
    userAux = input("Enter user: ")
    passwordAux = input("Enter password: ")

    conn = mariadb.connect(
        user=userAux,
        password=passwordAux,
        host="localhost",
        database="DarnellBertProject"
    )

    cur = conn.cursor()
    # Execute the query to retrieve data
    records = execute_query(cur)
    # Gets the tables attributes
    column_descriptions = get_field_info(cur)
    # Gets the column title fields
    column_headers = [description[0] for description in cur.description]
    
    # Display the query statement
    print(f"\nSQL command: \n{cur.statement}")

    # Display column descriptions
    print("Query results table column attributes:\n")
    for description in column_descriptions:
        print(description)

    # Display query report table
    print("\nReport table for query:")
    report_table(column_headers, records)

    conn.close()
except Exception as e:
    print(f"Error: {e}")

