class Solution(object):
    def minSwap(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        L = len(nums1)

        # dp
        # keep[x] - the minimal cost to keep the xth element in nums1
        # swap[x] - the minimal cost to swap the xth element in nums2
        keep = [float("inf")] * L
        swap = [float("inf")] * L
        keep[0] = 0
        swap[0] = 1

        for x in range(1, L):
            if nums1[x] > nums1[x - 1] and nums2[x] > nums2[x - 1]:
                keep[x] = min(keep[x], keep[x - 1])
                swap[x] = min(swap[x], swap[x - 1] + 1)
            if nums1[x] > nums2[x - 1] and nums2[x] > nums1[x - 1]:
                keep[x] = min(keep[x], swap[x - 1])
                swap[x] = min(swap[x], keep[x - 1] + 1)

        return min(keep[L - 1], swap[L - 1])


nums1 = [1,3,5,4]
nums2 = [1,2,3,7]

nums1 = [0,3,5,8,9]
nums2 = [2,1,4,6,9]

solution = Solution()
print(solution.minSwap(nums1, nums2))
