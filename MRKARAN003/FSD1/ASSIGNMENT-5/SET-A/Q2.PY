from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def addition():
    if request.method == 'POST':
        a = int(request.form['num1'])
        b = int(request.form['num2'])
        return "Addition = " + str(a + b)

    return '''
    <form method="post">
        First Number: <input type="number" name="num1"><br><br>
        Second Number: <input type="number" name="num2"><br><br>
        <input type="submit" value="Add">
    </form>
    '''

if __name__ == '__main__':
    app.run(debug=True)