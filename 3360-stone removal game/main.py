class Solution(object):
    def canAliceWin(self, n):
        """
        :type n: int
        :rtype: bool
        """
        k = 10
        c = 0
        while n >= k:
            n -= k
            k -= 1
            c += 1
        return False if c % 2 == 0 else True


n = 12
n = 1
n = 20
n = 28

solution = Solution()
print(solution.canAliceWin(n))
