class Solution(object):
    def minimumOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # pre-process
        from collections import defaultdict
        dicts = defaultdict(int)
        for num in nums:
            if num > 0:
                dicts[num] += 1

        # process
        ans = len(dicts.keys())
        return ans


nums = [1,5,0,3,5]
nums = [0]

solution = Solution()
print(solution.minimumOperations(nums))
