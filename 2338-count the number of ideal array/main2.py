from numpy.ma import maximum_fill_value


class Solution(object):
    def idealArrays(self, n, maxValue):
        """
        :type n: int
        :type maxValue: int
        :rtype: int
        """
        # process
        # dp init
        # dp[x] - the number of ideal array ended with number x
        prev = [1] * (maxValue + 1)
        for x in range(1, n):
            dp = [0] * (maxValue + 1)
            for y in range(1, maxValue + 1):
                for z in range(1, y + 1):
                    if y % z == 0:
                        dp[y] += prev[z]
            prev = dp
        # print(dp)
        ans = sum(dp)
        return ans

n = 2
maxValue = 5

#n = 5
#maxValue = 3

solution = Solution()
print(solution.idealArrays(n, maxValue))
