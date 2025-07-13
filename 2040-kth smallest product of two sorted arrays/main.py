class Solution(object):
    def kthSmallestProduct(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: int
        """
        # pre-process
        M, N = len(nums1), len(nums2)

        # helper function
        # hasK - if we have k products of two sorted array less or equal to limit
        from bisect import bisect_left, bisect_right
        def hasK(target):
            count = 0
            for num in nums1:
                if num > 0:
                    count += bisect_right(nums2, target // num)
                elif num < 0:
                    count += N - bisect_left(nums2, -(-target // num))
                else:
                    count += N if target >= 0 else 0
            return True if count >= k else False

        # process
        # binary search
        left, right = -10 ** 10, 10 ** 10
        while left + 1 < right:
            middle = (left + right) // 2
            if hasK(middle):
                right = middle
            else:
                left = middle + 1

        if hasK(left):
            return left
        else:
            return right


nums1 = [2,5]
nums2 = [3,4]
k = 2

nums1 = [-4,-2,0,3]
nums2 = [2,4]
k = 6

nums1 = [-2,-1,0,1,2]
nums2 = [-3,-1,2,4,5]
k = 3

nums1 = [-6]
nums2 = [-9]
k = 1

nums1 = [-10] * 5 * 10 ** 4
nums2 = [10] * 5 * 10 ** 4
k = 2500000000

import random
L = 5 * 10 ** 4
for x in range(L):
    nums1.append(random.randint(-1 * 10 ** 5, 10 ** 5))
    nums2.append(random.randint(-1 * 10 ** 5, 10 ** 5))
k = 2500000000

solution = Solution()
print(solution.kthSmallestProduct(nums1, nums2, k))
