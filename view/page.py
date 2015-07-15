#!/usr/bin/env python
# encoding: utf-8

from base.handler import BaseHandler

# 首页
class HomeHandler(BaseHandler):
    def get(self):
        self.render('index.html')

# 项目列表
class ProjectListHandler(BaseHandler):
    def get(self):
        self.write("xxxxx")
        
# 项目概要，目录
class ProjectGlanceHandler(BaseHandler):
    def get(self):
        self.write('ArchiveHandler')
        
# 文章列表
class ArticleListHandler(BaseHandler):
    def get(self):
        self.set_header("Content-Type", "text/json")
        articles = list(self.db.get_all('blog'))
        if articles:
            for article in articles:
                article['content'] = u"\n".join(article['content'].split('\n')[0:20])
        self.write(u'{"articles":[%s]}' % self.serialize(articles, many=True))

# 文章内容
class ArticleDetailHandler(BaseHandler):
    def get(self):
        article_id = self.get_query_argument('id', None)
        self.set_header("Content-Type", "text/json")
        if not article_id:
            self.custom_error("xxxxx")
        else:
            article = self.db.get_object('blog', article_id)
            self.write(self.serialize(article))

# 首页
class AuthLoginHandler(BaseHandler):
    def get(self):
        self.write('AuthLoginHandler')

# 首页
class AuthLogoutHandler(BaseHandler):
    def get(self):
        self.write('AuthLogoutHandler')
