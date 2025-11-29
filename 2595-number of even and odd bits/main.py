class Solution(object):
    def evenOddBit(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        # process
        even, odd = 0, 0
        idx = 0
        while n:
            if n % 2 == 1:
                if idx % 2 == 0:
                    even += 1
                else:
                    odd += 1
            n >>= 1
            idx += 1
        ans = [even, odd]
        return ans


n = 50
n = 2

solution = Solution()
print(solution.evenOddBit(n))
