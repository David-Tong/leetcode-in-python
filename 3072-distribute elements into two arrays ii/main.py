class Solution(object):
    def resultArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # pre-process
        L = len(nums)
        
        # process
        from sortedcontainers import SortedList
        sl1 = SortedList()
        sl2 = SortedList()
        nums1 = list()
        nums2 = list()

        sl1.add(nums[0])
        sl2.add(nums[1])
        nums1.append(nums[0])
        nums2.append(nums[1])

        idx = 2
        while idx < L:
            num = nums[idx]
            greater1 = len(nums1) - sl1.bisect_right(num)
            greater2 = len(nums2) - sl2.bisect_right(num)
            if greater1 > greater2:
                sl1.add(num)
                nums1.append(num)
            elif greater1 < greater2:
                sl2.add(num)
                nums2.append(num)
            else:
                if len(nums1) <= len(nums2):
                    sl1.add(num)
                    nums1.append(num)
                else:
                    sl2.add(num)
                    nums2.append(num)
            idx += 1

        ans = nums1 + nums2
        return ans


nums = [2,1,3,3]
nums = [5,14,3,1,2]
nums = [3,3,3,3]
nums = [1,1,1]
nums = [10,7,10,9,6,8,10,10,5,8,7,4,1,8,2,4,7,2,1,7]

"""
from random import randint
nums = [randint(1, 10) for _ in range(20)]
print(nums)
"""

solution = Solution()
print(solution.resultArray(nums))
