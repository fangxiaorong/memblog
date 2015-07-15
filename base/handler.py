#!/usr/bin/env python
# encoding: utf-8

import tornado.web

from lib.database import MemDB

# 基类，继承自tornado.web.RequestHandler 的，后面的类都是继承这个类的
class BaseHandler(tornado.web.RequestHandler):
    # 属性装饰器，使db函数变成一个属性，便于后面直接使用
    @property
    def db(self):
        return MemDB()
        
    def serialize(self, data, many=False):
        return self.db.serialize(data, many=many)

    # 获得当前的用户
    def get_current_user(self):
        user_id = self.get_secure_cookie("blogdemo_user")
        if not user_id:
            return None
        return None

    def custom_error(self, info, **kwargs):
        if not self._finished:
            error = dict()
            error['code'] = 1000
            error['message'] = info
            self.write(self.serialize(error))
        raise tornado.web.Finish()

    def write_jsonp(self, data):
        callback_name = self.get_query_argument('callback')
        self.write(u'%s(%s)' % (callback_name, data))
