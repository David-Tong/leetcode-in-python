class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        L = len(nums)
        total = L * (L + 1) / 2

        from collections import defaultdict
        dicts = defaultdict(int)
        for num in nums:
            dicts[num] += 1
            if dicts[num] == 2:
                one = num
            else:
                total -= num
        other = total

        return [one, other]


nums = [1,2,2,4]
nums = [1,1]

solution = Solution()
print(solution.findErrorNums(nums))
