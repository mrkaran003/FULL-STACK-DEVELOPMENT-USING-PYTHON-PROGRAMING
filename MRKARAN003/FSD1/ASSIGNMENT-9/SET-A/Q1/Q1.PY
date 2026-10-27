
from flask import Flask, request, render_template, redirect
import psycopg2

app = Flask(__name__)

# Connect to database
def get_connect():
    conn = psycopg2.connect(
        dbname="studentdb",
        user="postgres",
        password="karan",
        host="localhost",
        port="5432"
    )
    return conn


# Create Student1 table
def create_table():
    con = get_connect()
    cur = con.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS Student1 (
            Student_ID SERIAL PRIMARY KEY,
            Name VARCHAR(100),
            Course VARCHAR(100)
        )
    """)

    con.commit()
    cur.close()
    con.close()


# Student route
@app.route('/student', methods=['GET', 'POST'])
def student():
    con = get_connect()
    cur = con.cursor()

    if request.method == 'POST':
        name = request.form.get("Name")
        course = request.form.get("Course")

        cur.execute(
            "INSERT INTO Student1 (Name, Course) VALUES (%s, %s)",
            (name, course)
        )

        con.commit()
        cur.close()
        con.close()

        return redirect('/student')

    cur.execute("SELECT * FROM Student1 ORDER BY Student_ID")
    students = cur.fetchall()

    cur.close()
    con.close()

    return render_template("Q1.HTML", students=students)


if __name__ == '__main__':
    create_table()
    app.run(debug=True, use_reloader=False)
