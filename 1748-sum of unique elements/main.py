class Solution(object):
    def sumOfUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # pre-process
        from collections import defaultdict
        dicts = defaultdict(int)
        for num in nums:
            dicts[num] += 1

        # process
        ans = 0
        for num in dicts:
            if dicts[num] == 1:
               ans += num
        return ans


nums = [1,2,3,2]
# nums = [1,1,1,1,1]
nums = [1,2,3,4,5]

solution = Solution()
print(solution.sumOfUnique(nums))
