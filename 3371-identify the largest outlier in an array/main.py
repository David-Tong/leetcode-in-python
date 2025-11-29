class Solution(object):
    def getLargestOutlier(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # pre-process
        total = sum(nums)
        from collections import defaultdict
        dicts = defaultdict(int)
        for num in nums:
            dicts[num] += 1

        # process
        ans = float("-inf")
        for outlier in dicts.keys():
            if (total - outlier) % 2 == 0:
                special = (total - outlier) // 2
                if special == outlier:
                    if dicts[special] > 1:
                        ans = max(ans, outlier)
                else:
                    if dicts[special] > 0:
                        ans = max(ans, outlier)
        return ans


nums = [2,3,5,10]
nums = [-2,-1,-3,-6,4]
nums = [1,1,1,1,1,5,5]
nums = [-108,-108,-517]
nums = [874,159,-838,-375,658]
nums = [958,777,-746,566,989]

solution = Solution()
print(solution.getLargestOutlier(nums))
