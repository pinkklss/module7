import os


class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'
        if not os.path.isfile(self.__file_name):
            with open(self.__file_name, 'w') as file:
                pass

    def get_products(self):
        with open(self.__file_name, 'r') as file:
            f_r = file.read()
            return f'{f_r}'

    def add(self, *products):
        for product in products:
            with open(self.__file_name, 'r') as file:
                f = file.read()
                pr = str(product)
                if pr in f:
                    print(f'Продукт {pr} уже есть в магазине')
                else:
                    with open(self.__file_name, 'a') as file:
                        file.write(f'{pr}\n')


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)  # str

s1.add(p1, p2, p3)

print(s1.get_products())

s1.add(p1, p2, p3)

print(s1.get_products())
