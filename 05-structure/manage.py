#!/usr/bin/env python
import os
from app import create_app
from flask.ext.script import Manager

manager = Manager(create_app)

@manager.command
def test():
    from subprocess import call

    os.environ['FLASK_CONFIG'] = 'testing'
    call(['nosetests', '-v',
          '--with-coverage', '--cover-package=app', '--cover-branches',
          '--cover-erase', '--cover-html', '--cover-html-dir=cover'])

if __name__ == '__main__':
    manager.run()
