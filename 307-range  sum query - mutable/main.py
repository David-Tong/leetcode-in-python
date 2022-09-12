class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.L = len(nums)
        self.nums = [0] * self.L
        self.bits = [0] * (self.L + 1)

        for index in range(self.L):
            self.update(index, nums[index])
        self.nums = nums

    def update(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        delta = val - self.nums[index]
        self.nums[index] = val
        index += 1
        while index <= self.L:
            self.bits[index] += delta
            index += self.__lowbit(index)

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        return self.__getSum(right + 1) - self.__getSum(left)

    def __lowbit(self, index):
        return index & -index

    def __getSum(self, index):
        ans = 0
        while index > 0:
            ans += self.bits[index]
            index -= self.__lowbit(index)
        return ans


"""
obj = NumArray([1, 3, 5])
print(obj.sumRange(0, 2))
obj.update(1, 2)
print(obj.sumRange(0, 2))
"""

obj = NumArray([7, 2, 7, 2, 0])
obj.update(4, 6)
obj.update(0, 2)
obj.update(0, 9)
print(obj.sumRange(4, 4))
obj.update(3, 8)
print(obj.sumRange(0, 4))
obj.update(4, 1)
print(obj.sumRange(0, 3))
print(obj.sumRange(0, 4))
obj.update(0, 4)