from flask import Flask,jsonify,request

app = Flask(__name__)

products = [
        {"id": 1, "name": "T-shirt", "price": 499},
        {"id": 2, "name": "Jeans", "price": 999},
        {"id": 3, "name": "Sneakers", "price": 1999}
    ]

@app.route('/')
def home():
    return "Welcome to ShopCartX API!"

@app.route('/api/products',methods=['GET'])
def getproducts():
    
    return jsonify(products)

@app.route('/api/products/<int:productid>',methods=['GET'])
def getproductbyid(productid):
    product=next((p for p in products if p['id']==productid),None)
    if product:
        return jsonify({"products":product})
    else:
        return jsonify({"message":"product not found"}),404
    
@app.route('/api/products',methods=['POST'])
def add_product():
    data=request.get_json()
    
    if not data or not all(k in data for k in ("name","price")):
        return jsonify({"error":"Invalid response"})
    
    new_id=max([p['id'] for p in products])+1
    new_products={
        "id":new_id,
        "name":data["name"],
        "price":data["price"]
    }
    products.append(new_products)
    return jsonify(new_products),201

if __name__=='__main__':
    app.run(debug=True)