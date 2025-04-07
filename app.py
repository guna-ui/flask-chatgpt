from flask import Flask,jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to ShopCartX API!"

@app.route('/api/products',methods=['GET'])
def getproducts():
    products = [
        {"id": 1, "name": "T-shirt", "price": 499},
        {"id": 2, "name": "Jeans", "price": 999},
        {"id": 3, "name": "Sneakers", "price": 1999}
    ]
    return jsonify(products)

if __name__=='__main__':
    app.run(debug=True)