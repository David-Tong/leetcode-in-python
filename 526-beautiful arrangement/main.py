class Solution(object):
    def countArrangement(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.ans = 0
        def doArrangement(n, idx, used):
            if len(used) == n:
                self.ans += 1
                return

            for x in range(1, n + 1):
                go = False
                if x not in used:
                    if x % idx == 0:
                        go = True
                    if idx % x == 0:
                        go = True
                    if go:
                        doArrangement(n, idx + 1, used + [x])
        doArrangement(n, 1, list())
        return self.ans


n = 2
n = 1
n = 8
n = 10
n = 15

solution = Solution()
print(solution.countArrangement(n))
