class Solution(object):
    def findSmallestInteger(self, nums, value):
        """
        :type nums: List[int]
        :type value: int
        :rtype: int
        """
        # pre-process
        from collections import defaultdict
        dicts = defaultdict(int)
        for v in range(value):
            dicts[v] = 0
        for num in nums:
            mod = num % value
            dicts[mod] += 1
        print(dicts)

        # process
        mini_count = min(dicts.values())
        for v in range(value):
            if dicts[v] == mini_count:
                return value * mini_count + v


nums = [1,-10,7,13,6,8]
value = 5

nums = [1,-10,7,13,6,8]
value = 7

nums = [11,12,13,11,12,13]
value = 3

nums = [0] * 10 ** 5
value  = 10

solution = Solution()
print(solution.findSmallestInteger(nums, value))
