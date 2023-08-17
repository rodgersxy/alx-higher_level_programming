#!/usr/bin/python3
"""
a script that lists all states with a name starting with
N (upper N) from the database hbtn_0e_0_usa:
"""

import MySQLdb
import sys


def filter_states():
    """
    function that lists all states with a name starting
    with N (upper N) from the database hbtn_0e_0_usa:
    """
    if len(sys.argv) != 4:
        return

    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    cursor = db.cursor()
    cursor.execute("SELECT * FROM states;")

    results = cursor.fetchall()
    for elem in results:
        if elem[1][0] == 'N':
            print(elem)

    db.close()


if __name__ == "__main__":
    filter_states()
