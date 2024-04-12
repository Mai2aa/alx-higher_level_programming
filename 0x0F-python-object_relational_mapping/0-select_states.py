#!/usr/bin/python3
import sys
import MySQLdb


if __name__ == '__main__':
    """a function that lists all the states from the database"""
    conn = MySQLdb.connect(host='localhost', port='3306', user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3])
    cur = conn.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    conn.close()
