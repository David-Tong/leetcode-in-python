class MinStack(object):

    def __init__(self):
        self.stack = []
        self.min = None

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val)
        if self.min is None:
            self.min = val
        else:
            if self.min > val:
                self.min = val

    def pop(self):
        """
        :rtype: None
        """
        if len(self.stack) > 0:
            val = self.stack.pop(-1)

        if len(self.stack) == 0:
            self.min = None
        else:
            self.min = self.stack[0]
        for num in self.stack:
            if num < self.min:
                self.min = num


    def top(self):
        """
        :rtype: int
        """
        if len(self.stack) > 0:
            return self.stack[-1]
        else:
            return None

    def getMin(self):
        """
        :rtype: int
        """
        return self.min