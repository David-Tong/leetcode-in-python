class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.anses = []

        # n - number of ( can append
        # m - number of ) can append
        def doGenerate(n, m, ans):
            if n == 0 and m == 0:
                self.anses.append(ans)

            # append (
            if n > 0:
                doGenerate(n - 1, m + 1, ans + "(")
            if m > 0:
                doGenerate(n, m - 1, ans + ")")

        doGenerate(n, 0, "")
        return self.anses


n = 1
n = 2
n = 3
n = 4
n = 8

solution = Solution()
print(solution.generateParenthesis(n))
