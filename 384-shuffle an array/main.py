class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.N = len(nums)
        self.origins = nums[:]
        self.nums = nums

    def reset(self):
        """
        :rtype: List[int]
        """
        return self.origins

    def shuffle(self):
        """
        :rtype: List[int]
        """
        from random import randint
        for x in range(self.N - 1, -1, -1):
            idx = randint(0, x)
            tmp = self.nums[self.N - 1]
            self.nums[self.N - 1] = self.nums[idx]
            self.nums[idx] = tmp
        return self.nums


solution = Solution([1, 2, 3, 4, 5, 6])
print(solution.shuffle())
print(solution.reset())
print(solution.shuffle())