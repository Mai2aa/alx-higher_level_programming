#!/usr/bin/python3
"""list all states from the database"""
import sys
import MySQLdb


if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    try:
        conn = MySQLdb.connect(host='localhost', port=3306, user=username,
                               passwd=password, db=database)

    except MySQLdb.Error as e:
        print("Can't connect with the database: {}".format(e))
        sys.exit(1)
    cur = conn.cursor()
    cur.execute("SELECT * FROM states")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
