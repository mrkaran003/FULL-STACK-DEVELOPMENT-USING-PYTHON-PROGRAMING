from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        name = request.form['name']
        return "Student Name: " + name

    return '''
    <form method="post">
        Enter Student Name:
        <input type="text" name="name">
        <input type="submit" value="Submit">
    </form>
    '''

if __name__ == '__main__':
    app.run(debug=True)