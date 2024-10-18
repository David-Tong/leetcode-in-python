class CustomStack(object):

    def __init__(self, maxSize):
        """
        :type maxSize: int
        """
        self.size= maxSize
        self.items = list()

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if len(self.items) < self.size:
            self.items.append(x)

    def pop(self):
        """
        :rtype: int
        """
        if len(self.items) == 0:
            return -1
        else:
            return self.items.pop()

    def increment(self, k, val):
        """
        :type k: int
        :type val: int
        :rtype: None
        """
        for x in range(min(len(self.items), k)):
            self.items[x] += val


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)

cs = CustomStack(3)
cs.push(1)
cs.push(2)
print(cs.pop())
cs.push(2)
cs.push(3)
cs.push(4)
cs.increment(5, 100)
cs.increment(2, 100)
print(cs.pop())
print(cs.pop())
print(cs.pop())
print(cs.pop())
