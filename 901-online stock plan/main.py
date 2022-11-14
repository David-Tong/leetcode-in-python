class StockSpanner(object):

    def __init__(self):
        self.idx = 0
        self.stack = list()

    def next(self, price):
        """
        :type price: int
        :rtype: int
        """
        # stack - (idx, price)
        self.idx += 1
        while self.stack and self.stack[-1][1] <= price:
            self.stack.pop()
        if self.stack:
            ans = self.idx - self.stack[-1][0]
        else:
            ans = self.idx
        self.stack.append((self.idx, price))
        return ans


ss = StockSpanner()
print(ss.next(100))
print(ss.next(80))
print(ss.next(60))
print(ss.next(70))
print(ss.next(60))
print(ss.next(75))
print(ss.next(85))
print(ss.next(100))
print(ss.next(5))