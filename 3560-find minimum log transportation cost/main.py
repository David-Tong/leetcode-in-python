class Solution(object):
    def minCuttingCost(self, n, m, k):
        """
        :type n: int
        :type m: int
        :type k: int
        :rtype: int
        """
        # process
        ans = 0
        if n > k:
            ans = (n - k) * k
        elif m > k:
            ans = (m - k) * k
        return ans


n = 6
m = 5
k = 5

n = 4
m = 4
k = 6

solution = Solution()
print(solution.minCuttingCost(n, m, k))