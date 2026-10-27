from flask import Flask, request, render_template, redirect
import psycopg2

app = Flask(__name__)

# Connect to database
def db_connect():
    return psycopg2.connect(
        dbname="setc_studentdb",
        user="postgres",
        password="karan",
        host="localhost",
        port="5432"
    )


# Create Student table
def create_table():
    con = db_connect()
    cur = con.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS Student (
            Student_ID SERIAL PRIMARY KEY,
            Name VARCHAR(100),
            Course VARCHAR(100)
        )
    """)

    con.commit()
    cur.close()
    con.close()


# Add student
@app.route("/", methods=["GET", "POST"])
def add_student():
    if request.method == "POST":
        name = request.form["Name"]
        course = request.form["Course"]

        con = db_connect()
        cur = con.cursor()

        cur.execute(
            "INSERT INTO Student (Name, Course) VALUES (%s, %s)",
            (name, course)
        )

        con.commit()
        cur.close()
        con.close()

        return redirect("/display")

    return render_template("ADD.HTML")


# Display students
@app.route("/display")
def display_students():
    con = db_connect()
    cur = con.cursor()

    cur.execute("SELECT * FROM Student ORDER BY Student_ID")
    students = cur.fetchall()

    cur.close()
    con.close()

    return render_template("DISPLAY.HTML", students=students)


# Update student
@app.route("/update", methods=["GET", "POST"])
def update_student():
    if request.method == "POST":
        sid = request.form["Student_ID"]
        name = request.form["Name"]
        course = request.form["Course"]

        con = db_connect()
        cur = con.cursor()

        cur.execute(
            "UPDATE Student SET Name=%s, Course=%s WHERE Student_ID=%s",
            (name, course, sid)
        )

        updated = cur.rowcount
        con.commit()
        cur.close()
        con.close()

        if updated:
            return redirect("/display")

        return "Student ID not found!"

    return render_template("UPDATE.HTML")


# Delete student
@app.route("/delete", methods=["GET", "POST"])
def delete_student():
    if request.method == "POST":
        sid = request.form["Student_ID"]

        con = db_connect()
        cur = con.cursor()

        cur.execute(
            "DELETE FROM Student WHERE Student_ID=%s",
            (sid,)
        )

        deleted = cur.rowcount
        con.commit()
        cur.close()
        con.close()

        if deleted:
            return redirect("/display")

        return "Student ID not found!"

    return render_template("DELETE.HTML")


if __name__ == "__main__":
    create_table()
    app.run(debug=True, use_reloader=False, port=5001)
