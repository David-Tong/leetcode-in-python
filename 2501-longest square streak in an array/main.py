from collections import defaultdict
from itertools import count


class Solution(object):
    def longestSquareStreak(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # pre-process
        # build squares table
        squares = set()
        num = 2
        square = num * num
        while square <= 10 ** 5:
            squares.add(square)
            num += 1
            square = num * num

        nums = set(nums)
        L = len(nums)
        nums = sorted(nums)
        from collections import defaultdict
        dicts = defaultdict(int)
        for idx, num in enumerate(nums):
            dicts[num] = idx

        # process
        # dp init
        # dp[x] - sorted nums longest square streak length ended with nums[x]
        from math import sqrt
        dp = [1] * L

        # dp transfer
        for x in range(L):
            num = nums[x]
            if num in squares:
                root = int(sqrt(num))
                if root in dicts:
                    dp[x] = dp[dicts[root]] + 1
        # print(dp)

        # post-process
        ans = max(dp)
        return ans if ans > 1 else -1


nums = [4,3,6,16,8,2]
nums = [2,3,5,6,7]
nums = [2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,200,210,256,1000,65536]
nums = [_ for _ in range(100000)]

print(nums)

solution = Solution()
print(solution.longestSquareStreak(nums))
