import mariadb

# Execute a specific SQL query
def execute_query(cur):
    """Executes a specific SQL query to retrieve data from the database"""

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

def show_tables(cur):
    """Retrieves the list of tables from the database"""

    table_list = []

    # Retrieve Contacts
    cur.execute("SHOW TABLES")

    for (table,) in cur.fetchall():
        table_list.append(table)

    return table_list

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

# Get field info from cursor
def get_table_field_info(cur, table):
    """Retrieves the field info associated with a table"""

    # Fetch Table Information
    cur.execute(f"SELECT * FROM {table} LIMIT 1")

    field_info_text = get_field_info(cur)

    return field_info_text


try:
    conn = mariadb.connect(
        user='bert',
        password='password',
        host="localhost",
        database="project"
    )
    cur = conn.cursor()

    # Prints all the tables and their description in the database
    print("All the tables in database");
    tables = show_tables(cur)
    for table in tables:
        field_info_text = get_table_field_info(cur, table)

        print(f"Columns in table {table}:")
        print("\n".join(field_info_text))
        print("\n")

    # Fetch and display data
    for table in tables:
        cur.execute(f"SELECT * FROM {table}")
        rows = cur.fetchall()

        print(f"Data in table {table}:")
        for row in rows:
            print(row)


    # Execute the query to retrieve data
    records = execute_query(cur)
    column_descriptions = get_field_info(cur)

    # Display column descriptions
    print()
    print("Query column attributes:")
    for description in column_descriptions:
        print(description)

    # Display data
    print()
    print("Query data:")
    for row in records:
        print(row)

    conn.close()

except Exception as e:
    print(f"Error: {e}")

