class Solution(object):
    def longestSubsequence(self, arr, difference):
        """
        :type arr: List[int]
        :type difference: int
        :rtype: int
        """
        # dp[x] - the longest subsequence length ended with x
        from collections import defaultdict
        dp = defaultdict(int)

        for item in arr:
            prev = item - difference
            if prev in dp:
                dp[item] = max(dp[item], dp[prev] + 1)
            else:
                dp[item] = 1
        return max(dp.values())


arr = [1,2,3,4]
difference = 1

arr = [1,3,5,7]
difference = 1

arr = [1,5,7,8,5,3,4,2,1]
difference = -2

arr = [1]
difference = 100

arr = [5,4,3,2,1]
difference = -1

solution = Solution()
print(solution.longestSubsequence(arr, difference))
