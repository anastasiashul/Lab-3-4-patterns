from abc import ABC, abstractmethod

class Product(ABC):
    @abstractmethod
    def get_type(self):
        pass

class Food(Product):
    def get_type(self):
        return "Food"

class Drink(Product):
    def get_type(self):
        return "Drink"

class ProductFactory(ABC):
    @abstractmethod
    def create_product(self): pass
    
    def gettype(self):
        product : Product = self.create_product()
        return product.get_type()


class FoodFactory(ProductFactory):
    def create_product(self):
        return Food()
class DrinkFactory(ProductFactory):
    def create_product(self):
        return Drink()




