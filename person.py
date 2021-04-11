class Person:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    def full_name(self):
        return self.name + ' ' + self.surname

    def get_older(self, years):
        self.age = self.age + years


if __name__ == "__main__":
    x = Person("Name", "Surname", 20)
print(x.full_name())
x.get_older(12)
print(x.age)
