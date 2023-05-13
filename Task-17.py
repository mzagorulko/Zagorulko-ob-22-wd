class Book:

    def __init__(self, title, author, year, genre):
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre

    def info(self):
        print("{}, {} ({}), {}".format(self.title, self.author, self.year, self.genre))


my_favourite_book = Book("Темная башня", "Стивен Кинг", 2022, "фантастика")
my_favourite_book.info()
