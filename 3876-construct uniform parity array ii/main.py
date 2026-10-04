class Solution(object):
    def uniformArray(self, nums1):
        """
        :type nums1: List[int]
        :rtype: bool
        """
        # pre-process
        evens, odds = list(), list()
        for num1 in nums1:
            if num1 % 2 == 0:
                evens.append(num1)
            else:
                odds.append(num1)
        evens, odds = sorted(evens), sorted(odds)

        # process
        # case 1 : make nums1 to be even
        # only odd subtracts odd can be even
        # the smallest odd num1 can't find the another odd one less than itself to do operation 2
        # so the condition becomes no odd num1
        if len(odds) == 0:
            return True

        # case 2 :  make nums1 to be odd
        # only even subtracts odd can be odd
        # only if we have an odd number less than the smallest even num1
        if len(evens) == 0:
            return True

        if odds[0] < evens[0]:
            return True
        else:
            return False


nums1 = [1,4,7]
nums1 = [2,3]
nums1 = [4,6]

from random import randint
nums1 = list(set(randint(1, 10 ** 4) for _ in range(10 ** 3)))
print(nums1)

solution = Solution()
print(solution.uniformArray(nums1))
