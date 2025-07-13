class Solution(object):
    def arrayChange(self, nums, operations):
        """
        :type nums: List[int]
        :type operations: List[List[int]]
        :rtype: List[int]
        """
        # pre-process
        L = len(nums)
        from collections import defaultdict
        dicts = defaultdict(int)
        for idx, num in enumerate(nums):
            dicts[num] = idx

        # process
        for operation in operations:
            old, new = operation
            dicts[new] = dicts[old]
            del dicts[old]

        # post-process
        ans = [0] * L
        for key in dicts:
            ans[dicts[key]] = key
        return ans


nums = [1,2,4,6]
operations = [[1,3],[4,7],[6,1]]

nums = [1,2]
operations = [[1,3],[2,1],[3,2]]

solution = Solution()
print(solution.arrayChange(nums, operations))
