#!/usr/bin/env python
# encoding: utf-8

from tornado.options import define


#定义一些通用的配置信息，比如数据库的连接信息，端口信息
define("port", default=9000, help="run on the given port", type=int)
define("mongo_host", default="45.78.24.75:27017", help="blog database host")
define("mongo_database", default="memblog", help="blog database name")
define("mongo_user", default="fscience", help="blog database user")
define("mongo_password", default="123456", help="blog database password")