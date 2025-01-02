#!/usr/bin/python3
"""
Script that lists all cities of a given state from the database hbtn_0e_4_usa
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":

    db = MySQLdb.connect(host="Localhost",
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])

    cursor = db.cursor()
    query = """
             SELECT cities.name
             FROM cities
             JOIN states ON cities.state_id = states.id
             WHERE states.name LIKE %s
             ORDER BY cities.id ASC
    """
    cursor.execute(query, (argv[4],))

    states = cursor.fetchall()
    print(", ".join(city[0] for city in states))

    cursor.close()
    db.close()
