class Solution(object):
    def minMoves(self, nums, limit):
        """
        :type nums: List[int]
        :type limit: int
        :rtype: int
        """
        # pre-process
        L = len(nums)

        from collections import defaultdict
        # helper function
        # the number of moves needed to get the sum
        # min = a, max = b
        # [2, a] - 2
        # [a + 1, a + b - 1] - 1
        # a + b - 0
        # [a + b + 1, b + limit + 1] - 1
        # [b + limit + 1, 2 * limit] - 2
        def process(idx):
            res = defaultdict(int)
            a = min(nums[idx], nums[L - 1 - idx])
            b = max(nums[idx], nums[L - 1 - idx])
            res[2] += 2
            res[a + 1] -= 1
            res[a + b] -= 1
            res[a + b + 1] += 1
            res[b + limit + 1] += 1
            return res

        # process
        dicts = defaultdict(int)
        idx = 0
        while idx < L // 2:
            res = process(idx)
            for key in res:
                dicts[key] += res[key]
            # print(res)
            # print(dicts)
            idx += 1

        # process
        presum = 0
        ans = float('inf')
        for key in sorted(dicts.keys()):
            presum += dicts[key]
            ans = min(ans, presum)
        return ans


nums = [1,2,4,3]
limit = 4

nums = [1,2,2,1]
limit = 2

nums = [1,2,1,2]
limit = 2

from random import randint
nums = [randint(1, 10 ** 5) for _ in range(10 ** 5)]
limit = 10 ** 5
print(nums)

solution = Solution()
print(solution.minMoves(nums, limit))
