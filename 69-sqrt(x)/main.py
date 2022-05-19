class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        left = 0
        right = 2 ** 31 - 1
        while left + 1 < right:
            middle = (left + right) // 2
            if middle * middle < x:
                left = middle + 1
            elif middle * middle > x:
                right = middle - 1
            else:
                return middle

        if right * right <= x:
            return right
        elif left * left <= x:
            return left
        else:
            return left - 1


x = 4
#x = 5
#x = 10
#x = 8
#x = 26

solution = Solution()
print(solution.mySqrt(x))
