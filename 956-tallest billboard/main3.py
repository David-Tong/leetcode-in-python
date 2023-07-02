class Solution(object):
    def tallestBillboard(self, rods):
        """
        :type rods: List[int]
        :rtype: int
        """
        # dp[left][right] - if exists the pair of left and right
        from collections import defaultdict
        dp = defaultdict()
        dp[0] = defaultdict(bool)
        dp[0][0] = True

        ans = 0
        for rod in rods:
            lefts = sorted(dp.keys(), key=lambda x: -x)
            for left in lefts:
                rights = sorted(dp[left].keys(), key=lambda x: -x)
                for right in rights:
                    if dp[left][right]:
                        if (left + rod) not in dp:
                            dp[left + rod] = defaultdict(bool)
                        dp[left + rod][right] = True
                        dp[left][right + rod] = True

                        if left + rod == right:
                            ans = max(ans, right)
                        if left == right + rod:
                            ans = max(ans, left)
        return ans


rods = [1,2,3,6]
rods = [1,2,3,4,5,6]
#rods = [1,2]
#rods = [12,34,5,6,7,8,9,11,23,12,31,12,11,56,7,8,9]
#rods = [4,5,6,8,9,1,11,23,87,1,2,3,4,5,6,1,12,44,55,6]
rods = [61,53,44,44,45,51,45,48,46,57,54,55,49,51,47]

solution = Solution()
print(solution.tallestBillboard(rods))
