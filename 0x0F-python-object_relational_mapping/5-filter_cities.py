#!/usr/bin/python3
""" a script takes state name and list cities"""
import sys
import MySQLdb


if __name__ == "__main__":
    conn = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3])
    cur = conn.cursor()
    query = """SELECT * FROM cities
               JOIN states ON cities.state_id = states.id
               WHERE states.name=%s
               ORDER BY cities.id ASC"""
    state_name = sys.argv[4]
    cur.execute(query, (state_name,))
    rows = cur.fetchall()
    city_name = [row[2] for row in rows]
    city_list = ", ".join(city_name)
    print(city_list)
