#!/usr/bin/python3
"""List from table state"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    mysql_username = argv[1]
    mysql_password = argv[2]
    database_name = argv[3]
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        db=database_name,
        charset="utf8"
    )
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY states.id ASC")
    rows = cursor.fetchall()
    for row in rows:
        # Decode and cast each column appropriately
        decoded_row = (
            int(row[0]),
            row[1].decode('utf-8') if isinstance(row[1], bytes) else row[1]
        )
        print(decoded_row)
    cursor.close()
    db.close()
