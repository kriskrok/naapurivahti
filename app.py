from flask import Flask, url_for
from flask import redirect, render_template, request
from flask_sqlalchemy import SQLAlchemy
from markupsafe import escape

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///db'
db = SQLAlchemy(app)

@app.route("/")
def index():
    """Serve homepage template."""
    words = ['apina', 'banaani', 'cembalo']
    return render_template('index.html',
        message='Tervetuloa!',
        items = words) 

@app.route("/page1", methods=['GET'])
def page1():
    return "Tämä on sivu 1"

@app.route("/form")
def form():
    return render_template("form.html")

@app.route("/result", methods=["POST"])
def result():
    name = request.form['name']
    return render_template('result.html',
        name=request.form["name"])

@app.route("/page/<int:id>")
def page(id):
    return 'Tämä on sivu %d' % id
#   return "Tämä on sivu " +str(id)

# with resources for exception handling mate!
with app.test_request_context():
    print('index: {}'.format(url_for('index')))
    print('index: {}'.format(url_for('static', filename='style.css')))
    print('index: {}'.format(url_for('assets', filename='main.css')))


# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True)