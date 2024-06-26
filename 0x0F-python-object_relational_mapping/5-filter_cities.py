#!/usr/bin/python3
""" A  script that takes in the name of a state as an
    argument and lists all cities of that state, using
    the database hbtn_0e_4_usa
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=argv[1],
            passwd=argv[2],
            db=argv[3],
            charset="utf8"
            )
    cur = db.cursor()
    cur.execute(
            "SELECT cities.name FROM cities INNER JOIN states\
                    ON cities.state_id = states.id\
                    WHERE states.name = %s\
                    ORDER BY cities.id ASC", (argv[4], )
                    )
    rows = cur.fetchall()
    num_cities = len(rows)
    count = 0
    for row in rows:
        for col in row:
            print(f"{col}, ", end="") if count < num_cities-1 else print(col)
        count += 1

    cur.close()
    db.close()
