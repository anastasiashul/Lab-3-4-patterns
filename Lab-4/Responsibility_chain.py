from abc import ABC, abstractmethod
class Request():
    def __init__(self, mark):
        self._mark=mark
    def getMark(self): return self._mark
class StudyHandler(ABC):
    @abstractmethod
    def handleRequest(self, request : Request): pass
    @abstractmethod
    def setNextHandler(self, handler : 'StudyHandler'): pass

class GreatHandler(StudyHandler):
    _next_handler=None
    def setNextHandler(self, handler: StudyHandler):
        self._next_handler=handler
    def handleRequest(self, request:Request):
        if request.getMark()>=80:
            print("You have 5 for this subject")
        elif self._next_handler is not None: 
            self._next_handler.handleRequest(request)

class GoodHandler(StudyHandler):
    _next_handler=None
    def setNextHandler(self, handler: StudyHandler):
        self._next_handler=handler
    def handleRequest(self, request:Request):
        if request.getMark()>=60:
            print("You have 4 for this subject")
        elif self._next_handler is not None: 
            self._next_handler.handleRequest(request)

class GiftHandler(StudyHandler):
    _next_handler=None
    def setNextHandler(self, handler: StudyHandler):
        self._next_handler=handler
    def handleRequest(self, request:Request):
        if request.getMark()>0:
            print("You have 3 for this subject")
        elif self._next_handler is not None: 
            self._next_handler.handleRequest(request)
 

