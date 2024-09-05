class Solution(object):
    def numberOfWays(self, startPos, endPos, k):
        """
        :type startPos: int
        :type endPos: int
        :type k: int
        :rtype: int
        """
        MODULO = 10 ** 9 + 7

        def combination(n, k):
            from math import factorial
            return factorial(n) // (factorial(k) * factorial(n - k))

        # pre-process
        temp = (endPos - startPos) + k
        if temp % 2 != 0:
            return 0

        positive = temp // 2
        negative = k - positive

        if positive < 0 or negative < 0:
            return 0

        # process
        ans = combination(positive + negative, negative) % MODULO
        return ans


startPos = 1
endPos = 2
k = 3

startPos = 2
endPos = 5
k = 10

startPos = 1
endPos = 2
k = 7

startPos = 1
endPos = 6
k = 19

startPos = 800
endPos = 105
k = 999

startPos = 1
endPos = 10
k = 3

solution = Solution()
print(solution.numberOfWays(startPos, endPos, k))
