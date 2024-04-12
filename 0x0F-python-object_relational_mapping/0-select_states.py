#!/usr/bin/python3
import sys
import MySQLdb

def listAll(username, password, database):
    """a function that lists all the states from the database"""


    conn = MySQLdb.connect(host='localhost', port='3306', user=username, passwd=password, db=database)
    cur = conn.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
    
if __name__ == '__main__':
    sys.argv[1] = username
    
