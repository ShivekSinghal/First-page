from flask import Flask, jsonify, request, render_template
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)



@app.route('/')
def landing_page():
    return render_template("index.html")

@app.route('/pinkd')
def pinkd_tickets():
    return render_template("pinkd.html")



if __name__ == '__main__':
    app.run(debug=True, port=4883)
