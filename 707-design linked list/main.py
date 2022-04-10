class MyLinkedList(object):

    def __init__(self):
        from collections import deque
        self.nodes = []

    def get(self, index):
        """
        :type index: int
        :rtype: int
        """
        if index < len(self.nodes):
            return self.nodes[index]
        else:
            return -1

    def addAtHead(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.nodes = [val] + self.nodes

    def addAtTail(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.nodes.append(val)

    def addAtIndex(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        if index <= len(self.nodes):
            self.nodes = self.nodes[:index] + [val] + self.nodes[index:]

    def deleteAtIndex(self, index):
        """
        :type index: int
        :rtype: None
        """
        self.nodes = self.nodes[:index] + self.nodes[index+1:]


"""
myLinkedList = MyLinkedList()
myLinkedList.addAtHead(1)
myLinkedList.addAtTail(3)
myLinkedList.addAtIndex(1, 2)
print(myLinkedList.get(1))
myLinkedList.deleteAtIndex(1)
print(myLinkedList.get(1))
"""

"""
myLinkedList = MyLinkedList()
myLinkedList.addAtIndex(1, 0)
print(myLinkedList.get(1))
"""

myLinkedList = MyLinkedList()
myLinkedList.addAtHead(7)
myLinkedList.addAtHead(2)
myLinkedList.addAtHead(1)
myLinkedList.addAtIndex(3, 0)
myLinkedList.deleteAtIndex(2)
myLinkedList.addAtHead(6)
myLinkedList.addAtTail(4)
print(myLinkedList.get(4))
myLinkedList.addAtHead(4)
myLinkedList.addAtIndex(5, 0)
myLinkedList.addAtHead(6)
