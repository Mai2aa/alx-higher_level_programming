#!/usr/bin/python3
"""list all states from the database"""
import sys
import MySQLdb


def list_states(usename, password, database):
    conn = MySQLdb.connect(host='localhost', port=3306, user=username,
                           passwd=password, db=database)
    cur = conn.cursor
    cur.execute("SELECT * FROM states ORDER BY states.id")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    cunn.close()


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    list_states(username, password, database)
