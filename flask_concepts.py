import flask
from flask import request,jsonify

app = flask.Flask(__name__)

app.config['DEBUG']=True

book=[
    {'no':1,
     'title':"Python",
     'publication': 2022},
    {"no":2,
     'title':"Mysql",
     'publication':2022}
]
@app.route('/',methods=['GET'])
def home():
    return '<h1>Welcome to my api</h1>'

@app.route('/books/all', methods=['GET'])

def api_all():
    return jsonify(book)
app.run()