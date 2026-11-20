import sqlite3

# Connect to database
connection = sqlite3.connect("table.db")

# Create cursor
cursor = connection.cursor()

# Create table if it doesn't exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER
)
""")

# Delete old records
cursor.execute("DELETE FROM students")

# Insert information
cursor.execute("""
INSERT INTO students (name, age)
VALUES ('Doaa', 20)
""")

# Query to view tables
cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
tables = cursor.fetchall()

print("Tables in the database:")
for table in tables:
    print(table[0])

# Save changes
connection.commit()

# Display students
cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()

print("\nStudents table:")
for row in rows:
    print(row)

# Close database connection
connection.close()
