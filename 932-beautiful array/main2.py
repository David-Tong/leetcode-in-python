class Solution(object):
    def beautifulArray(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        def makeArray(n):
            if n == 1:
                return [1]
            else:
                return ([2 * x - 1 for x in makeArray((n + 1) // 2)]
                        + [2 * x for x in makeArray(n // 2)])

        return makeArray(n)


n = 4
n = 5

solution = Solution()
print(solution.beautifulArray(n))
