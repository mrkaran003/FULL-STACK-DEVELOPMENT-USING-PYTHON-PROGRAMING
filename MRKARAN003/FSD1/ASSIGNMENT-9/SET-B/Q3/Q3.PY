from flask import Flask, request, render_template, redirect
import psycopg2

app = Flask(__name__)

# Connect to database
def get_connect():
    return psycopg2.connect(
        dbname="setb_student",
        user="postgres",
        password="karan",
        host="localhost",
        port="5432"
    )


# Create Student table
def create_table():
    con = get_connect()
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


# Insert and display students
@app.route("/student", methods=["GET", "POST"])
def student():
    con = get_connect()
    cur = con.cursor()

    if request.method == "POST":
        name = request.form.get("Name")
        course = request.form.get("Course")

        cur.execute(
            "INSERT INTO Student (Name, Course) VALUES (%s, %s)",
            (name, course)
        )

        con.commit()
        cur.close()
        con.close()

        return redirect("/student")

    cur.execute("SELECT * FROM Student ORDER BY Student_ID")
    students = cur.fetchall()

    cur.close()
    con.close()

    return render_template("Q3.HTML", students=students)


# Update student's course using Student ID
@app.route("/update", methods=["POST"])
def update_course():
    student_id = request.form.get("Student_ID")
    course = request.form.get("New_Course")

    con = get_connect()
    cur = con.cursor()

    cur.execute(
        "UPDATE Student SET Course = %s WHERE Student_ID = %s",
        (course, student_id)
    )

    updated = cur.rowcount
    con.commit()

    cur.close()
    con.close()

    if updated:
        return redirect("/student")

    return "Student ID not found. Go back and check the ID."


if __name__ == "__main__":
    create_table()
    app.run(debug=True, use_reloader=False)
