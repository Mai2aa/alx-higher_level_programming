#!/usr/bin/python3
"""Displays values in states that matches the name of the argument passed"""
import sys
import MySQLdb


if __name__ == '__main__':
    conn = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3])
    cur = conn.cursor()
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    state_name = sys.argv[4]
    cur.execute(query, (state_name,))
    rows = cur.fetchall()
    for row in rows:
        print(row)
