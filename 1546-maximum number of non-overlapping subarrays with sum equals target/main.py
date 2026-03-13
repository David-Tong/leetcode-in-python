class Solution(object):
    def maxNonOverlapping(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # process
        presum = 0
        keys = set()
        keys.add(0)
        ans = 0
        for num in nums:
            presum += num
            key = presum - target
            if key in keys:
                presum = 0
                keys = set()
                keys.add(0)
                ans += 1
            else:
                keys.add(presum)
        return ans


nums = [1,1,1,1,1]
target = 2

nums = [-1,3,5,1,4,2,-9]
target = 6

nums = [2,0,-2,2,2,0,1,-1,3,1,-1,2,2,0,2]
target = 2

from random import randint
nums = [randint(-10 ** 2, 10 ** 2) for _ in range(10 ** 5)]
target = 10
print(nums)

solution = Solution()
print(solution.maxNonOverlapping(nums, target))
