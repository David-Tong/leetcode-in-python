class Solution(object):
    def countBadPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # pre-process
        L = len(nums)

        # convert nums[j] - nums[i] == j - i
        # to nums[i] - i == nums[j] - j
        from collections import defaultdict
        dicts = defaultdict(int)
        for idx, num in enumerate(nums):
            dicts[num - idx] += 1

        # process
        # count the number of good pairs
        pairs = 0
        for num in dicts:
            count = dicts[num]
            pairs += count * (count - 1) // 2

        # post-process
        ans = L * (L - 1) // 2 - pairs
        return ans


nums = [4,1,3,3]
nums = [1,2,3,4,5]
nums = [1,6,3,8,5]

solution = Solution()
print(solution.countBadPairs(nums))
