from flask import Flask, request, render_template, jsonify, redirect
from forex import convert, currency_symbol
from flask_debugtoolbar import DebugToolbarExtension
app = Flask(__name__)
app.config['SECRET_KEY'] = 'not-so=secret-for-now'
debug = DebugToolbarExtension(app)

@app.route("/")
def home_page():
    """Home Page"""
    return render_template("index.html")
    
@app.route("/form", methods=["POST"])
def get_data():
    """get input from user and data from API"""
    ### get is better than alternated form of ex: request.form["cfrom"]
    from_curr = request.form.get('cfrom')
    to_curr = request.form.get('cto')
    amount = request.form.get('amount')
    
    #get converted amount (c_amount) from exchangerate.host API
    API = 'convert'
    KEY = '9fe18299682790786003cc50793e2111'
    cnvt_amount = convert(API,KEY,from_curr,to_curr, amount)
    cnvt_amount = round(cnvt_amount,2)
    cnvt_symbol = currency_symbol(to_curr)
    return render_template("converted.html",cnvt_amount=cnvt_amount,cnvt_symbol=cnvt_symbol)
    
    