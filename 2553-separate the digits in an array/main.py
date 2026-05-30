class Solution(object):
    def separateDigits(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # pre-process
        def digitize(num):
            res = list()
            while num:
                res.append(num % 10)
                num //= 10
            res.reverse()
            return res

        # process
        ans = list()
        for num in nums:
            ans.extend(digitize(num))
        return ans


nums = [13,25,83,77]

solution = Solution()
print(solution.separateDigits(nums))
