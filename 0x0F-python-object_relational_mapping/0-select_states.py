#!/usr/bin/python3
""" A script to lists all states in the mySQL
    database hbtn_0e_0_usa
"""

import MySQLdb
from sys import argv

# connecting to the database
db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3], charset="utf8"
        )
# creating a cursor
cur = db.cursor()
# executing queries
cur.execute("SELECT * FROM states ORDER BY states.id")
rows = cur.fetchall()
for row in rows:
    print(row)

cur.close()
db.close()
