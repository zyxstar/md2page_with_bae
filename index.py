#-*- coding:utf-8 -*-
import web


urls = ('/echo', 'echo')


class echo:
    def GET(self):
        return "render.poplang(RES_BASE_URL_PATH)"

app = web.application(urls, globals())

app.run()
