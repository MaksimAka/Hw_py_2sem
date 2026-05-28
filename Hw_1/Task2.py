def bread(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        return f"Bread\n{res}\nBread" if res else "Bread\nBread"
    return wrapper

def salad(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        return f"Salat\n{res}" if res else "Salat"
    return wrapper

def tomato(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        return f"Tomato\n{res}" if res else "Tomato"
    return wrapper

def meat(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        return f"Meat\n{res}" if res else "Meat"
    return wrapper

@bread
@salad
@tomato
@meat
def make_sandwich():
    return ""

print(make_sandwich())