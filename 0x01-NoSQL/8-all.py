#!/usr/bin/env python3
"""
lists all documents in a collections
"""
import pymongo


def list_all(mongo_collection):
    """
    lists all documents in a collections
    """
    result = mongo_collection.find()
    if not result:
        return []
    return list(result)
