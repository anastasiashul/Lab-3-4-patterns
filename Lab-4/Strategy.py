from abc import ABC, abstractmethod
class GameStrategy(ABC):
    @abstractmethod
    def play(self): pass

class EasyGameStrategy(GameStrategy):
    def play(self):
        print('Play with easy difficulty')

class HardGameStrategy(GameStrategy):
    def play(self):
        print('Play with hard difficulty')

class Game():
    _gamestateg : GameStrategy=None
    def setStrategy(self,strategy:GameStrategy):
        self._gamestateg=strategy

    def playGame(self):
        if self._gamestateg is None: print("No strategy")
        else:
            self._gamestateg.play()

    




