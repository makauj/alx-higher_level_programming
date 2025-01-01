#!/usr/bin/python3
"""
script to safely filter states
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    """
    list states by id
    """
    db = MySQLdb.connect(host="Localhost",
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])

    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name = '{}' ORDER BY id ASC"
                   .format(argv[4]))

    query_rows = cursor.fetchall()
    for row in query_rows:
        print(row)

    cursor.close()
    db.close()
