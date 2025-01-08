from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
"""
SQLAlchemy:

pip install flask-sqlalchemy. Allows us to write database tables with python classes.
"""

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'  # This is a dictionary that will accept new key values. 
"""
We use the app object and add an extra configuration so the flask application can recognize its database. 

SQLALCHEMY_DATABASE_URI - We have to add this key so the flask application can understand where the database is located. 

URI - uniform resource identifier - A file that is identified as a database.

"""
# Databases allows us to store organized information within tables where each table describes some data that we want to store.
db = SQLAlchemy(app)  # Database
app.app_context().push()

class Item(db.Model):
    id = db.Column(db.Integer(), primary_key=True)  # MUST CREATE. Convention to flask models, which allows it to understand the unique objects that will be inside our items.
    name = db.Column(db.String(length=30), nullable=False, unique=True)
    price = db.Column(db.Integer(), nullable=False)
    barcode = db.Column(db.String(length=12), nullable=False, unique=True)
    description = db.Column(db.String(length=1024), nullable=False, unique=True)

    def __repr__(self):
        return f'Item {self.name}'

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')

# Create a new route to a market page.
@app.route('/market')
def market_page():
    # This is the data we want to display.
    items = Item.query.all()
    return render_template('market.html', items=items)  # We set the variable name to the dictonary.

"""
On the Termial:

python

from 'filename' import db
db.create_all()
from 'filename' import Item
item1 = Item(name='', price=n, barcode='m', description="")
db.session.add(item1)
db.session.commit()
Item.query.all()

for item in Item.query.all()
...     item.name
...     item.barcode
...     item.id
...     item.description
...     item.price
...

item.query.filter_by(price=500)

for item in item.query.filter_by(price=500):
...     item.name
...

db.drop_all() - deletes everything.

item1 = Item.query.filter_by(name='Iphone 10).first()
item1.owner = User.query.filter_by(username='jsc').first().id()

db.session.rollback()

i = Item.query.filter_by(name='Iphone 10').first()
i.owned_user
"""