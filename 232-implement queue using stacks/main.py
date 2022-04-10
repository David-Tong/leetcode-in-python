class MyQueue(object):

    def __init__(self):
        self.stack = []
        self.stack2 = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack.append(x)

    def pop(self):
        """
        :rtype: int
        """
        if self.empty():
            return None

        while len(self.stack) > 0:
            self.stack2.append(self.stack.pop(-1))
        item = self.stack2.pop(-1)
        while len(self.stack2) > 0:
            self.stack.append(self.stack2.pop(-1))
        return item

    def peek(self):
        """
        :rtype: int
        """
        if self.empty():
            return None

        while len(self.stack) > 0:
            self.stack2.append(self.stack.pop(-1))
        item = self.stack2[-1]
        while len(self.stack2) > 0:
            self.stack.append(self.stack2.pop(-1))
        return item

    def empty(self):
        """
        :rtype: bool
        """
        if len(self.stack) == 0:
            return True
        else:
            return False


myQueue = MyQueue()
myQueue.push(1)
myQueue.push(2)
print(myQueue.peek())
print(myQueue.pop())
print(myQueue.pop())
print(myQueue.pop())
print(myQueue.peek())
print(myQueue.empty())
