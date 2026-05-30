class Fancy(object):

    def __init__(self):
        self.add = 0
        self.multiply = 1
        self.values = list()
        self.MODULO = 10 ** 9 + 7

    def append(self, val):
        """
        :type val: int
        :rtype: None
        """
        val = (val - self.add) * pow(self.multiply, -1, self.MODULO) % self.MODULO
        self.values.append(val)

    def addAll(self, inc):
        """
        :type inc: int
        :rtype: None
        """
        self.add = (self.add + inc) % self.MODULO

    def multAll(self, m):
        """
        :type m: int
        :rtype: None
        """
        self.add = (self.add * m) % self.MODULO
        self.multiply = (self.multiply * m) % self.MODULO

    def getIndex(self, idx):
        """
        :type idx: int
        :rtype: int
        """
        if idx >= len(self.values):
            return -1
        else:
            return (self.values[idx] * self.multiply + self.add) % self.MODULO


# Your Fancy object will be instantiated and called as such:
# obj = Fancy()
# obj.append(val)
# obj.addAll(inc)
# obj.multAll(m)
# param_4 = obj.getIndex(idx)

f = Fancy()
f.append(2)
f.addAll(3)
f.append(7)
f.multAll(2)
print(f.getIndex(0))
f.addAll(3)
f.append(10)
f.multAll(2)
print(f.getIndex(0))
print(f.getIndex(1))
print(f.getIndex(2))
