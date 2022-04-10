class Solution(object):
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from collections import defaultdict
        dicts = defaultdict(int)
        for num in nums:
            dicts[num] += 1
        keys = sorted(dicts.keys())

        dp = [0] * len(keys)
        dp[0] = keys[0] * dicts[keys[0]]
        for x in range(1, len(keys)):
            for y in range(0, x):
                if keys[y] + 1 != keys[x]:
                    dp[x] = max(dp[x], dp[y] + keys[x] * dicts[keys[x]])
                else:
                    dp[x] = max(dp[x], keys[x] * dicts[keys[x]])
        return max(dp)


nums = [3, 4, 2]
nums = [2, 2, 3, 3, 3, 4]
nums = [2]
nums = [1, 2, 2, 1, 3, 3, 1, 4, 5, 5, 4, 3, 4, 4]

solution = Solution()
print(solution.deleteAndEarn(nums))
