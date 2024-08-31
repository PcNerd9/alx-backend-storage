#!/usr/bin/env python3

"""
request a page from the internet and cache
"""
import functools
import requests
from redis import Redis
from typing import Callable


def cache(func: Callable) -> Callable:
    """
    a wrapper function
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        """
        store the number of times a url is requested
        """
        redis = Redis()
        key_name = f"count: {args[0]}"
        redis.incr(key_name)
        result = func(*args, **kwargs)
        redis.setex(args[0], 10, result)
        return result

    return wrapper


@cache
def get_page(url: str) -> str:
    """
    request a page from a url and return the
    test
    """

    request = requests.get(url)
    return request.content
