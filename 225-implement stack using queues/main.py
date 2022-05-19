class MyStack(object):

    def __init__(self):
        from collections import deque
        self.queue = deque()
        self.queue2= deque()

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if not self.queue2:
            self.queue2.append(x)
        else:
            while self.queue2:
                self.queue.append(self.queue2.popleft())
            self.queue2.append(x)
            while self.queue:
                self.queue2.append(self.queue.popleft())

    def pop(self):
        """
        :rtype: int
        """
        if self.queue2:
            return self.queue2.popleft()

    def top(self):
        """
        :rtype: int
        """
        if self.queue2:
            return self.queue2[0]

    def empty(self):
        """
        :rtype: bool
        """
        return not self.queue2


stack = MyStack()
stack.push(1)
stack.push(2)
print(stack.top())
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.empty())
