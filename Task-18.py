class Figure:

    def __init__(self, square, perimeter):
        self.square = square
        self.perimeter = perimeter

    def info(self):
        print("площадь - {}, периметр - {}".format(self.square, self.perimeter))


figure = Figure(25, 20)
figure.info()
