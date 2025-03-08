from flask import Flask,render_template,request,redirect,url_for,session
from flask_mysqldb import MySQL
import random

app=Flask(__name__)
app.secret_key="123"

app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']='Tanusri@123'
app.config['MYSQL_DB']='ecommerce'

mysql=MySQL(app)

@app.route("/")
def home():
    cur=mysql.connection.cursor()
    cur.execute("select * from products")
    products=list(cur.fetchall())
    cur.close()
    
    random.shuffle(products)
    
    return render_template("home.html", products=products)

@app.route('/product/<int:product_id>')
def product(product_id):
    cur=mysql.connection.cursor()
    cur.execute("select * from products where id= %s ",(product_id,))
    product=cur.fetchone()
    cur.close()
    
    return render_template('product.html',product=product)


@app.route("/add_to_cart/<int:product_id>")
def add_to_cart(product_id):
    if 'cart' not in session:
        session['cart']=[]
    if product_id not in session['cart']:
        session['cart'].append(product_id)
        session.modified=True
    return redirect(url_for('cart'))
    
@app.route('/remove_from_cart/<int:product_id>')
def remove_from_cart(product_id):
    if 'cart' in session and product_id in session['cart']:
        session['cart'].remove(product_id)
        session.modified = True
    return redirect(url_for('cart'))
   
@app.route('/cart')
def cart():
    cart_items = []
    if 'cart' in session:
        cur = mysql.connection.cursor()
        for product_id in session['cart']:
            cur.execute("SELECT * FROM products WHERE id = %s", (product_id,))
            cart_items.append(cur.fetchone())
        cur.close()
    return render_template('cart.html', cart_items=cart_items)


if __name__=="__main__":
    app.run(debug=True)