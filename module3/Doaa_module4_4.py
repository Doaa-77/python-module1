
import sqlite3

# Connect to the database
conn = sqlite3.connect("tasks.db")

# Create cursor
cursor = conn.cursor()

# Get all table names
cursor.execute("""
    SELECT name FROM sqlite_master
    WHERE type='table'
""")

tables = cursor.fetchall()

# Check if tables exist
if not tables:
    print("No tables found")

else:
    # Display table names
    for table in tables:
        table_name = table[0]

        print("\nTable:", table_name)

        # Get all information from the table
        cursor.execute(f'SELECT * FROM "{table_name}"')

        rows = cursor.fetchall()

        # Display column names
        columns = [description[0] for description in cursor.description]
        print(columns)

        # Display table data
        for row in rows:
            print(row)

# Close database
conn.close()
