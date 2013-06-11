# -*- coding: utf-8 -*-
from bottle import run, request, response, route, abort

@route('api/resize/', method='POST')
@route('api/resize', method='POST')
def resize():
    return {
        'status': 'success',
        'data': ''
    }
