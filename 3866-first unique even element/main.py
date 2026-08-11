class Solution(object):
    def firstUniqueEven(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # pre-process
        from collections import Counter
        counter = Counter(nums)

        # process
        for num in nums:
            if num % 2 == 0:
                if counter[num] == 1:
                    return num
        return -1

nums = [3,4,2,5,4,6]
nums = [4,4]

solution = Solution()
print(solution.firstUniqueEven(nums))
