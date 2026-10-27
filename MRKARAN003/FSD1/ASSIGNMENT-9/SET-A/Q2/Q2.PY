from flask import Flask, request, render_template, redirect
import psycopg2

app = Flask(__name__)

# Connect to database
def get_connect():
    return psycopg2.connect(
        dbname="employeedb",
        user="postgres",
        password="karan",
        host="localhost",
        port="5432"
    )

# Create Employee table
def create_table():
    con = get_connect()
    cur = con.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS Employees (
            Emp_ID SERIAL PRIMARY KEY,
            Name VARCHAR(100),
            Department VARCHAR(100)
        )
    """)

    con.commit()
    cur.close()
    con.close()

# Insert and display employees
@app.route("/employee", methods=["GET", "POST"])
def employee():
    con = get_connect()
    cur = con.cursor()

    if request.method == "POST":
        name = request.form.get("Name")
        department = request.form.get("Department")

        cur.execute(
            "INSERT INTO Employees (Name, Department) VALUES (%s, %s)",
            (name, department)
        )

        con.commit()
        return redirect("/employee")

    cur.execute("SELECT * FROM Employees ORDER BY Emp_ID")
    employees = cur.fetchall()

    cur.close()
    con.close()

    return render_template("Q2.HTML", employees=employees)

if __name__ == "__main__":
    create_table()
    app.run(debug=True, use_reloader=False)
