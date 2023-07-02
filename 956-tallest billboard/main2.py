class Solution(object):
    def tallestBillboard(self, rods):
        """
        :type rods: List[int]
        :rtype: int
        """
        L = 5000 // 2 + 1

        # dp[left][right] - if exists the pair of left and right
        dp = [[False] * L for _ in range(L)]
        dp[0][0] = True

        ans = 0
        for rod in rods:
            for x in range(L-1, -1, -1):
                for y in range(L-1, -1, -1):
                    if dp[x][y]:
                        if x + rod < L:
                            dp[x + rod][y] = True
                        if y + rod < L:
                            dp[x][y + rod] = True
                        if x + rod == y:
                            ans = max(ans, y)
                        if x == y + rod:
                            ans = max(ans, x)
        return ans


rods = [1,2,3,6]
#rods = [1,2,3,4,5,6]
#rods = [1,2]
#rods = [12,34,5,6,7,8,9,11,23,12,31,12,11,56,7,8,9]
#rods = [4,5,6,8,9,1,11,23,87,1,2,3,4,5,6,1,12,44,55,6]

solution = Solution()
print(solution.tallestBillboard(rods))
