class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = 0
        while n > 0:
            if n & 1 == 1:
                ans += 1
            n >>= 1
        return ans


n = 0b00000000000000000000000000001011
n = 0b00000000000000000000000010000000
n = 0b11111111111111111111111111111101

solution = Solution()
print(solution.hammingWeight(n))