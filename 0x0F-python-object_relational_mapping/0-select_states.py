#!/usr/bin/python3
import sys
import MySQLdb


def listAll(username, password, database):
    """a function that lists all the states from the database"""
    conn = MySQLdb.connect(host='localhost', port='3306',
                           user=username, passwd=password, db=database)
    cur = conn.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    conn.close()


if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    listAll(username, password, database)
