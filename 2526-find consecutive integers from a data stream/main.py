class DataStream(object):

    def __init__(self, value, k):
        """
        :type value: int
        :type k: int
        """
        self.value = value
        self.k = k
        from collections import defaultdict
        self.dicts = defaultdict(int)
        self.nums = list()

    def consec(self, num):
        """
        :type num: int
        :rtype: bool
        """
        self.nums.append(num)
        if len(self.nums) > self.k:
            out = self.nums[len(self.nums) - self.k - 1]
            self.dicts[out] -= 1
        self.dicts[num] += 1
        return self.dicts[self.value] == self.k

# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)

"""
ds = DataStream(4, 3)
print(ds.consec(4))
print(ds.consec(4))
print(ds.consec(4))
print(ds.consec(3))
"""

ds = DataStream(1, 2)
print(ds.consec(1))
print(ds.consec(2))
print(ds.consec(1))
print(ds.consec(1))
print(ds.consec(1))