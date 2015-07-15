#!/usr/bin/env python
# encoding: utf-8

import tornado.auth
import tornado.httpserver
import tornado.ioloop
import tornado.web

from tornado.options import options

import defines
from view.page import *


#定义Application信息，它是继承tornado.web.Application 的
class Application(tornado.web.Application):
    # __init__ 函数自动调用
    def __init__(self):
        #这里就是url对应的控制器，下面分别对应一个类，来处理里面的逻辑
        handlers = [
            (r"/", HomeHandler),
            (r"/project/list", ProjectListHandler),
            (r"/project/glance", ProjectGlanceHandler),
            (r"/article/list", ArticleListHandler),
            (r"/article/detail", ArticleDetailHandler),
            (r"/auth/login", AuthLoginHandler),
            (r"/auth/logout", AuthLogoutHandler),
        ]
        
        #然后调用tornado.web.Application类的__init__函数加载进来
        from settings import settings
        tornado.web.Application.__init__(self, handlers, **settings)

#入口函数
def main():
    tornado.options.parse_command_line()
    #创建一个服务器
    http_server = tornado.httpserver.HTTPServer(Application())
    #监听端口
    http_server.listen(options.port)
    #启动服务
    tornado.ioloop.IOLoop.instance().start()

#调用的入口
if __name__ == "__main__":
    main()




