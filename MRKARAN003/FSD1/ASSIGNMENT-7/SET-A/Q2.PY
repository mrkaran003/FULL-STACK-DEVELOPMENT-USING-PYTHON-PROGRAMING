from flask import Flask, request, jsonify

app = Flask(__name__)

employee = {
    "name": "JARVICE",
    "department": "CYBER SECURITY"
}

@app.route('/employee', methods=['GET'])
def get_employee():
    return jsonify(employee)

@app.route('/addemployee', methods=['POST'])
def add_employee():
    data = request.get_json()

    return jsonify({
        "message": "Employee added successfully",
        "name": data["name"],
        "department": data["department"]
    }), 201

if __name__ == '__main__':
    app.run(debug=True)