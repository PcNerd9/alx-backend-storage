#!/usr/bin/env python3

"""
contains a python function that changes all topics
of a school document based on the name
"""

import pymongo


def update_topics(mongo_collection, name, topics):
    """
    update all the topics of a school document
    parameters:
        mongo_collection: mongodb collection
        topics: the new topic to update it with
    """
    update_values = {"$set": {"topics": topics}}
    mongo_collection.update_many({"name": name},
                                 update_values)
