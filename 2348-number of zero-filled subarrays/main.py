class Solution(object):
    def zeroFilledSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def countSum(l):
            return l * (l + 1) // 2

        was_zero = False
        zeros = list()
        for idx, num in enumerate(nums):
            if num == 0:
                if not was_zero:
                    was_zero = True
                    zeros.append([idx, -1])
            elif num != 0:
                if was_zero:
                    was_zero = False
                    zeros[-1][1] = idx
        if was_zero:
            zeros[-1][1] = idx + 1

        ans = 0
        for zero in zeros:
            ans += countSum(zero[1] - zero[0])
        return ans


nums = [1,3,0,0,2,0,0,4]
nums = [0,0,0,2,0,0]
nums = [0,1,3,0,0,2,0,0,4,0]
nums = [2,10,2019]
nums = [0]

solution = Solution()

print(solution.zeroFilledSubarray(nums))
