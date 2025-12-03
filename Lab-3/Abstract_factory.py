from abc import ABC, abstractmethod
class Chess(ABC):
    @abstractmethod
    def play(self): pass
class Minesweeper(ABC):
    @abstractmethod
    def play(self): pass

class WindowsChess(Chess):
    def play(self):
        return "Starting a WindowsChess..."
class WindowsMinesweeper(Minesweeper):
    def play(self):
        return "Starting a WindowsMinesweeper..."

class MacChess(Chess):
    def play(self):
        return "Starting a MacChess..."
class MacMinesweeper(Minesweeper):
    def play(self):
        return "Starting a MacMinesweeper..."

class GameFactory(ABC):
    @abstractmethod
    def create_chess(self): pass
    @abstractmethod
    def create_minesweeper(self): pass

class WindowsFactory(GameFactory):
    def create_chess(self):
        return WindowsChess()
    def create_minesweeper(self):
        return WindowsMinesweeper()

class MacFactory(GameFactory):
    def create_chess(self):
        return MacChess()
    def create_minesweeper(self):
        return MacMinesweeper()

class Collection:
    def __init__(self, factory):
        self._chess=factory.create_chess()
        self._minesweeper=factory.create_minesweeper()
    def play_chess(self):
        return self._chess.play()
    def play_minesweeper(self):
        return self._minesweeper.play()



