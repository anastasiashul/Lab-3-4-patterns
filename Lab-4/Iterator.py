class FileIterator():
    def __init__(self, files):
        self._files=files
        self._position=0
    def hasNext(self):
        return self._position<len(self._files)
    def next(self):
        if self.hasNext():
            Object=self._files[self._position]
            self._position+=1
            return Object
        raise StopIteration()


    
