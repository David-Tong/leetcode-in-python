class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        binary = bin(n)
        match = 1 << len(binary) - 3
        if n ^ match == 0:
            return True
        else:
            return False


n = 1
n = 16
n = 3
n = -2
n = 2 ** 31
n = 0

solution = Solution()
print(solution.isPowerOfTwo(n))