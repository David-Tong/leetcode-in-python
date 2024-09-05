class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1

        N = 33
        pows = [0] * N
        pows[0] = 1
        pows[1] = x

        for x in range(2, N):
            pows[x] = pows[x - 1] * pows[x - 1]

        ans = 1
        power = abs(n)
        digit = 0
        while digit < N:
            if power >> digit & 1:
                ans *= pows[digit + 1]
            digit += 1

        return ans if n > 0 else 1.0 / ans


x = 2.0000
n = 10

x = 1.0001
n = 2147483647

x = 2.10000
n = 3

x = -2.1000
n = 3

x = 2.00000
n = -2

x = 42.38803
n = 1

x = 1.00000
n = -2147483648

solution = Solution()
print(solution.myPow(x, n))
