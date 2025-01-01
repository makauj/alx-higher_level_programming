#!/usr/bin/python3
"""
script that filters states
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])

    cursor = db.cursor()
    cursor.execute("SELECT * from states WHERE name LIKE 'N%' ORDER BY id ASC")

    query_rows = cursor.fetchball()

    for row in query_rows:
        print(row)

    cursor.close()
    db.close()
