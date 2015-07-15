#!/usr/bin/env python
# encoding: utf-8

from tornado.options import options
from pymongo import MongoClient
from bson.objectid import ObjectId

from json import JSONEncoder

from lib.singleton import singleton

class MyJSONEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, ObjectId):
            return unicode(obj)
        return JSONEncoder.default(self, obj)


@singleton
class MemDB:
    
    def __init__(self):
        self.database = None
        self._authed = False
        
        self._client = MongoClient(options.mongo_host)
        if self._client:
            self.database = self._client[options.mongo_database]
            self._authed = self.database.authenticate(options.mongo_user, options.mongo_password)
    
    def is_authed(self):
        return self._authed

    def get_object(self, name, object_id):
        return self.database[name].find_one({'_id': ObjectId(object_id)})
        
    def get_all(self, name):
        return self.database[name].find()
        
    def delete_object(self, object):
        pass

    def serialize(self, object, many=False):
        if many:
            array = []
            for obj in object:
                array.append(MyJSONEncoder().encode(obj).decode('utf-8'))
            return u",".join(array)
        else:
            return MyJSONEncoder().encode(object).decode('utf-8')
