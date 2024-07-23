class Solution(object):
    def waysToMakeFair(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # pre-process
        L = len(nums)
        evens_presum = [0]
        odds_presum = [0]
        for x in range(L):
            if x % 2 == 0:
                evens_presum.append(nums[x] + evens_presum[-1])
            else:
                odds_presum.append(nums[x] + odds_presum[-1])

        # process
        ans = 0
        for x in range(L):
            if x % 2 == 0:
                idx = x // 2
                evens = evens_presum[idx] + odds_presum[-1] - odds_presum[idx]
                odds = odds_presum[idx] + evens_presum[-1] - evens_presum[idx + 1]
            else:
                idx = x // 2 + 1
                evens = evens_presum[idx] + odds_presum[-1] - odds_presum[idx]
                odds = odds_presum[idx - 1] + evens_presum[-1] - evens_presum[idx]
            if evens == odds:
                ans += 1
        return ans


nums = [2,1,6,4]
nums = [1,1,1]
nums = [1,2,3]
nums = [1,2,1,2,1,2,1,1,1]

solution = Solution()
print(solution.waysToMakeFair(nums))
