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
        # search
        def search(num, target):
            left, right = 0, N - 1
            if num >= 0:
                while left + 1 < right:
                    middle = (left + right) // 2
                    if nums2[middle] * num <= target:
                        left = middle
                    else:
                        right = middle - 1

                if nums2[right] * num <= target:
                    return right
                elif nums2[left] * num <= target:
                    return left
                else:
                    return -1
            else:
                while left + 1 < right:
                    middle = (left + right) // 2
                    if nums2[middle] * num <= target:
                        right = middle
                    else:
                        left = middle + 1

                if nums2[left] * num <= target:
                    return left
                elif nums2[right] * num <= target:
                    return right
                else:
                    return -1

        # hasK - if we have k products of two sorted array less or equal to limit
        def hasK(target):
            count = 0
            for num in nums1:
                idx = search(num, target)
                if idx >= 0:
                    if num >= 0:
                        count += idx + 1
                    else:
                        count += N - idx
            return True if count >= k else False

        # print(hasK(8))

        # process
        # binary search
        left, right = -10 ** 10, 10 ** 10
        while left + 1 < right:
            middle = (left + right) // 2
            print(middle)
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

"""
nums1 = [-4,-2,0,3]
nums2 = [2,4]
k = 6

nums1 = [-2,-1,0,1,2]
nums2 = [-3,-1,2,4,5]
k = 3

nums1 = [-6]
nums2 = [-9]
k = 1
"""

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
