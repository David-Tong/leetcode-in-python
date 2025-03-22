class Solution(object):
    def checkPowersOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        import math
        L = int(math.log(n, 3)) + 1

        def getPower(x):
            power = 0
            idx = 0
            while x:
                if x & 1:
                   power += 3 ** idx
                x >>= 1
                idx += 1
            return power

        for x in range(2 ** L):
            if getPower(x) == n:
                return True
        return False


n = 12
n = 91
n = 21
n = 1
n = 10 ** 7

solution = Solution()
print(solution.checkPowersOfThree(n))
