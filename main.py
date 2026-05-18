def add(a, b=None):
    if isinstance(a, list):
        return sum(a)
    return a + b

print(add(3, 5))
