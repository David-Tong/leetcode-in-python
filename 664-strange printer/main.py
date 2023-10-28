class Solution(object):
    def strangePrinter(self, s):
        """
        :type s: str
        :rtype: int
        """
        L = len(s)

        def printer(i, j):
            key = str(i) + "-" + str(j)
            if key in self.cache:
                return self.cache[key]

            if i > j:
                return 0
            elif i == j:
                return 1

            res = 1 + printer(i + 1, j)
            for k in range(i + 1, j + 1):
                if s[i] == s[k]:
                    res = min(res, printer(i, k - 1) + printer(k + 1, j))
            self.cache[key] = res
            return res

        from collections import defaultdict
        self.cache = defaultdict(int)
        ans = printer(0, L - 1)
        return ans


s = "aaabbb"
#s = "aba"

solution = Solution()
print(solution.strangePrinter(s))
