from flask import Flask

app = Flask(__name__)

@app.route('/')
def student():
    student = {
        "Name": "ROMAN",
        "Roll No": 44,
        "Course": "B.Sc. IT",
        "Marks": 95
    }

    result = "Student Information:"

    for key, value in student.items():
        result += "<br>" + key + ": " + str(value)

    return result

if __name__ == '__main__':
    app.run(debug=True)