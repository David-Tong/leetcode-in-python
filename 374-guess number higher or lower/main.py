# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):

class Solution(object):

    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        def guess(num):
            pass

        left = 1
        right = n
        while left + 1 < right:
            middle = (left + right) // 2
            result = guess(middle)
            if result == 0:
                return middle
            elif result == 1:
                left = middle + 1
            else:
                right = middle - 1

        if guess(left) == 0:
            return left
        elif guess(right) == 0:
            return right