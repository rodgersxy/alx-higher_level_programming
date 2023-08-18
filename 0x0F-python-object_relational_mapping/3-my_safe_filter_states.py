#!/usr/bin/python3
"""
a sript that is safe from MySQL injections!
"""
import MySQLdb
import sys


def main():
    """
    -a script that is safe from MySQL injections!
    -query to prevent SQL injection
    """
    if len(sys.argv) != 5:
        return

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    cur = db.cursor()

    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cur.execute(query, (sys.argv[4],))
    query_rows = cur.fetchall()

    for row in query_rows:
        print(row)
    cur.close()
    db.close()


if __name__ == "__main__":
    main()
