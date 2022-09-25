from abc import ABC, abstractmethod

# Abstract method


class IQueuable(ABC):

    @abstractmethod
    def enqueue(self, value):
        pass

    @abstractmethod
    def dequeue(self):
        pass

    @abstractmethod
    def getQueue(self):
        pass

    @abstractmethod
    def size(self):
        pass

# Queue with array


class Queue(IQueuable):
    def __init__(self):
        self.items = []

    def enqueue(self, value):
        self.items.append(value)
        return self.items

    def dequeue(self):
        item = self.items[0]
        self.items = self.items[1:]
        return item

    def getQueue(self):
        return self.items

    def size(self):
        return len(self.items)

# Stack with array


class Stack(IQueuable):
    def __init__(self):
        self.items = []

    def enqueue(self, value):
        self.items.append(value)
        return self.items

    def dequeue(self):
        return self.items.pop()

    def getQueue(self):
        return self.items

    def size(self):
        return len(self.items)
