import mariadb

# Execute a specific SQL query
def execute_query(cur):
    """Executes a SQL query to retrieve recorods from the database"""

    data = []

    query = """
SELECT
    employee.Name AS employee_working,
    department.Name AS department_worked,
    works.*
FROM works
JOIN department ON works.DepartmentID = department.DepartmentID
JOIN employee ON works.Employee = employee.EmployeeID
WHERE DATE(works.DateTime) = '2000-01-01';
    """
    cur.execute(query)

    for row in cur.fetchall():
        data.append(row)

    return data



# Get field info from cursor
def get_field_info(cur):
    """Retrieves the field info associated with a cursor"""

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
    in all the columns """

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


try:
    conn = mariadb.connect(
        user='bert',
        password='password',
        host="localhost",
        database="project"
    )
    cur = conn.cursor()


    # Execute the query to retrieve data
    records = execute_query(cur)
    column_headers = [description[0] for description in cur.description]
    column_descriptions = get_field_info(cur)

    # Display column descriptions
    print("\nQuery results table column attributes:")
    for description in column_descriptions:
        print(description)

    # Display query report table
    print("\nReport table:")
    report_table(column_headers, records)

    conn.close()

except Exception as e:
    print(f"Error: {e}")

