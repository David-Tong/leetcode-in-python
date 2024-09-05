class Solution(object):
    def tallestBillboard(self, rods):
        """
        :type rods: List[int]
        :rtype: int
        """
        # dp[x] - the max left when difference between left - right is x
        from collections import defaultdict
        curr_dp = defaultdict(int)
        curr_dp[0] = 0

        for idx, rod in enumerate(rods):
            if idx == 0:
                curr_dp[rod] = rod
                curr_dp[0 - rod] = 0
            else:
                diffs = old_dp.keys()
                for diff in diffs:
                    curr_dp[diff + rod] = max(curr_dp[diff + rod], old_dp[diff] + rod)
                    curr_dp[diff - rod] = max(curr_dp[diff - rod], old_dp[diff])
            old_dp = curr_dp.copy()

        return old_dp[0]


rods = [1,2,3,6]
rods = [1,2,3,4,5,6]
rods = [1,2]
rods = [12,34,5,6,7,8,9,11,23,12,31,12,11,56,7,8,9]
rods = [4,5,6,8,9,1,11,23,87,1,2,3,4,5,6,1,12,44,55,6]

solution = Solution()
print(solution.tallestBillboard(rods))