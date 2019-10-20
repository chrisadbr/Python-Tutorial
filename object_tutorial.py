"""first = 'christian'
last = 'brown'
full_name = f'{first.title()} [{last.title()}] is a coder'
print(full_name)"""
"""
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        print("Move")
    def draw(self):
        print("Draw")
"""


class Person:
    def __init__(self, name):
        self.name = name

    def display_name(self):
        print(f'Hello, {self.name}')


username = Person('Juma Ramadhani')
username.display_name()

bob = Person('Bob Smith')
bob.display_name()
