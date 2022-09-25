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


# single node
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

# Queue with LinkedList


class Queue(IQueuable):
    def __init__(self):
        self.head = self.tail = None

    def isEmpty(self):
        return self.head == None

    def enqueue(self, value):
        temp = Node(value)

        if self.tail == None:
            self.head = self.tail = temp
            return
        self.tail.next = temp
        self.tail = temp

    def dequeue(self):
        if self.isEmpty():
            return
        temp = self.tail
        curr = self.head
        while curr.next != None:
            curr = curr.next
        self.tail = curr
        return temp.data

    def getQueue(self):
        return self.head

    def size(self):
        count = 0
        temp = self.head
        while temp != None:
            count += 1
            temp = temp.next
        return count


# stack with linked list
class Stack(IQueuable):
    def __init__(self):
        self.head = self.tail = None

    def isEmpty(self):
        return self.head == None

    def enqueue(self, value):
        temp = Node(value)

        if self.tail == None:
            self.head = self.tail = temp
            return
        self.tail.next = temp
        self.tail = temp

    def dequeue(self):
        if self.isEmpty():
            return
        temp = self.head
        self.head = self.head.next
        return temp.data

    def getQueue(self):
        return self.head

    def size(self):
        count = 0
        temp = self.head
        while temp != None:
            count += 1
            temp = temp.next
        return count
