# -*- coding: utf-8 -*-
import bottle
from bottle import request, response, install

from app.api import pdfresize

app = bottle.app()

if __name__ == '__main__':
    bottle.run(app=app, host='localhost', port=8070, reloader=True, debug=True)
else:
    application = app
