from flask import Flask, render_template


app = Flask(__name__)



@app.route('/')
def landing_page():
    return render_template("index.html")

@app.route('/pinkd')
def pinkd_tickets():
    return render_template("pinkd.html")


if __name__ == '__main__':
    app.run(debug=True, port=4999)
