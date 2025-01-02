#!/usr/bin/python3
"""
Script that takes in an argument and displays all
states where the name matches the argument
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
    )

    cursor = db.cursor()
    q = f"SELECT * FROM states WHERE name = '{argv[4]}' ORDER BY id ASC"
    cursor.execute(q)

    states = cursor.fetchall()
    for state in states:
        print(state)

    cursor.close()
    db.close()
