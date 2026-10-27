from flask import Flask

app = Flask(__name__)

@app.route('/contact')
def contact():
    return "welcom to contact Page"

@app.route('/services')
def services():
    return"welcome to Services Page"

if __name__ == '__main__':
    app.run(debug=True)