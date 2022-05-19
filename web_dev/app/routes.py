"""Routes for flask"""
from flask import render_template, request
from app import app

@app.route("/")
@app.route("/index")
def index():
    """Index handler"""
    return render_template('index.html')

@app.route("/get")
def get_params():
    """Route that accepts parameters"""
    par1 = request.args.get('p1')
    par2 = request.args.get('p2')
    return f"Param 1 = {par1}<br>Param 2 = {par2}"

@app.errorhandler(404)
def page_not_found(e):
    """Page not found handler"""
    return render_template('404.html'), 404 

@app.errorhandler(500)
def internal_server_error(e):
    """Internal Server Error handler"""
    return render_template('500.html'), 500
