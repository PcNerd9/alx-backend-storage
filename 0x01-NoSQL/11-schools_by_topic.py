#!/usr/bin/env python3

"""
contains a function that return the list of school
having a specific topic
"""

import pymongo


def schools_by_topic(mongo_collection, topic):
    """
    return a list of school having a specific topic
    """
    result = mongo_collection.find({"topics": {"$in": [topic]}})
    return list(result)
