from flask import Flask, request, jsonify
from flask_cors import CORS
from models import db, Product, Conversation

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ecom.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
CORS(app)

@app.route('/products', methods=['GET'])
def get_products():
    query = request.args.get('q', '')
    products = Product.query.filter(Product.name.ilike(f'%{query}%')).all()
    return jsonify([{
        'id': p.id,
        'name': p.name,
        'price': p.price,
        'category': p.category,
        'description': p.description,
        'image_url': p.image_url
    } for p in products])

@app.route('/chat', methods=['POST'])
def chat():
    user_msg = request.json['message']
    products = Product.query.filter(Product.name.ilike(f'%{user_msg}%')).limit(3).all()

    if products:
        bot_response = f"Here are {len(products)} matching product(s) for '{user_msg}'"
    else:
        bot_response = "Sorry, no matching products found."

    conv = Conversation(user_message=user_msg, bot_response=bot_response)
    db.session.add(conv)
    db.session.commit()

    return jsonify({
        'response': bot_response,
        'products': [{
            'name': p.name,
            'price': p.price,
            'image_url': p.image_url
        } for p in products]
    })

if __name__ == '__main__':
    app.run(debug=True)
