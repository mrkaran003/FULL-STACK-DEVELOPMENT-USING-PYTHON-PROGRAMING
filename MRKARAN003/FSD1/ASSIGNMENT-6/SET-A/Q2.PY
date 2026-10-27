from flask import Flask

app = Flask(__name__)

@app.route('/')
def students():
    names = ["KARAN", "BEAST", "ROMEO", "PRIYA", "VEDIKA"]

    result = "Student Names:"

    for name in names:
        result += "<br>" + name

    return result

if __name__ == '__main__':
    app.run(debug=True)