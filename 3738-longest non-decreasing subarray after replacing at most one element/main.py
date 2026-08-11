class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # pre-process
        L = len(nums)

        # short-cut
        if L == 1:
            return 1

        # increasing array
        # increasing[x] - the length of increasing array ended with xth element
        increasing = list()
        increasing.append(1)
        idx = 1
        while idx < L:
            if nums[idx] >= nums[idx - 1]:
                increasing.append(increasing[idx - 1] + 1)
            else:
                increasing.append(1)
            idx += 1
        # print(increasing)

        # decreasing array
        # decreasing[x] - the length of decreasing array ended with xth element, from right to left
        decreasing = list()
        decreasing.append(1)
        idx = L - 1
        while idx > 0:
            if nums[idx] >= nums[idx - 1]:
                decreasing.append(decreasing[-1] + 1)
            else:
                decreasing.append(1)
            idx -= 1
        decreasing = decreasing[::-1]
        # print(decreasing)

        # process
        # enumerate nums[x]
        idx = 0
        ans = 1
        while idx < L:
            if idx == 0:
                ans = max(ans, decreasing[idx + 1] + 1)
            elif idx == L - 1:
                ans = max(ans, increasing[idx - 1] + 1)
            else:
                if nums[idx - 1] <= nums[idx + 1]:
                    ans = max(ans, increasing[idx - 1] + decreasing[idx + 1] + 1)
                else:
                    ans = max(ans, max(increasing[idx - 1] + 1, decreasing[idx + 1] + 1))
            idx += 1
        return ans


nums = [1,2,3,1,2]
nums = [2,2,2,2,2]
nums = [1,2,1,2,3,1,2]
nums = [1,2,3,1,-11,-10,-9,-8,-10,-11]
nums = [3,-4,-2]
nums = [7,1,-8]
nums = [4]
nums = [1,2]

"""
from random import randint
nums = [randint(1, 100) for _ in range(10 ** 5)]
print(nums)
"""

solution = Solution()
print(solution.longestSubarray(nums))
