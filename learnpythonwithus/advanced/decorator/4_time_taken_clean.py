import time

def timeit(func):
    def inner():
        start_time = time.perf_counter()
        func()
        end_time = time.perf_counter()
        print(end_time - start_time)
    return inner

@timeit
def slow_process():
    time.sleep(3)
    print('Hello World')
    return True



slow_process()
