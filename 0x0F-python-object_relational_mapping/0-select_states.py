#!/usr/bin/env python3
"""List from table state"""
import MySQLdb
import sys

# Replace these values with your actual database credentials
mysql_username = sys.argv[1]
mysql_password = sys.argv[2]
database_name = sys.argv[3]

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        db=database_name,
        charset="utf8",
    )

    # Create a cursor object to interact with the database
    cursor = db.cursor()

    # Execute a query
    cursor.execute("SELECT * FROM states ORDER BY states.id ASC")

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    # Close the cursor and connection
    cursor.close()
    db.close()
