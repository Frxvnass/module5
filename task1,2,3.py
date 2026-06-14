
class Even_numbers:
    def __init__(self, num):
        self.num = num
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.count += 2
        if self.count <= self.num:
            return self.count
        else:
            raise StopIteration
my_iterator = Even_numbers(1_000)
for i in my_iterator:



    import time
    def spendtime(func):
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            print(f"Work is finished in  {end_time - start_time} seconds")
            return result

        return wrapper
    @spendtime
    def work():
        time.sleep(1)
        return 'done'
    print(work())





