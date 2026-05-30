class StockPrice(object):

    def __init__(self):
        from collections import defaultdict
        self.dicts = defaultdict(int)
        from sortedcontainers import SortedList
        self.prices = SortedList()
        self.timestamp = 0
        self.price = 0

    def update(self, timestamp, price):
        """
        :type timestamp: int
        :type price: int
        :rtype: None
        """
        if timestamp in self.dicts:
            self.prices.discard(self.dicts[timestamp])
        self.dicts[timestamp] = price
        self.prices.add(price)
        if timestamp >= self.timestamp:
            self.timestamp = timestamp
            self.price = price

    def current(self):
        """
        :rtype: int
        """
        return self.price

    def maximum(self):
        """
        :rtype: int
        """
        return self.prices[-1]

    def minimum(self):
        """
        :rtype: int
        """
        return self.prices[0]


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()

sp = StockPrice()
sp.update(1, 10)
sp.update(2, 5)
print(sp.current())
print(sp.maximum())
sp.update(1, 3)
print(sp.maximum())
sp.update(4, 2)
print(sp.minimum())
sp.update(4, 12)
print(sp.current())
