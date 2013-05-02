'''
Created on Mar 14, 2013

@author: gdudhwal
'''

#!/usr/bin/env python
import web
from zk import ZooKepperConnection

urls = ('/(.*)', 'node')
render = web.template.render('templates/')

zkc = ZooKepperConnection("zk1:2181")

class node:
    def GET(self, url = ""):
        name = url if not url.endswith('/') else url[:-1]
        home = web.ctx.homedomain + ('/' + name if name != "" else '')
        raw_data = zkc.raw_data(name)
        data = raw_data[0]
        info = raw_data[1]
        children = zkc.children(name)
        return render.page(home, name, data, info, children)

app = web.application(urls, globals())
app.internalerror = web.debugerror
app.run()