#!/usr/bin/env python3

"""
contains a Cache class
"""

import redis
from uuid import uuid4


class Cache:
    def __init__(self):
        """
        create an instance of redis and store it in
        a private variable
        """
        self._redis = redis.Redis()
        self._redis.flushdb

    def store(self, data: str | bytes | int | float) -> str:
        """
        store a data in the redis database using a random key
        """
        key = str(uuid4())
        self._redis.set(key, data)
        return key
