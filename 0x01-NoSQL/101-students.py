#!/usr/bin/env python3

"""
contain a function that returns all students
sorted by average score
"""

import pymongo


def top_students(mongo_collection):
    """
    return all students sorted by average
    parameters:
        mongo_collection: the collection of query
    """

    pipeline = [
            {"$unwind": "$topics"},
            {"$group": {
                "_id": {"student_id": "$_id", "name": "$name"},
                "averageScore": {"$avg": "$topics.score"}}
             },
            {
                "$project": {
                    "_id": "$_id.student_id",
                    "name": "$_id.name",
                    "averageScore": "$averageScore",
                    }
             },
            {"$sort": {"averageScore": -1}}
            ]
    top_student = mongo_collection.aggregate(pipeline)
    return list(top_student)
