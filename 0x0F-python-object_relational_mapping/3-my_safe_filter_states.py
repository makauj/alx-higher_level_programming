#!/usr/bin/python3
"""
Script that safely takes in an argument and displays all
states where the name matches the argument
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="Localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
    )

    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE %s ORDER BY \
        id ASC", (argv[4],))

    states = cursor.fetchall()
    for state in states:
        print(state)

    cursor.close()
    db.close()
