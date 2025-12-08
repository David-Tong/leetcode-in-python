class Solution(object):
    def maxFrequency(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # pre-process
        from collections import defaultdict
        counts = 0
        for num in nums:
            if num == k:
                counts += 1

        # process
        ans = counts
        presums = defaultdict(int)
        for num in nums:
            if num == k:
                for key in presums:
                    presums[key] = max(0, presums[key] - 1)
            else:
                presums[num] += 1
            ans = max(ans, counts + presums[num])
        return ans


nums = [1,2,3,4,5,6]
k = 1

nums = [10,2,3,4,5,5,4,3,2,2]
k = 10

from random import randint
nums = [randint(1, 50) for _ in range(10 ** 5)]
k = 30
print(nums)

solution = Solution()
print(solution.maxFrequency(nums, k))
