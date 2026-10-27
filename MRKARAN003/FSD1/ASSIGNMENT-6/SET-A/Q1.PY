from flask import Flask

app = Flask(__name__)

@app.route('/')
def student():
    name = "Karan"
    marks = [80, 75, 90]

    total = sum(marks)
    average = total / len(marks)

    return (
        "Student Name: " + name +
        "<br>Marks: " + str(marks) +
        "<br>Total Marks: " + str(total) +
        "<br>Average Marks: " + str(average)
    )

if __name__ == '__main__':
    app.run(debug=True)