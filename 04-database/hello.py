import os
from flask import Flask, render_template, request
from flask.ext.pymongo import PyMongo

app = Flask(__name__)
app.config['MONGO_URI'] = os.environ['MONGO_URI']
mongo = PyMongo(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    name = None
    new = False
    if request.method == 'POST' and 'name' in request.form:
        name = request.form['name']
        if mongo.db.names.find_one({'name': name}) is None:
            # this is a new name, add it to the database
            mongo.db.names.insert({'name': name})
            new = True
    return render_template('index.html', name=name, new=new)

if __name__ == '__main__':
    app.run(debug=True)

