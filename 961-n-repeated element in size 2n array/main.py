class Solution(object):
    def repeatedNTimes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # pre-process
        s = set()

        # process
        for num in nums:
            if num in s:
                return num
            else:
                s.add(num)


nums = [1,2,3,3]

solution = Solution()
print(solution.repeatedNTimes(nums))
