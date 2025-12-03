from Singleton import User
from Factory_Method import *
from Abstract_factory import *
from builder import *


s1=User('Kate')
s2=User('Vova')
s1.change_name('Anna')
print(f"Checking Singleton:same object? {s2 is s1}, same name? {s1.get_name()==s2.get_name()}")
ffact=FoodFactory()
f1=ffact.create_product()


dfact=DrinkFactory()
d1=dfact.create_product()
print()
print("Checking Factory Method:")
print(f"Type: {type(f1)}, gettype: {ffact.gettype()}, get_type: {f1.get_type()}")
print(f"Type: {type(d1)}, gettype: {dfact.gettype()}, get_type: {d1.get_type()}")
print()


wcoll = Collection(WindowsFactory())
mcoll = Collection(MacFactory())
print("Checking Abstract Factory:")
print(f"For Windows: chess: {wcoll.play_chess()}, minesweeper: {wcoll.play_minesweeper()}")
print(f"For Mac: chess: {mcoll.play_chess()}, minesweeper: {mcoll.play_minesweeper()}")
print()


builder1=SmallComboOrderBuilder()
director=OrderDirector(builder1)
director.constructOrder()
order1=builder1.getOrder()

builder2=BigComboOrderBuilder()
director.change_builder(builder2)
director.constructOrder()
order2=builder2.getOrder()
print("Cheking builder:")
print(f"Small order: {order1.description()}; \nBig order: {order2.description()}")