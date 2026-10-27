from flask import Flask

app = Flask(__name__)

@app.route('/')
def employee():
    details = ["JACK", 101, "IT", 25000]

    return (
        "Employee Name: " + details[0] +
        "<br>Employee ID: " + str(details[1]) +
        "<br>Department: " + details[2] +
        "<br>Salary: Rs. " + str(details[3])
    )

if __name__ == '__main__':
    app.run(debug=True)