class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        def merge(nums1, nums2):
            merged = list()
            idx1, idx2 = 0, 0
            while idx1 < len(nums1) and idx2 < len(nums2):
                if nums1[idx1] <= nums2[idx2]:
                    merged.append(nums1[idx1])
                    idx1 += 1
                else:
                    merged.append(nums2[idx2])
                    idx2 += 1

            while idx1 < len(nums1):
                merged.append(nums1[idx1])
                idx1 += 1

            while idx2 < len(nums2):
                merged.append(nums2[idx2])
                idx2 += 1

            return merged

        def mergeSort(nums):
            if len(nums) <= 1:
                return nums

            middle = len(nums) // 2
            nums1 = mergeSort(nums[:middle])
            nums2 = mergeSort(nums[middle:])
            return merge(nums1, nums2)

        return mergeSort(nums)


nums = [1,3,7,8,2,4,5,6,9,10]
nums = [3] + [2] * 100000

solution = Solution()
print(solution.sortArray(nums))
