import mariadb

# Get list of tables
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

    conn.close()

except Exception as e:
    print(f"Error: {e}")
