# -*- coding: UTF-8 -*-

import re
import urllib2

def fix_res_link(html, based_url):
    def replace_link(match_obj):
        _url = match_obj.group(2)
        _url_result = urllib2.urlparse.urlparse(_url)
        if _url_result.scheme == '' and _url_result.path != '':
            _url = urllib2.urlparse.urljoin(based_url, _url)

        return u"%s%s%s" % (match_obj.group(1), _url, match_obj.group(3))

    for _pattern in  [ur"""(<img.*?src=")(.*?)(".*?/>)""", ur"""(<a.*?href=")(.*?)(".*?>)"""]:
        html = re.sub(_pattern, replace_link, html)
    return html


def proxy_http_get(url, **headers):pass

def proxy_http_post(url, **headers):pass

