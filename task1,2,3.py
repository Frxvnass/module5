import time
#iterator
class even_numbers:
    def __init__(self):
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.current += 2
        if self.current > 1_000_000:
            raise StopIteration
        return self.current
my_iterator = even_numbers()
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))


#generator
def fibonacci(n):
    a, b = 0, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1

for num in fibonacci(8):
    print(num)

# Decorator
def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        ms = (time.time() - start) * 1000
        print(f"{ms:.2f}ms")
        return result
    return wrapper
@timer
def sleep():
    time.sleep(1)
    return "Done"

print(sleep())