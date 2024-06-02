import sqlite3

with sqlite3.connect("db_4.db") as con:
    cur = con.cursor()

    cur.execute("""
    SELECT *
    FROM Ware
    ORDER BY Price DESC
    LIMIT 2, 5
    """)

    # # res = cur.fetchall()  #  [(), ()]
    # # res = cur.fetchone()  # ()
    # res = cur.fetchmany(100)
    # print(res)

    for res in cur:
        print(res)
