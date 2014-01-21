#-*- coding:utf-8 -*-
import os
import web
import urllib
import urllib2
import markdown
import re
from lib import utils

RES_BASE_URL_PATH = "//rawgithub.com/zyxstar/markdown2page/master/res"
SAMPLE_NOTE_URL = "https://raw2.github.com/zyxstar/markdown_note/master/docs/Manual.md"

urls = ('/', 'index',
        '/echo', 'echo',
        '/gen_md','gen_md',
        '/popup/lang', 'poplang',
        '/popup/web', 'popweb',
        '/(.*)/', 'redirect')

app_root = os.path.dirname(__file__)
templates_root = os.path.join(app_root, 'templates')
render = web.template.render(templates_root)


class index:
    def GET(self):
        _sample_note = urllib2.urlopen(SAMPLE_NOTE_URL).read()
        return render.index(_sample_note, RES_BASE_URL_PATH)

class poplang:
    def GET(self):
        return render.poplang(RES_BASE_URL_PATH)

class popweb:
    def GET(self):
        return render.popweb(RES_BASE_URL_PATH)


class redirect:
    def GET(self, path):
        web.seeother('/' + path)

class echo:
    def GET(self):
        return "echo"
    def POST(self):
        web.header('Content-Type','application/octet-stream')
        filename= web.input(filename="file.txt").filename
        web.header('Content-Disposition',' attachment; filename="%s"' % filename )
        return web.input(content="no data").content

class gen_md:
    def GET(self):
        _query = web.input(src='',title='',encoding='utf-8')
        _md_text = urllib2.urlopen(_query.src).read()
        _title = os.path.basename(_query.src).split('.')[0] if _query.title == '' else _query.title
        _title = urllib.unquote_plus(_title.encode('utf-8'))
        return self.render_md(_title,unicode(_md_text, _query.encoding),_query.src)

    def POST(self):
        _query = web.input(note='',title='',based_url='')
        return self.render_md(_query.title, _query.note, _query.based_url)


    def render_md(self, title, md_text, based_url):
        _md_html = markdown.markdown(md_text)
        return render.gen_md(title, utils.fix_res_link(_md_html, based_url), RES_BASE_URL_PATH)









app = web.application(urls, globals()).wsgifunc()

from bae.core.wsgi import WSGIApplication
application = WSGIApplication(app)