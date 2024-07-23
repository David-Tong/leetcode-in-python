class Solution(object):
    def frequencySort(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # pre-process
        from collections import defaultdict
        dicts = defaultdict(int)

        for num in nums:
            dicts[num] += 1

        num_freq = list()
        for num in dicts:
            num_freq.append((dicts[num], num))

        # process
        num_freq = sorted(num_freq, key=lambda x: (x[0], -1 * x[1]))
        ans = list()
        for freq, num in num_freq:
            for _ in range(freq):
                ans.append(num)
        return ans


nums = [1,1,2,2,2,3]
nums = [2,3,1,3,2]
nums = [-1,1,-6,4,5,-6,1,4,1]

solution = Solution()
print(solution.frequencySort(nums))
