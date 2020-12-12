#!/usr/bin/python3
"""lists all states with a name starting with N (upper N) from the database
hbtn_0e_0_usa"""

if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id")
    rows = cur.fetchall()
    for row in rows:
        if row[1].startswith('N'):
            print(row)
    cur.close()
    db.close()
