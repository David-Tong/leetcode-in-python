class Solution(object):
    def countTriples(self, n):
        """
        :type n: int
        :rtype: int
        """
        # pre-process
        SQUARES = [(x + 1) ** 2 for x in range(n)]

        # process
        ans = 0
        for x in range(n):
            for y in range(n):
                target = SQUARES[x] + SQUARES[y]
                if target in SQUARES:
                    ans += 1
        return ans


n = 5
n = 10

solution = Solution()
print(solution.countTriples(n))
