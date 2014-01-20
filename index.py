#-*- coding:utf-8 -*-
import web

def app(environ, start_response):
    status = '200 OK'
    headers = [('Content-type', 'text/html')]
    start_response(status, headers)

    body=dir(web)

    return body

from bae.core.wsgi import WSGIApplication
application = WSGIApplication(app)
