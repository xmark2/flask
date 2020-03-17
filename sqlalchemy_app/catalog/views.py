from flask import request, jsonify, Blueprint
from sqlalchemy_app import app, db
from sqlalchemy_app.catalog.models import Product, Category

catalog = Blueprint('catalog', __name__)

@catalog.route('/')
@catalog.route('/home')
def home():
    return "Welcome to the Catalog Home."

@catalog.route('/product/<id>')
def product(id):
    product = Product.query.get_or_404(id)
    return 'Product - %s, $%s' % (product.name, product.price)

@catalog.route('/products')
def products():
    products = Product.query.all()
    res = {}
    for product in products:
        res[product.id] = {
            'name': product.name,
            'price': str(product.price),
            'category': product.category
        }
    return jsonify(res)

@catalog.route('/product-create', methods=['POST',])
def create_product():
    name = request.form.get('name')
    price = request.form.get('price')
    category = request.form.get('category')
    # category = Category.query.filter_by(name=category).first()
    # if not category:
    #     category = Category(category)
    product = Product(name, price, category)
    db.session.add(product)
    db.session.commit()
    return 'Product created.'

@catalog.route('/category-create', methods=['POST',])
def create_category():
    name = request.form.get('name')
    category = Category(name)
    db.session.add(category)
    db.session.commit()
    return 'Category created.'

@catalog.route('/categories')
def categories():
    categories = Category.query.all()
    res = {}
    for category in categories:
        res[category.id] = {
            'name': category.name
        }
    # for product in category.products:
    #     res[category.id]['products'] = {
    #         'id': product.id,
    #         'name': product.name,
    #         'price': product.price
    #     }
    return jsonify(res)