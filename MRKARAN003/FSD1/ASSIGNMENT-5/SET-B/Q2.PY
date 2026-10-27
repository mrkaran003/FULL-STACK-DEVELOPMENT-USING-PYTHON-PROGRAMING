from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def feedback():
    if request.method == 'POST':
        name = request.form['name']
        rating = request.form['rating']
        comments = request.form['comments']

        return (
            "Name: " + name +
            "<br>Rating: " + rating +
            "<br>Comments: " + comments
        )

    return '''
    <form method="post">
        Name: <input type="text" name="name" required><br><br>

        Rating:
        <select name="rating">
            <option value="1">1</option>
            <option value="2">2</option>
            <option value="3">3</option>
            <option value="4">4</option>
            <option value="5">5</option>
        </select><br><br>

        Comments: <textarea name="comments" required></textarea><br><br>

        <input type="submit" value="Submit Feedback">
    </form>
    '''

if __name__ == '__main__':
    app.run(debug=True)