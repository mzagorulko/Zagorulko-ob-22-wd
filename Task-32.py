class Schoolkid:
    def __init__(self, name, current_class):
        self.name = name
        self.current_class = current_class

    def study(self):
        print(f"Школьник по имени {self.name}, из {self.current_class} класса сейчас на занятии")


schoolkid = Schoolkid("Вася", "3a")
schoolkid.study()
