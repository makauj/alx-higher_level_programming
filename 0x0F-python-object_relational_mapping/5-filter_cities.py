#!/usr/bin/python3

import MySQLdb
from sys import argv

if __name__ == "__main__":
    """
    script that takes in the name of a state as an argument
    and lists all cities of that state
    """
    db = MySQLdb.connect(host="Localhost",
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])

    cursor = db.cursor()
    cursor.execute("""
                   SELECT cities.name
                   FROM cities
                   JOIN states ON cities.state_id = states.id
                   WHERE states.name = %s
                   ORDER BY cities.id ASC
                   """)

    query_rows = cursor.fetchall()
    print(", ".join(city[0] for city in query_rows))

    cursor.close()
    db.close()
