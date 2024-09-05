class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from collections import defaultdict
        dicts = defaultdict(int)
        mins = defaultdict(int)
        maxs = defaultdict(int)

        for idx, num in enumerate(nums):
            dicts[num] += 1
            if num not in mins:
                mins[num] = idx
            maxs[num] = idx

        maxi = max(dicts.values())

        ans = float("inf")
        for key in dicts:
            if dicts[key] == maxi:
                ans = min(ans, maxs[key] - mins[key] + 1)
        return ans


nums = [1,2,2,3,1]

solution = Solution()
print(solution.findShortestSubArray(nums))
