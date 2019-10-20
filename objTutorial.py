class Person:
    def __init__(self, first_name, last_name, id = 0):
        self.first_name = first_name
        self.last_name = last_name
        self.id = id
    
    def __str__(self):
        return "{} {}, ID:{}".format\
            (self.first_name, self.last_name, self.id)


my_obj = Person('John', 'Smith', 12345)
print(my_obj)