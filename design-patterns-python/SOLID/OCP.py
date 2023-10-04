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

# SPECIFICATION

class Specification:
    # Class determines whether or not a particular item satisfies a particular criteria
    # Abstract class for extension
    def is_satisfied(self, item):
        pass

    def __and__(self, other):
        return AndSpecification(self, other)

class Filter:
    # Abstract class for extension
    def filter(self, item, spec):
        pass

class ColorSpecification:
    def __init__(self, color):
        self.color = color

    def is_satisfied(self, item):
        return item.color == self.color

class SizeSpecification:
    def __init__(self, size):
        self.size = size

    def is_satisfied(self, item):
        return item.size == self.size

# COMBINATOR
class AndSpecification(Specification):
    # Combines two or more specifications
    def __init__(self, *args):
        self.args = args

    def is_satisfied(self, item):
        return all(map(
            lambda spec: spec.is_satisfied(item), self.args))

class BetterFilter(Filter):
    def filter(self, items, spec):
        for item in items:
            if spec.is_satisfied(item):
                yield item




if __name__ == "__main__":

    apple = Product('Apple', Color.RED, Size.SMALL)
    tree = Product('Tree', Color.GREEN, Size.LARGE)
    house = Product('House', Color.BLUE, Size.LARGE)
    cherry = Product('Cherry', Color.RED, Size.SMALL)

    bf = BetterFilter()

    products = [apple, tree, house, cherry]
    # red products
    red = ColorSpecification(Color.RED)

    for prod in bf.filter(products, red):
        print(f'{prod.name} is Red')

    # large products
    large = SizeSpecification(Size.LARGE)

    for prod in bf.filter(products, large):
        print(f'{prod.name} is Large')

    # large blue items 
    large_blue = AndSpecification(large, ColorSpecification(Color.BLUE))
    for prod in bf.filter(products, large_blue):
        print(f'{prod.name} is Large and Blue')


# We can also achieve AndSpecification by overloading boolean &. (Line: 31)
# We can't overload 'and'


    # Overloaded And Specification
    # small_red = ColorSpecification(Color.RED) & SizeSpecification(Size.SMALL)
    # for prod in bf.filter(products, small_red):
    #     print(f'{prod.name} is Small and Red')