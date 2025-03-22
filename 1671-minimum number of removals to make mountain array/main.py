class Solution(object):
    def minimumMountainRemovals(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def getMaxStrictIncreasingSubsequence(nums):
            # dp init
            dp = list()

            # dp transfer
            from bisect import bisect_left
            ans = list()
            for num in nums:
                idx = bisect_left(dp, num)
                if idx == len(dp):
                    dp.append(num)
                else:
                    dp[idx] = num
                ans.append((len(dp), dp[-1]))
            return ans

        # pre-process
        L = len(nums)
        lefts = getMaxStrictIncreasingSubsequence(nums)
        rights = getMaxStrictIncreasingSubsequence(nums[::-1])
        rights = rights[::-1]

        print(L)
        print(lefts)
        print(rights)

        # process
        maxi = 0
        for x in range(L - 1):
            if lefts[x][0] == 1:
                if lefts[x][1] >= rights[x + 1][1]:
                    continue
            if rights[x + 1][0] == 1:
                if lefts[x][1] <= rights[x + 1][1]:
                    continue
            if lefts[x][1] == rights[x + 1][1]:
                maxi = max(maxi, lefts[x][0] + rights[x + 1][0] - 1)
            else:
                maxi = max(maxi, lefts[x][0] + rights[x + 1][0])
        ans = L - maxi
        return ans


nums = [1,3,1]
nums = [2,1,1,5,6,2,3,1]
nums = [3,9,11,7,22,5,4,3,2,1]
nums = [1,2,3,4,4,3,2,1]
nums = [2,22,94,51,74,56,59,58,58,30,32,29,70,1,7]
nums = [9,8,1,7,6,5,4,3,2,1]
nums = [4,5,13,17,1,7,6,11,2,8,10,15,3,9,12,14,16]
nums = [1,2,1,3,4,4]

solution = Solution()
print(solution.minimumMountainRemovals(nums))
