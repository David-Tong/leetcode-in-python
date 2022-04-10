class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        def compare(num, num2):
            num = str(num)
            num2 = str(num2)

            if num + num2 < num2 + num:
                return -1
            elif num + num2 > num2 + num:
                return 1
            else:
                return 0

        from functools import cmp_to_key
        nums = sorted(nums, key=cmp_to_key(compare), reverse=True)
        ans = ""
        for num in nums:
            ans += str(num)
        if int(ans) == 0:
            return "0"
        else:
            return ans


nums = [3,30,34,5,9,99]
#nums = [3,300,30000,30000000]
nums = [10,2]
nums = [3,30,34,5,9]
nums = [0,0]

solution = Solution()
print(solution.largestNumber(nums))
