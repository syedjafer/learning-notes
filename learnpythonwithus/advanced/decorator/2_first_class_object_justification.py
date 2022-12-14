def greet(name : str):
    print(f"Hi {name}")

# 1. Functions can be passed as arguments to other functions

def test(func):
    return func('Python') # -> greet('Pythin')

# test(greet)


# 2. Store Function to an variable

val = greet
# val('Jafer')

# 3. Return function from another function. (inner function)

def is_called():
    def is_returned():
        print("Hello")
    return is_returned

res = is_called()
print(res)
res()
