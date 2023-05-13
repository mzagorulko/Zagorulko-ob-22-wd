class Cat:

    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    def info(self):
        print("кошка по имени {}, {} лет, цвет {}".format(self.name, self.age, self.color))


my_cat = Cat("Куся", 10, "дымчато-серый")
my_cat.info()
