# coding: utf-8
"""
Code using async/await keywords, located in its own module to keep
compatibility with python 3.4.
"""
import functools
import inspect


def make_native_coroutine(coroutine):
    """
    Wrap a coroutine (or any function returning an awaitable) in a native
    coroutine.
    """
    if inspect.iscoroutinefunction(coroutine):
        # Nothing to do.
        return coroutine

    @functools.wraps(coroutine)
    async def wrapper(*args, **kwargs):
        return await coroutine(*args, **kwargs)

    return wrapper
