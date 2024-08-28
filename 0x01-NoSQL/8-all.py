#!/usr/bin/python3

import pymongo


def list_all(mongo_collection):
    result = mongo_collection.find()
    if not result:
        return []
    return list(result)
        
