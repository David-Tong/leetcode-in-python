class Solution(object):
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        self.anses = []
        def doLexical(n, digit, number):
            for x in range(0, 10):
                if digit == 1 and x == 0:
                    continue
                next_number = number * 10 + x
                if next_number > n:
                    return
                self.anses.append(next_number)
                doLexical(n, digit + 1, next_number)
        doLexical(n, 1, 0)
        return self.anses


n = 13
n = 2
n = 50000

solution = Solution()
print(solution.lexicalOrder(n))
