class Solution(object):
    def getCommon(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        # pre-process
        M, N = len(nums1), len(nums2)
        idx, idx2 = 0, 0

        # process
        while idx < M and idx2 < N:
            if nums1[idx] == nums2[idx2]:
                return nums1[idx]
            elif nums1[idx] < nums2[idx2]:
                idx += 1
            else:
                idx2 += 1
        return -1


nums1 = [1,2,3]
nums2 = [2,4]

nums1 = [1,2,3,6]
nums2 = [2,3,4,5]

nums1 = [1,2,3,4,5]
nums2 = [6,7,8,9,10]

nums1 = [5,6,7,8,9]
nums2 = [1,2,3,5]

nums1 = [1]
nums2 = [1]

solution = Solution()
print(solution.getCommon(nums1, nums2))
