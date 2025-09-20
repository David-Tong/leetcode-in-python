class Solution(object):
    def flowerGame(self, n, m):
        """
        :type n: int
        :type m: int
        :rtype: int
        """
        # pre-process
        n_odds, n_evens = (n + 1) // 2, n // 2
        m_odds, m_evens = (m + 1) // 2, m // 2

        # process
        ans = n_odds * m_evens + n_evens * m_odds
        return ans


n = 3
m = 2

n = 1
m = 1

n = 10 ** 5
m = 10 ** 5

solution = Solution()
print(solution.flowerGame(n, m))
