class Solution(object):
    def numberOfPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # pre-process
        from collections import defaultdict
        dicts = defaultdict(int)
        for num in nums:
            dicts[num] += 1

        # process
        pairs, leftover = 0, 0
        for num in dicts.keys():
            pairs += dicts[num] // 2
            leftover += dicts[num] % 2
        return [pairs, leftover]


nums = [1,3,2,1,3,2,2]
nums = [1,1]
nums = [0]

solution = Solution()
print(solution.numberOfPairs(nums))
