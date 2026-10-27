from flask import Flask

app = Flask(__name__)

@app.route('/product/<int:product_id>')
def product(product_id):
    return "Product ID: " + str(product_id) + \
           "<br>Product Name: Laptop" + \
           "<br>Price: Rs. 50000"

if __name__ == '__main__':
    app.run(debug=True)