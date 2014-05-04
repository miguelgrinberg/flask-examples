from flask import request, render_template
from . import hello
from .. import mongo

@hello.route('/', methods=['GET', 'POST'])
def index():
    name = None
    new = False
    if request.method == 'POST' and 'name' in request.form:
        name = request.form['name']
        if mongo.db.names.find_one({'name': name}) is None:
            # this is a new name, add it to the database
            mongo.db.names.insert({'name': name})
            new = True
    return render_template('hello/index.html', name=name, new=new)
