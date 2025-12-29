from abc import ABC, abstractmethod

class Subject(ABC):
    @abstractmethod
    def query(self, request): pass

class RealSubject(Subject):
    def query(self, request):
        print('This request: '+request)

class ProxySubject(Subject):
    def __init__(self, access):
        self._access = access
        self._realsubject=RealSubject()
    def query(self, request):
        if self._access:
            self._realsubject.query(request)
        else:
            print("You cannot do it")
