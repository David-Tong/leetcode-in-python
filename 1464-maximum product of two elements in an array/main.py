class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxi = 0
        maxi2 = 0

        for num in nums:
            if num > maxi:
                tmp = maxi
                maxi = num
                if tmp > maxi2:
                    maxi2 = tmp
            elif num > maxi2:
                maxi2 = num

        return (maxi - 1) * (maxi2 - 1)


nums = [3,4,5,2]
nums = [1,5,4,5]
nums = [3,7]
nums = [9,10,3,4,5]

solution = Solution()
print(solution.maxProduct(nums))
