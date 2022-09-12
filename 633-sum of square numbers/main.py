class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        from math import sqrt
        left = 0
        right = int(sqrt(c))

        while left <= right:
            s = left ** 2 + right ** 2
            if s < c:
                left += 1
            elif s > c:
                right -= 1
            else:
                return True
        return False


c = 5
c = 3
c = 2 ** 31 - 1
c = 10
c = 4
c = 2

solution = Solution()
print(solution.judgeSquareSum(c))
