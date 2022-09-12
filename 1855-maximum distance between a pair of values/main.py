class Solution(object):
    def maxDistance(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        def binarySearch(nums, key, left):
            right = len(nums) - 1
            while left + 1 < right:
                middle = (left + right) // 2
                if key <= nums[middle]:
                    left = middle
                else:
                    right = middle

            if nums[right] >= key:
                return right
            else:
                return left

        ans = 0
        for idx, num in enumerate(nums1):
            idx2 = binarySearch(nums2, num, idx)
            ans = max(ans, idx2 - idx)

        return ans


nums1 = [55,30,5,4,2]
nums2 = [100,20,10,10,5]

nums1 = [2,2,2]
nums2 = [10,10,1]

nums1 = [30,29,19,5]
nums2 = [25,25,25,25,25]

nums1 = [2]
nums2 = [3]

solution = Solution()
print(solution.maxDistance(nums1, nums2))
