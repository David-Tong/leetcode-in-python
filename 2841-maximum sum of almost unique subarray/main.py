class Solution(object):
    def maxSum(self, nums, m, k):
        """
        :type nums: List[int]
        :type m: int
        :type k: int
        :rtype: int
        """
        # pre-process
        L = len(nums)
        from collections import defaultdict
        dicts = defaultdict(int)

        # process
        idx = 0
        total = 0
        ans = 0
        while idx < k:
            dicts[nums[idx]] += 1
            total += nums[idx]
            idx += 1
        if len(dicts) >= m:
            ans = total

        while idx < L:
            dicts[nums[idx - k]] -= 1
            total -= nums[idx - k]
            if dicts[nums[idx - k]] == 0:
                del dicts[nums[idx - k]]
            dicts[nums[idx]] += 1
            total += nums[idx]
            if len(dicts) >= m:
                ans = max(ans, total)
            idx += 1
        return ans


nums = [2,6,7,3,1,7]
m = 3
k = 4

nums = [5,9,9,2,4,5,4]
m = 1
k = 3

nums = [1,2,1,2,1,2,1]
m = 3
k = 3

import random
nums = [random.randint(1,10 ** 9) for _ in range(2 * 10 ** 4)]
print(nums)
m = 100
k = 500

solution = Solution()
print(solution.maxSum(nums, m, k))
