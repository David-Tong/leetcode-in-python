class Solution(object):
    def mergeArrays(self, nums1, nums2):
        """
        :type nums1: List[List[int]]
        :type nums2: List[List[int]]
        :rtype: List[List[int]]
        """
        # pre-process
        from collections import defaultdict
        dicts = defaultdict(int)
        for pair in nums1:
            dicts[pair[0]] += pair[1]
        for pair in nums2:
            dicts[pair[0]] += pair[1]

        # process
        ans = list()
        for key in sorted(dicts.keys()):
            ans.append([key, dicts[key]])
        return ans


nums1 = [[1,2],[2,3],[4,5]]
nums2 = [[1,4],[3,2],[4,1]]

nums1 = [[2,4],[3,6],[5,5]]
nums2 = [[1,3],[4,3]]

solution = Solution()
print(solution.mergeArrays(nums1, nums2))
