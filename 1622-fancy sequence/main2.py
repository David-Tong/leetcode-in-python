class Fancy(object):

    def __init__(self):
        self.nums = list()
        self.operators = list()
        self.operator_idxes = list()
        self.MODULO = 10 ** 9 + 7
        from collections import defaultdict
        self.cache = defaultdict(tuple)

    def append(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.nums.append(val)
        self.operator_idxes.append(len(self.operators))

    def addAll(self, inc):
        """
        :type inc: int
        :rtype: None
        """
        self.operators.append(("+", inc))

    def multAll(self, m):
        """
        :type m: int
        :rtype: None
        """
        self.operators.append(("*", m))

    def getIndex(self, idx):
        """
        :type idx: int
        :rtype: int
        """
        if idx >= len(self.nums):
            return -1
        else:
            return self.__calculate(idx)

    def __calculate(self, idx):
        if idx not in self.cache:
            operator_idx = self.operator_idxes[idx]
            res = self.nums[idx]
        else:
            operator_idx = self.cache[idx][0]
            res = self.cache[idx][1]

        while operator_idx < len(self.operators):
            if self.operators[operator_idx][0] == "+":
                res = (res + self.operators[operator_idx][1]) % self.MODULO
            elif self.operators[operator_idx][0] == "*":
                res = (res * self.operators[operator_idx][1]) % self.MODULO
            operator_idx += 1
        self.cache[idx] = (operator_idx, res)
        return res


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
