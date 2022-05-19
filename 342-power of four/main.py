class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        left = 0
        right = 30
        while left + 1 < right:
            middle = (left + right) // 2
            four_power = 4 ** middle
            if four_power < n:
                left = middle + 1
            elif four_power > n:
                right = middle - 1
            else:
                return True

        if 4 ** right == n:
            return True
        elif 4 ** left == n:
            return True
        else:
            return False


n = 16
#n = 5
#n = -16
#n = -64
#n = 1
#n = 0
#n = 2
#n = -4

solution = Solution()
print(solution.isPowerOfFour(n))
