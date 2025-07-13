class Solution(object):
    def maxSubsequence(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # pre-process
        numbers = list()
        for idx, num in enumerate(nums):
            numbers.append((idx, num))
        numbers = sorted(numbers, key=lambda x: x[1])

        # process
        numbers = numbers[-k:]
        numbers = sorted(numbers, key=lambda x: x[0])
        ans = [number for idx, number in numbers]
        return ans


nums = [2,1,3,3]
k = 2

nums = [-1,-2,3,4]
k = 3

nums = [3,4,3,3]
k = 2

nums = [50,-75]
k = 2

solution = Solution()
print(solution.maxSubsequence(nums, k))
