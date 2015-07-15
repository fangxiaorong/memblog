#!/usr/bin/env python
# encoding: utf-8

import os.path

#设置，如博客标题，模板目录，静态文件目录，xsrf，是否调试
settings = dict(
    blog_title=u"MemBlog",
    template_path=os.path.join(os.path.dirname(__file__), "templates"),
    static_path=os.path.join(os.path.dirname(__file__), "static"),
    xsrf_cookies=True,
    cookie_secret="__TODO:_GENERATE_YOUR_OWN_RANDOM_VALUE_HERE__",
    login_url="/auth/login",
    debug=True,
)