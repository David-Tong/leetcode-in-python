class Solution(object):
    def maxSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # pre-process
        L = len(nums)

        from collections import defaultdict
        dicts = defaultdict(int)
        dicts[0] = 0
        presum = 0

        # process
        idx = 1
        ans = float("-inf")
        while idx <= L:
            mod = idx % k
            presum += nums[idx - 1]
            if idx >= k:
                if mod in dicts:
                    ans = max(ans, presum - dicts[mod])
            if mod in dicts:
                dicts[mod] = min(dicts[mod], presum)
            else:
                dicts[mod] = presum
            idx += 1
        return ans


nums = [1,2]
k = 1

nums = [1,2,3]
k = 2

"""
nums = [-1, -2, -3, -4, -5]
k = 4

nums = [-5,1,2,-3,4]
k = 2

from random import randint
nums = [randint(-10 ** 5, 10 ** 5) for _ in range(10 ** 4)]
k = 99
"""

print(nums)

solution = Solution()
print(solution.maxSubarraySum(nums, k))
