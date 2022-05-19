class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        left = 1
        right = 2 ** 31 - 1
        while left + 1 < right:
            middle = (left + right) // 2
            square = middle * middle
            if square == num:
                return True
            elif square < num:
                left = middle + 1
            else:
                right = middle - 1

        if left * left == num:
            return True
        elif right * right == num:
            return True
        else:
            return False


num = 16
num = 14
num = 1

solution = Solution()
print(solution.isPerfectSquare(num))
