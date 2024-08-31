#!/usr/bin/env python3

"""
contains a Cache class
"""
import functools
import redis
from typing import Callable, Union, Optional
from uuid import uuid4


def call_history(method: Callable) -> Callable:
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        input_key = method.__qualname__ + ":inputs"
        output_key = method.__qualname__ + ":outputs"

        self._redis.rpush(input_key, str(args))

        output = method(self, *args, **kwargs)
        self._redis.rpush(output_key, str(output))

        return output

    return wrapper


def count_calls(method: Callable) -> Callable:
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        key = method.__qualname__

        self._redis.incr(key)

        return method(self, *args, **kwargs)
    return wrapper


class Cache:
    def __init__(self):
        """
        create an instance of redis and store it in
        a private variable
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[int, str, float, bytes]) -> str:
        """
        store a data in the redis database using a random key
        """
        key = str(uuid4())
        self._redis.set(key, data)
        return key

    @call_history
    @count_calls
    def get(self, key: str,
            fn: Optional[Callable] = None) -> Union[int,
                                                    str, float,
                                                    bytes]:
        """
        get a data from redis and convert to the data type of
        desires
        """
        result = self._redis.get(key)
        if fn is None:
            return result
        if result is not None:
            return fn(result)
        else:
            return None

    @call_history
    @count_calls
    def get_str(self, key: str) -> str:
        """
        get the string representation of data stored in redis
        """
        return self.get(key, str)

    @call_history
    @count_calls
    def get_int(self, key: str) -> int:
        """
        get the integer representation of data stored in redis
        """
        return self.get(key, int)


def replay(fn: Callable) -> None:
    """
    display the history of calls of a particular function
    """

    function_name = fn.__qualname__
    cache = redis.Redis()
    no_of_times = int(cache.get(function_name))

    inputs = cache.lrange(function_name + ":inputs", 0, -1)
    outputs = cache.lrange(function_name + ":outputs", 0, -1)
    combine = list(zip(inputs, outputs))

    print("{} was called {} times:".format(function_name,
                                           no_of_times))
    for com in combine:
        print("{}(*{}) -> {}".format(function_name,
                                     com[0].decode("utf-8"),
                                     com[1].decode("utf-8")))
