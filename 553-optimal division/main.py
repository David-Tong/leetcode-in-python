class Solution(object):
    def optimalDivision(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        expr = ""
        L = len(nums)

        if L == 1:
            return str(nums[0])
        elif L == 2:
            return str(nums[0]) + "/" + str(nums[1])

        for idx, num in enumerate(nums):
            if idx == L - 1:
                expr += str(nums[idx]) + ")"
            elif idx == 1:
                expr += "(" + str(nums[idx]) + "/"
            else:
                expr += str(nums[idx]) + "/"

        return expr


nums = [1000,100,10,2]
nums = [2,3,4]
nums = [2]
nums = [2,3]

solution = Solution()
print(solution.optimalDivision(nums))
