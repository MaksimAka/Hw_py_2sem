import os
import pickle

def cache_v2(filename, key_type='args'):
    if os.path.exists(filename) and os.path.getsize(filename) > 0:
        try:
            with open(filename, 'rb') as f:
                file_cache = pickle.load(f)
        except Exception:
            file_cache = {}
    else:
        file_cache = {}

    def decorator(func):
        storage = file_cache.copy()

        def wrapper(*args, **kwargs):
            if key_type == 'args':
                key = args
            elif key_type == 'kwargs':
                key = tuple(sorted(kwargs.items()))
            else:
                key = (args, tuple(sorted(kwargs.items())))

            if key in storage:
                return storage[key]

            res = func(*args, **kwargs)
            storage[key] = res

            latest_file_cache = {}
            if os.path.exists(filename) and os.path.getsize(filename) > 0:
                try:
                    with open(filename, 'rb') as f:
                        latest_file_cache = pickle.load(f)
                except Exception:
                    pass

            latest_file_cache.update(storage)
            storage.update(latest_file_cache)

            with open(filename, 'wb') as f:
                pickle.dump(storage, f)

            return res
        return wrapper
    return decorator


@cache_v2('my_cache.pkl')
def heavy_comp(x, y):
    print(f"Вычисление для {x} + {y}:")
    return x + y


print(heavy_comp(7, 3))
print(heavy_comp(2, 3))
print(heavy_comp(5, 4))

