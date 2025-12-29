from abc import ABC, abstractmethod

class Device(ABC):
    @abstractmethod
    def display(self,data): pass

class Monitor(Device):
    def display(self, data):
        print("Data on monitor: "+data)
class Printer(Device):
    def display(self, data):
        print("Data on printer: "+data)

class Output(ABC):
    def __init__(self, device:Device):
        self.device=device
    @abstractmethod
    def render(self,data): pass

class TextOutput(Output):
    def __init__(self, device:Device):
        super().__init__(device)
    def render(self,data):
        self.device.display("Text: "+data)
class ImageOutput(Output):
    def __init__(self, device:Device):
        super().__init__(device)
    def render(self,data):
        self.device.display("Image: "+data)

        
