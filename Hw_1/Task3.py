def cache(func):
    storage = {}
    def wrapper(*args, **kwargs):
        if args in storage:
            return storage[args]
        res = func(*args, **kwargs)
        storage[args] = res
        return res
    return wrapper

@cache
def slow_add(a, b):
    print(f"Вычисление для {a} + {b}:")
    return a + b

print(slow_add(2, 3))
print(slow_add(2, 3))
print(slow_add(5, 4))