#-*- coding:utf-8 -*-
import web
import os.path
from lib import handlers

app_root = os.path.dirname(__file__)

handlers.RES_BASE_URL_PATH = "/static"
handlers.SAMPLE_NOTE_URL = "https://raw2.github.com/zyxstar/md_note/master/docs/Manual.md"
handlers.render = web.template.render(os.path.join(app_root, '/static/templates'))

app = web.application(handlers.urls, handlers.all_handlers).wsgifunc()

from bae.core.wsgi import WSGIApplication
application = WSGIApplication(app)
