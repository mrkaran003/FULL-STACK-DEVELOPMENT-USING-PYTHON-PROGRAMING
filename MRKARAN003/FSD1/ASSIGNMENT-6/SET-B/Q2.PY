from flask import Flask

app = Flask(__name__)

@app.route('/')
def employees():
    employees = [
        {"Name": "PRIYA", "ID": 101, "Department": "IT"},
        {"Name": "JANAVI", "ID": 102, "Department": "HR"},
        {"Name": "JACK", "ID": 103, "Department": "Sales"},
        {"Name": "KARAN", "ID": 104, "Department": "Finance"},
        {"Name": "VEDIKA", "ID": 105, "Department": "IT"}
    ]

    result = "Employee Details:"

    for emp in employees:
        result += (
            "<br><br>Name: " + emp["Name"] +
            "<br>ID: " + str(emp["ID"]) +
            "<br>Department: " + emp["Department"]
        )

    return result

if __name__ == '__main__':
    app.run(debug=True)