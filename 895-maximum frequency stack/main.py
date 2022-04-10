class FreqStack(object):

    def __init__(self):
        from collections import defaultdict
        self.stacks = []
        self.frequency = defaultdict(int)

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.frequency[val] += 1
        if self.frequency[val] > len(self.stacks):
            stack = list()
            stack.append(val)
            self.stacks.append(stack)
        else:
            self.stacks[self.frequency[val] - 1].append(val)

    def pop(self):
        """
        :rtype: int
        """
        val = self.stacks[-1].pop()
        if len(self.stacks[-1]) == 0:
            self.stacks.pop()
        self.frequency[val] -= 1
        if self.frequency[val] == 0:
            del self.frequency[val]
        return val


obj = FreqStack()
obj.push(5)
obj.push(7)
obj.push(5)
obj.push(7)
obj.push(4)
obj.push(5)
print(obj.pop())
print(obj.pop())
print(obj.pop())
print(obj.pop())