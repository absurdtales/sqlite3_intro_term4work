import sqlite3
user_input = input("Entery Country: ")

with sqlite3.connect("movies.db") as db:
    cursor = db.cursor()
    cursor.execute(
        f"""
        SELECT dirname
        FROM director
        WHERE country = '{user_input}'
        """
    )

    results = cursor.fetchall()

    for record in results:
        print(record[0])