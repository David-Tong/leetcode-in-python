class Solution(object):
    def advantageCount(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # pre-process
        L = len(nums1)

        pairs2 = sorted(zip(nums2, list(range(L))))
        nums1 = sorted(nums1)

        # process
        idx = 0
        idx2 = 0

        ans = [0] * L
        remains = list()
        while idx < L:
            if nums1[idx] <= pairs2[idx2][0]:
                remains.append(nums1[idx])
                idx += 1
            else:
                ans[pairs2[idx2][1]] = nums1[idx]
                idx += 1
                idx2 += 1

        remains.extend(nums1[idx:])

        idx = 0
        while idx2 < L:
            ans[pairs2[idx2][1]] = remains[idx]
            idx += 1
            idx2 += 1
        return ans


nums1 = [2,7,11,15]
nums2 = [1,10,4,11]

nums1 = [12,24,8,32]
nums2 = [13,25,32,11]

nums1 = [22,34,5,1,2,3,1,3,35,11]
nums2 = [23,11,1,5,6,7,8,11,2,1]

solution = Solution()
print(solution.advantageCount(nums1, nums2))
