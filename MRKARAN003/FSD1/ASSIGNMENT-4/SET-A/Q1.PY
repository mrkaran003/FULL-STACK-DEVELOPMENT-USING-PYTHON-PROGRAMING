from flask import Flask

app = Flask(__name__)

@app.route('/home')
def home():
    return "Welcom to Home Page"

@app.route('/about')
def about():
    return "Welcom to About Page"

if __name__ == "__main__":
    app.run(debug=True)