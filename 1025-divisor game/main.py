class Solution(object):
    def divisorGame(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n % 2 == 0


n = 2
n = 3

solution = Solution()
print(solution.divisorGame(n))
