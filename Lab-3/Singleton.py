class User:
    _person=None
    def __new__(cls, name):
        if cls._person is None: cls._person=super().__new__(cls)
        return cls._person
    def __init__(self, name):
        self._name=name
    def get_name(self):
        return self._name
    def change_name(self, name):
        self._name=name











