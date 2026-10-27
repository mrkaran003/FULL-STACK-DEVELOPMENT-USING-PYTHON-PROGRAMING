from flask import Flask
import psycopg2

app = Flask(__name__)

def db_connect():
    return psycopg2.connect(
        dbname='library1',
        user='postgres',
        password='karan',
        host='localhost',
        port='5432'
    )

@app.route('/create_table')
def create_table():
    try:
        conn = db_connect()
        cur = conn.cursor()

        cur.execute("""
            CREATE TABLE IF NOT EXISTS Books1(
                Bid SERIAL PRIMARY KEY,
                Bname VARCHAR(100),
                Bauthor VARCHAR(100),
                Bprice INT
            )
        """)

        conn.commit()
        cur.close()
        conn.close()

        return "Table created successfully"

    except Exception as e:
        return f"Error: {e}"


@app.route('/insert_books')
def insert_books():
    try:
        conn = db_connect()
        cur = conn.cursor()

        Books = [
            ("Python", "Akshata mam", 400),
            ("Java", "Rachna mam", 500),
            ("Flask", "Gauri mam", 350),
            ("Database", "Beast", 600),
            ("Cyber Security", "Karan", 700)
        ]

        cur.executemany(
            "INSERT INTO Books1 (Bname, Bauthor, Bprice) VALUES (%s, %s, %s)",
            Books
        )

        conn.commit()
        cur.close()
        conn.close()

        return "Books inserted successfully"

    except Exception as e:
        return f"Error: {e}"


@app.route('/display_books')
def display_books():
    try:
        conn = db_connect()
        cur = conn.cursor()

        cur.execute("SELECT * FROM Books")
        Books = cur.fetchall()

        cur.close()
        conn.close()

        book_list = ""

        for book in Books:
            book_list += f"Bid: {book[0]}, Bname: {book[1]}, Bauthor: {book[2]}, Bprice: {book[3]}<br>"

        return book_list

    except Exception as e:
        return f"Error: {e}"


if __name__ == '__main__':
    app.run(debug=True)