class Solution(object):
    def maxFrequencyElements(self, nums):
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
        rever = defaultdict(int)
        for val in dicts.values():
            rever[val] += 1
        maxi = max(rever.keys())

        ans = rever[maxi] * maxi
        return ans


nums = [1,2,2,3,1,4]
nums = [1,2,3,4,5]

solution = Solution()
print(solution.maxFrequencyElements(nums))
