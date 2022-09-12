class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        BITS = 32
        z = x ^ y

        bit = 0
        ans = 0
        while bit < BITS:
            if z & 1 == 1:
                ans += 1
            z = z >> 1
            bit += 1

        return ans


x = 1
y = 4

x = 3
y = 1

solution = Solution()
print(solution.hammingDistance(x, y))
