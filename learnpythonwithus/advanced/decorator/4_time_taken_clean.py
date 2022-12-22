import time

def timeit(func):
    def inner(*args, **kwargs):
        start_time = time.perf_counter()
        func(*args, **kwargs)
        end_time = time.perf_counter()
        print(end_time - start_time)
    return inner


@timeit
def slow_process(message):
    time.sleep(5)
    print('Hello World', message)
    return True

slow_process('python')
