class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def about_me(self):
        print("Меня зовут {} и мой возраст - {}".format(self.name, self.age))


person = Person("Михаил", 33)
person.about_me()
