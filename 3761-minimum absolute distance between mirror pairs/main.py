class Solution(object):
    def minMirrorPairDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # pre-process
        # helper function
        def reverse(num):
            return int(str(num)[::-1])

        # process
        from collections import defaultdict
        dicts = defaultdict(int)

        ans = float('inf')
        for idx, num in enumerate(nums):
            if num in dicts:
                ans = min(ans, idx - dicts[num])
            dicts[reverse(num)] = idx
        return -1 if ans == float('inf') else ans


nums = [12,21,45,33,54]
nums = [120,21]
nums = [21,120]

solution = Solution()
print(solution.minMirrorPairDistance(nums))
