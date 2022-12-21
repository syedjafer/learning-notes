import time

def timeit(func):
    def inner():
        start_time = time.perf_counter()
        func()
        end_time = time.perf_counter()
        print(end_time - start_time)
    return inner

def execute_times(num):
    def decorator_repeat(func):
        def inner(*args, **kwargs):
            for _ in range(num):
                print(func.__name__)
                func(*args, **kwargs)
        return inner
    return decorator_repeat

@execute_times(num=2)
def slow_process():
    print('Hello World')
    return True



slow_process()
