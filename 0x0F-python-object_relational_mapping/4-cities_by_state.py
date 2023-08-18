#!/usr/bin/python3
"""
a script that lists all cities from the database
hbtn_0e_4_usa
"""
import MySQLdb
import sys


def main():
    """
    function to lists all cities database
    hbtn_0e_4_usa
    """
    if len(sys.argv) != 4:
        return

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name\
                FROM cities\
                JOIN states\
                ON cities.state_id = states.id\
                ORDER BY cities.id")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)

    cur.close()
    db.close()


if __name__ == "__main__":
    main()
