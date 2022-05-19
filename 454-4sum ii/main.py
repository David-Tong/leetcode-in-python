class Solution(object):
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type nums3: List[int]
        :type nums4: List[int]
        :rtype: int
        """
        from collections import defaultdict
        dicts2 = defaultdict(int)
        for num in nums1:
            for num2 in nums2:
                dicts2[num + num2] += 1

        dicts3 = defaultdict(int)
        for key in dicts2:
            for num3 in nums3:
                dicts3[key + num3] += dicts2[key]

        ans = 0
        for num4 in nums4:
            if -1 * num4 in dicts3:
               ans += dicts3[-1 * num4]
        return ans


nums1 = [1,2]
nums2 = [-2,-1]
nums3 = [-1,2]
nums4 = [0,2]

nums1 = [0]
nums2 = [0]
nums3 = [0]
nums4 = [0]

nums1 = [-1,-1]
nums2 = [-1,1]
nums3 = [-1,1]
nums4 = [1,-1]

nums1 = [0,1,-1]
nums2 = [-1,1,0]
nums3 = [0,0,1]
nums4 = [-1,1,1]

solution = Solution()
print(solution.fourSumCount(nums1, nums2, nums3, nums4))
