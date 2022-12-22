import time

def execute_times(num):
    def decorator_repeat(func):
        def logic(*args, **kwargs):
            for _ in range(num):
                func(*args, **kwargs)
        return logic
    return decorator_repeat

@execute_times(num=3)
def slow_process(message):
    print('Hello World', message)
    return True

@execute_times(num=2)
def ping_me():
    print('PING 1.1.1.1')

slow_process('python')
ping_me()


API -> req/res -> 10s
