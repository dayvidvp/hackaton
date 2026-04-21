import time, functools

_store: dict[str, tuple[float, object]] = {}

def ttl_cache(seconds: int):
    def decorator(fn):
        @functools.wraps(fn)
        def wrapper(*args, **kwargs):
            key = (fn.__qualname__, args, tuple(sorted(kwargs.items())))
            entry = _store.get(key)
            if entry and time.monotonic() - entry[0] < seconds:
                return entry[1]
            result = fn(*args, **kwargs)
            _store[key] = (time.monotonic(), result)
            return result
        wrapper.cache_clear = lambda: _store.clear()
        return wrapper
    return decorator

def clear_all():
    _store.clear()
