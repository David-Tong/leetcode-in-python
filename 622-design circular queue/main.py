class MyCircularQueue(object):

    def __init__(self, k):
        """
        :type k: int
        """
        self.k = k
        self.queue = [0] * self.k
        self.head = 0
        self.tail = -1
        self.size = 0

    def enQueue(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if self.isFull():
            return False
        else:
            self.tail = (self.tail + 1) % self.k
            self.queue[self.tail] = value
            self.size += 1
            return True

    def deQueue(self):
        """
        :rtype: bool
        """
        if self.isEmpty():
            return False
        else:
            self.head = (self.head + 1) % self.k
            self.size -= 1
            return True

    def Front(self):
        """
        :rtype: int
        """
        if self.isEmpty():
            return -1
        else:
            return self.queue[self.head]

    def Rear(self):
        """
        :rtype: int
        """
        if self.isEmpty():
            return -1
        else:
            return self.queue[self.tail]

    def isEmpty(self):
        """
        :rtype: bool
        """
        return self.size == 0

    def isFull(self):
        """
        :rtype: bool
        """
        return self.size == self.k


mcq = MyCircularQueue(3)
print(mcq.enQueue(1))
print(mcq.enQueue(2))
print(mcq.enQueue(3))
print(mcq.enQueue(4))
print(mcq.Rear())
print(mcq.isFull())
print(mcq.deQueue())
print(mcq.enQueue(4))
print(mcq.Rear())
