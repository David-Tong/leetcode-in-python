class Solution(object):
    def minRemoval(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # pre-process
        L = len(nums)
        nums = sorted(nums)
        print(nums)

        # helper function
        def valid(target):
            if target == 1:
                return True
            start = 0
            end = start + target - 1
            while end < L:
                if nums[start] * k >= nums[end]:
                    return True
                start += 1
                end = start + target - 1
            return False

        # process
        left, right = 1, L
        while left + 1 < right:
            middle = (left + right) // 2
            if valid(middle):
                left = middle
            else:
                right = middle - 1

        if valid(right):
            ans = L - right
        else:
            ans = L - left
        return ans


nums = [2,1,5]
k = 2

nums = [1,6,2,9]
k = 3

nums = [4,6]
k = 2

"""
from random import randint
nums = [randint(1, 10 ** 3) for _ in range(10 ** 2)]
print(nums)
k = 300
"""

nums = [157, 106, 124, 761, 865, 182, 912, 75, 695, 772, 465, 400, 981, 332, 519, 757, 683, 733, 649, 867, 755, 941, 444, 530, 338, 489, 396, 719, 280, 111, 673, 329, 740, 210, 427, 863, 633, 187, 327, 527, 728, 24, 252, 326, 355, 121, 777, 194, 336, 487, 671, 330, 414, 791, 944, 519, 476, 571, 911, 864, 854, 841, 960, 202, 732, 953, 997, 601, 794, 482, 312, 795, 304, 911, 555, 99, 124, 929, 559, 347, 649, 564, 989, 684, 67, 172, 673, 38, 119, 263, 97, 796, 783, 805, 752, 904, 838, 843, 121, 412]
k = 300

solution = Solution()
print(solution.minRemoval(nums, k))
