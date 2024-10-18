class MyCircularDeque(object):

    def __init__(self, k):
        """
        :type k: int
        """
        self.size = k
        self.items = list()

    def insertFront(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if self.isFull():
            return False
        else:
            self.items.insert(0, value)
            return True

    def insertLast(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if self.isFull():
            return False
        else:
            self.items.append(value)
            return True

    def deleteFront(self):
        """
        :rtype: bool
        """
        if self.isEmpty():
            return False
        else:
            self.items.pop(0)
            return True

    def deleteLast(self):
        """
        :rtype: bool
        """
        if self.isEmpty():
            return False
        else:
            del self.items[-1]
            return True

    def getFront(self):
        """
        :rtype: int
        """
        if self.isEmpty():
            return -1
        else:
            return self.items[0]

    def getRear(self):
        """
        :rtype: int
        """
        if self.isEmpty():
            return -1
        else:
            return self.items[-1]

    def isEmpty(self):
        """
        :rtype: bool
        """
        return len(self.items) == 0

    def isFull(self):
        """
        :rtype: bool
        """
        return len(self.items) == self.size


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()

"""
mcd = MyCircularDeque(3)
print(mcd.insertLast(1))
print(mcd.insertLast(2))
print(mcd.insertFront(3))
print(mcd.insertFront(4))
print(mcd.getRear())
print(mcd.isFull())
print(mcd.deleteLast())
print(mcd.insertFront(4))
print(mcd.getFront())
"""

mcd = MyCircularDeque(4)
print(mcd.insertFront(9))
print(mcd.deleteLast())
print(mcd.getRear())
print(mcd.getFront())
print(mcd.getFront())
print(mcd.deleteFront())
print(mcd.insertFront(6))
print(mcd.insertLast(5))
print(mcd.insertFront(9))
print(mcd.getFront())
print(mcd.insertFront(6))
