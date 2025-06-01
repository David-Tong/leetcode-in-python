class Solution(object):
    def distributeCandies(self, n, limit):
        """
        :type n: int
        :type limit: int
        :rtype: int
        """
        # process
        ans = 0
        total = min(n + 1, limit + 1)
        for x in range(total):
            remain = n - x
            low, high = max(0, remain - limit), remain
            if low <= limit:
                ans += min(limit, high) - low + 1
        return ans


n = 5
limit = 2

n = 3
limit = 3

n = 1
limit = 3

solution = Solution()
print(solution.distributeCandies(n, limit))
