from abc import ABC, abstractmethod
class Order:
    def __init__(self):
        self.ingredients={}
        self.burger=None
        self.fries=None
        self.salad=None
        self.drink=None
    def setBurger(self, burger):
        self.burger=burger
        if burger is not None: self.ingredients["burger"]=burger
    def setFries(self, fries):
        self.fries=fries
        if fries is not None: self.ingredients["fries"]=fries
    def setSalad(self, salad):
        self.salad=salad
        if salad is not None: self.ingredients["salad"]=salad
    def setDrink(self, drink):
        self.drink=drink
        if drink is not None: self.ingredients["drink"]=drink
    def description(self):
        return self.ingredients

class OrderBuilder(ABC):
    @abstractmethod
    def buildBurger(self): pass
    @abstractmethod
    def buildFries(self): pass
    @abstractmethod
    def buildSalad(self): pass
    @abstractmethod
    def buildDrink(self): pass
    @abstractmethod
    def getOrder(self): pass

class SmallComboOrderBuilder(OrderBuilder):
    def __init__(self):
        self.order=Order()
    def buildBurger(self):
        self.order.setBurger("Hamburger")
    def buildFries(self):
        self.order.setFries("Small")
    def buildSalad(self):
        self.order.setSalad(None)
    def buildDrink(self):
        self.order.setDrink("Small cola")
    def getOrder(self):
        return self.order

class BigComboOrderBuilder(OrderBuilder):
    def __init__(self):
        self.order=Order()
    def buildBurger(self):
        self.order.setBurger("Double big special")
    def buildFries(self):
        self.order.setFries("Big")
    def buildSalad(self):
        self.order.setSalad("Cesar")
    def buildDrink(self):
        self.order.setDrink("Big cola")
    def getOrder(self):
        return self.order

class OrderDirector:
    def __init__(self, builder):
        self.builder=builder
    def constructOrder(self):
        self.builder.buildBurger()
        self.builder.buildFries()
        self.builder.buildSalad()
        self.builder.buildDrink()
    def change_builder(self, builder):
        self.builder=builder

    


