class Solution(object):
    def maximumSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # pro-process
        from collections import defaultdict
        dicts = defaultdict(list)

        # helper
        def getDigitsSum(num):
            total = 0
            for ch in str(num):
                total += int(ch)
            return total

        for num in nums:
            dicts[getDigitsSum(num)].append(num)

        # process
        ans = -1
        for key in dicts:
            items = sorted(dicts[key])
            if len(items) >= 2:
                ans = max(ans, items[-1] + items[-2])
        return ans


nums = [18,43,36,13,7]
nums = [10,12,19,14]

solution = Solution()
print(solution.maximumSum(nums))
