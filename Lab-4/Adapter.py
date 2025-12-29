from abc import ABC, abstractmethod

class External():
    def start_job(self, mes):
        print('Starting job: '+mes)

class Job(ABC):
    @abstractmethod
    def job(self, mes):pass

class JobAdapter(Job):
    def __init__(self, external):
        self._external = external
    def job(self, mes):
        self._external.start_job(mes)
