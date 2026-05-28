def bread(func):
    def wrapper(*args, **kwargs):
        print("Bread")
        res = func(*args, **kwargs)
        print("Bread")
        return res
    return wrapper

def salad(func):
    def wrapper(*args, **kwargs):
        print("Salat")
        return func(*args, **kwargs)
    return wrapper

def tomato(func):
    def wrapper(*args, **kwargs):
        print("Tomato")
        return func(*args, **kwargs)
    return wrapper

def meat(func):
    def wrapper(*args, **kwargs):
        print("Meat")
        return func(*args, **kwargs)
    return wrapper

@bread
@salad
@tomato
@meat
def make_sandwich():
    pass

make_sandwich()