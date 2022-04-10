class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 2:
            return 1
        elif n == 3:
            return 2

        div3 = n // 3
        remain3 = n % 3
        if remain3 == 1:
            div3 -= 1
            remain3 += 3

        div2 = remain3 // 2
        return pow(3, div3) * pow(2, div2)


n = 2
n = 3
n = 10

solution = Solution()
print(solution.integerBreak(n))
