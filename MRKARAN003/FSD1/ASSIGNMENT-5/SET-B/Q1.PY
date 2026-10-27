from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def employee():
    if request.method == 'POST':
        name = request.form['name']
        emp_id = request.form['emp_id']
        department = request.form['department']

        return (
            "Employee Name: " + name +
            "<br>Employee ID: " + emp_id +
            "<br>Department: " + department
        )

    return '''
    <form method="post">
        Employee Name: <input type="text" name="name" required><br><br>
        Employee ID: <input type="text" name="emp_id" required><br><br>
        Department: <input type="text" name="department" required><br><br>
        <input type="submit" value="Submit">
    </form>
    '''

if __name__ == '__main__':
    app.run(debug=True)