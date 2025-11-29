class Solution(object):
    def getSneakyNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # process
        s = set()
        ans = list()
        for num in nums:
            if num not in s:
                s.add(num)
            else:
                ans.append(num)
        return ans


nums = [0,1,1,0]
nums = [0,3,2,1,3,2]
nums = [7,1,5,4,3,4,6,0,9,5,8,2]

solution = Solution()
print(solution.getSneakyNumbers(nums))
