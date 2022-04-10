class Solution(object):
    def isUgly(self, n):
        if n == 0:
            return True
        while n % 5 == 0:
            n = n // 5

        while n % 3 == 0:
            n = n // 3

        while n % 2 == 0:
            n = n // 2

        if n == 1:
            return True
        else:
            return False


solution = Solution()
print(solution.isUgly(0))
print(solution.isUgly(1))
print(solution.isUgly(14))
