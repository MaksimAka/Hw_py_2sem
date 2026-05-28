def retry(func):
    def wrapper(*args, **kwargs):
        while True:
            try:
                return func(*args, **kwargs)
            except ValueError:
                continue
            except OSError:
                print(f"{func.name} raise OSError exception.")
                raise
    return wrapper

@retry
def test_function(x):
#функция
    pass