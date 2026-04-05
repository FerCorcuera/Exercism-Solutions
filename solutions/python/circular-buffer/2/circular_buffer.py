class BufferFullException(BufferError):
    """Exception raised when CircularBuffer is full.

    message: explanation of the error.

    """
    def __init__(self, message):
        pass


class BufferEmptyException(BufferError):
    """Exception raised when CircularBuffer is empty.

    message: explanation of the error.

    """
    def __init__(self, message):
        pass


class CircularBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.buffer = []

    def read(self):

        
        if self.buffer == []:

            raise BufferEmptyException("Circular buffer is empty")

        else:
            
            a = self.buffer.pop()

            return a

    def write(self, data):
        

        if len(self.buffer) == self.capacity:

            raise BufferFullException("Circular buffer is full")
        
        self.buffer.insert(0,data)

    def overwrite(self, data):

        if len(self.buffer) == self.capacity:

            self.buffer.pop(-1)
            self.buffer.insert(0,data)
        
        else: 
            self.buffer.insert(0,data)

    def clear(self):

        self.buffer = []
