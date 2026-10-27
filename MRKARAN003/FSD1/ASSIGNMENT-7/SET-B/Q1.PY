
from flask import Flask, request, jsonify

app = Flask(__name__)

products = [
    {"name": "Laptop", "price": 50000},
    {"name": "Mobile", "price": 20000},
    {"name": "Headphones", "price": 1500}
]

@app.route('/products', methods=['GET'])
def get_products():
    return jsonify(products)

@app.route('/addproduct', methods=['POST'])
def add_product():
    data = request.get_json()

    if not data or not data.get('name') or 'price' not in data:
        return jsonify({
            "msg": "Product Name and Price are required"
        }), 400

    product = {
        "name": data['name'],
        "price": data['price']
    }

    products.append(product)

    return jsonify({
        "msg": "Product added successfully",
        "product": product
    }), 201

if __name__ == '__main__':
    app.run(debug=True)
