def greet():
    print("hello world")

# print(dir(greet))

# l = [1, 2, 3,4]
# print(dir(l))

class Greet:
    def __init__(self):
        self.message = 'Hi Mate'

    def __call__(self):
        print(self.message)

g = Greet()
# print(dir(g))

greet()

g()
