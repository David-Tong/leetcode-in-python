class Solution(object):
    def resultArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # pre-process
        L = len(nums)

        # process
        nums1, nums2 = list(), list()
        nums1.append(nums[0])
        nums2.append(nums[1])

        idx = 2
        while idx < L:
            if nums1[-1] > nums2[-1]:
                nums1.append(nums[idx])
            else:
                nums2.append(nums[idx])
            idx += 1

        nums1.extend(nums2)
        ans = nums1
        return ans


nums = [2,1,3]
nums = [5,4,3,8]

solution = Solution()
print(solution.resultArray(nums))
