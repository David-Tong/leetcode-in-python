class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        N = len(nums)
        self.prefixes = [0] * (N + 1)
        for x in range(1, N + 1):
            self.prefixes[x] = self.prefixes[x-1] + nums[x-1]

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        return self.prefixes[right + 1] - self.prefixes[left]


nums = [-2, 0, 3, -5, 2, -1]
numArray = NumArray(nums)
print(numArray.sumRange(0, 2))
print(numArray.sumRange(2, 5))
print(numArray.sumRange(0, 5))
