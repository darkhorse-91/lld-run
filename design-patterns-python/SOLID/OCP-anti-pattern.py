# Open Closed Principle
# Suggests that when you add a new functionality you add it via extension not as modification.
# OCP - open for extension, closed for modification

from enum import Enum

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

class Size(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3 

class Product:
    def __init__(self, name, color, size):
        self.name = name
        self.color = color
        self.size = size


class ProductFilter:
    def filter_by_color(self, products, color):
        for product in products:
            if product.color == color: yield product

    def filter_by_size(self, products, size):
        for product in products:
            if product.size == size: yield product

    def filter_by_size_And_color(self, products, color, size):
        for product in products:
            if product.size == size and product.color == color:
                yield product

# In case of 2 filters we have 3 kinds of methods for filtering.
# What in case we have 3 filters - & kinds of methods.
# This design doesn't holds good as we increase filter and everytime we 
# introduce new filter we have to modify the class which is violation of
# OC Principle

# For solving this problem - we are going to introduce a new Enterprise 
# pattern called the SPECIFICATION pattern.
# Implemented in OCP.py


if __name__ == "__main__":

    apple = Product('Apple', Color.RED, Size.SMALL)
    tree = Product('Tree', Color.GREEN, Size.LARGE)
    house = Product('House', Color.BLUE, Size.LARGE)

    pf = ProductFilter()

    products = [apple, tree, house]

    # filter green items
    for prod in pf.filter_by_color(products,Color.GREEN):
        print(f'{prod.name} is green')
