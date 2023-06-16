class ProductCard:
    def __init__(self, name, price, count):
        self.name = name
        self.price = price
        self.count = count

    def count_decrease(self, count_change):
        if count_change:
            if self.count >= count_change:
                self.count -= count_change
            else:
                print('Ошибка изменения остатков')
                exit()
        else:
            print('Ошибка изменения остатков')
            exit()

    def price_change(self, price_change):
        if price_change:
            self.price -= price_change
        else:
            print('Ошибка изменения цены')
            exit()


product = ProductCard('Lay`s', 99.99, 100)
product.count_decrease(99)
product.price_change(120.00)
