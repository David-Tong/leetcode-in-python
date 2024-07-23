class Solution(object):
    def reductionOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # pre-process
        from collections import defaultdict
        dicts = defaultdict(int)

        for num in nums:
            dicts[num] += 1

        freqs = list()
        for key in sorted(dicts.keys()):
            freqs.append(dicts[key])

        # process
        ans = 0
        for idx, freq in enumerate(freqs):
            ans += idx * freq
        return ans


nums = [5,1,3]
nums = [1,1,1]
nums = [1,1,2,2,3]

solution = Solution()
print(solution.reductionOperations(nums))
