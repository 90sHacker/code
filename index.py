import urllib.request, urllib.parse, urllib.error

baseParams = {'username': 'test', 'password': 'testing', 'to': '07055987643', 'content': 'Hello'}

urllib.request.urlopen('http://127.0.0.1:1401/send?%s' % urllib.parse.urlencode(baseParams)).read()