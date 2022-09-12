class Solution(object):
    def lastRemaining(self, n):
        """
        :type n: int
        :rtype: int
        """
        def doRemain(n, times):
            if n == 1:
                return

            if times % 2 == 0:
                self.remains.append(0)
            else:
                if n % 2 == 1:
                    self.remains.append(0)
                else:
                    self.remains.append(1)
            doRemain(n // 2, times + 1)

        self.remains = list()
        doRemain(n, 0)

        ans = 1
        for remain in self.remains[::-1]:
            if remain == 1:
                ans = ans * 2 - 1
            else:
                ans = ans * 2

        return ans


n = 9
n = 1
n = 7

solution = Solution()
print(solution.lastRemaining(n))

