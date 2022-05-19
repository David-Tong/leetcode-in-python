class Solution(object):
    def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        N = len(nums)

        # dp[][0] - length of sequence, dp[][1] - number of sequences
        dp = [[1] * 2 for _ in range(N)]

        for idx, num in enumerate(nums):
            if idx > 0:
                for idx2, num2 in enumerate(nums[:idx]):
                    if num2 < num:
                        if dp[idx2][0] + 1 > dp[idx][0]:
                            dp[idx][0] = dp[idx2][0] + 1
                            dp[idx][1] = dp[idx2][1]
                        elif dp[idx2][0] + 1 == dp[idx][0]:
                            dp[idx][1] += dp[idx2][1]

        max_seq = 0
        ans = 0
        for seq in dp:
            if max_seq < seq[0]:
                max_seq = seq[0]
                ans = seq[1]
            elif max_seq == seq[0]:
                ans += seq[1]
        return ans


nums = [1,3,5,4,7]
nums = [2,2,2,2,2]
nums = [1]
nums = [1,3,2,5,4,8,7]
nums = [1,2,3,5,4,8,7]
nums = [1,2,4,3,5,4,7,2]


solution = Solution()
print(solution.findNumberOfLIS(nums))
