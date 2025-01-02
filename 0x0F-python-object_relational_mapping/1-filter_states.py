#!/usr/bin/python3
"""
Script that lists all states with a name starting with N
from the database hbtn_0e_0_usa
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
    cursor.execute(f"SELECT * from states WHERE name LIKE 'N%' ORDER BY id ASC")

    states = cursor.fetchball()

    for state in states:
        if state[1][0] == 'N':
            print(state)

    cursor.close()
    db.close()
