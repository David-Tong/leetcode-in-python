class Solution(object):
    def isPossibleToSplit(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # process
        from collections import defaultdict
        dicts = defaultdict(int)
        for num in nums:
            dicts[num] += 1
            if dicts[num] > 2:
                return False
        return True


nums = [1,1,2,2,3,4]
nums = [1,1,1,1]

solution = Solution()
print(solution.isPossibleToSplit(nums))
