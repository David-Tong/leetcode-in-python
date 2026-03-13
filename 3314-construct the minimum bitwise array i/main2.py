class Solution(object):
    def minBitwiseArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # pre-process
        L = 1024
        from collections import defaultdict
        dicts = defaultdict(int)
        for x in range(L):
            target = (x + 1) | (x + 2)
            if target not in dicts:
                dicts[target] = x + 1

        # process
        ans = list()
        for num in nums:
            if num not in dicts:
                ans.append(-1)
            else:
                ans.append(dicts[num])
        return ans


nums = [2,3,5,7]
nums = [11,13,31]
nums = [491, 827, 991]

solution = Solution()
print(solution.minBitwiseArray(nums))
