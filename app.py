from flask import Flask, render_template, redirect, url_for, session, request, jsonify
import json
from pathlib import Path

app = Flask(__name__)
app.secret_key = 'secret123'  # required for sessions

# Load products
with open(Path('products.json')) as f:
    products = json.load(f)

@app.route('/')
def index():
    return render_template('index.html', products=products)

@app.route('/add_to_cart/<int:product_id>')
def add_to_cart(product_id):
    # Initialize cart if not in session
    if 'cart' not in session:
        session['cart'] = []

    # Find product
    product = next((p for p in products if p['id'] == product_id), None)
    if product:
        session['cart'].append(product)
        session.modified = True

    return redirect(url_for('index'))

@app.route('/cart')
def cart():
    cart_items = session.get('cart', [])
    total = sum(item['price'] for item in cart_items)
    return render_template('cart.html', cart_items=cart_items, total=total)

@app.route('/clear_cart')
def clear_cart():
    session.pop('cart', None)
    return redirect(url_for('cart'))

if __name__ == '__main__':
    app.run(debug=True)
