import sqlite3

cars_list = [
    ('Toyota', 36500),
    ('Chevrolet', 87625),
    ('Nissan', 26891),
    ('Nissan', 167422),
    ('Honda', 59875)
]

with sqlite3.connect("car.db") as con:
    cur = con.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS cars
        (
        car_id INTEGER PRIMARY KEY AUTOINCREMENT,
        model TEXT,
        price INTEGER
        )
    """)

    cur.executescript("""
    DELETE FROM cars WHERE model LIKE 'N%';
    UPDATE cars SET price = price + 100;
    """)

    # cur.execute("UPDATE cars SET price = :Price where model LIKE 'N%'", {'Price': 0})

    # cur.executemany("INSERT INTO cars VALUES(NULL, ?, ?)", cars_list)

    # for car in cars_list:
    #     cur.execute("INSERT INTO cars VALUES(NULL, ?, ?)", car)

    # cur.execute("INSERT INTO cars VALUES(1, 'Renault', 22000)")
    # cur.execute("INSERT INTO cars VALUES(2, 'Dodge', 100000)")
    # cur.execute("INSERT INTO cars VALUES(3, 'Mitsubishi', 57749)")
    # cur.execute("INSERT INTO cars VALUES(4, 'Toyota', 76525)")
    # cur.execute("INSERT INTO cars VALUES(5, 'Subaru', 127126)")
