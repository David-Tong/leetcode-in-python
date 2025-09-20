class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        num = n
        alternating = -1
        while num:
            bit = num & 1
            num >>= 1
            if alternating == -1:
                alternating = bit
            else:
                if bit == alternating:
                    return False
                else:
                    alternating = bit
        return True


n = 5
n = 7
n = 11

solution = Solution()
print(solution.hasAlternatingBits(n))


