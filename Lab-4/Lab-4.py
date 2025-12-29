from Strategy import *
from Responsibility_chain import *
from Iterator import *
from Proxy import *
from Adapter import *
from Bridge import *
print("Testing strategy")

game=Game()
print("Play without strategy: ", end='')
game.playGame()

game.setStrategy(EasyGameStrategy())
print("Play with easy strategy: ", end='')
game.playGame()

game.setStrategy(HardGameStrategy())
print("Play with hard strategy: ", end='')
game.playGame()

print()

print("Testing Responsibility chain")
handler5 = GreatHandler()
handler4=GoodHandler()
handler3=GiftHandler()
handler5.setNextHandler(handler4)
handler4.setNextHandler(handler3)
mark1=Request(81)
mark2=Request(79)
mark3=Request(50)
print(f'For mark {mark1.getMark()}: ')
handler5.handleRequest(mark1)
print(f'For mark {mark2.getMark()}: ')
handler5.handleRequest(mark2)
print(f'For mark {mark3.getMark()}: ')
handler5.handleRequest(mark3)
print()

print('Testing Iterator')
mas1=[1, 4, 7, 5]
it=FileIterator(mas1)
print(it.next())
print(it.next())
mas2=['File1', 'File2']
it2=FileIterator(mas2)
print(it2.next())
print(it2.next())

print()
print("Testing Proxy")
user1=ProxySubject(False)
user2=ProxySubject(True)
request='Simple request'
user1.query(request)
user2.query(request)

print()
print('Testing adapter:')
external=External()
job1=JobAdapter(external)
job1.job("job for External")

print()
print('Testing bridge')
monitor = Monitor()
printer=Printer()
textonmonitor =TextOutput(monitor)
textonprinter=TextOutput(printer)
textonmonitor.render("I am monitor")
textonprinter.render("I am printer")
image=ImageOutput(monitor)
image.render("100100100100")
