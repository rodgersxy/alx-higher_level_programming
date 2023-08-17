#!/usr/bin/python3
"""
a script that lists all states from the database hbtn_0e_0_usa:
"""
import MySQLdb
import sys


def list_states():
    """
    list's allthe states from hbtn_0e_0_usa database,
    connnect with MySQL server
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
        print(elem)

    db.close()


if __name__ == "__main__":
    list_states()
