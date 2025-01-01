#!/usr/bin/python3

import MySQLdb
from sys import argv

if __name__ == "__main__":
    """
    script that lists all cities from hbtn_0e_usa database
    """
    db = MySQLdb.connect(host="Localhost",
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])

    cursor = db.cursor()
    cursor.execute("""
                   SELECT cities.id, cities.name, states.name
                   FROM cities
                   JOIN states ON cities.state_id = states.id
                   ORDER BY cities.id ASC
                   """)

    query_rows = cursor.fetchall()
    for row in query_rows:
        print(row)

    cursor.close()
    db.close()
