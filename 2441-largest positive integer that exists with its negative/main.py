class Solution(object):
    def findMaxK(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # pre-process
        from collections import defaultdict
        dicts = defaultdict(bool)
        for num in nums:
            dicts[num] = True

        # process
        matched = list()
        for num in nums:
            if num > 0:
                if -1 * num in dicts:
                    matched.append(num)
        ans = max(matched) if matched else -1
        return ans


nums = [-1,2,-3,3]
nums = [-1,10,6,7,-7,1]
nums = [-10,8,6,7,-2,-3]

solution = Solution()
print(solution.findMaxK(nums))
