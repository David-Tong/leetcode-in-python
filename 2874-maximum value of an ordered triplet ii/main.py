class Solution(object):
    def maximumTripletValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # pre-process
        L = len(nums)
        left_maxis, right_maxis = list(), list()
        for x in range(L):
            if x == 0:
                left_maxis.append(float("-inf"))
            else:
                left_maxis.append(max(left_maxis[-1], nums[x - 1]))
        for x in range(L - 1, -1, -1):
            if x == L - 1:
                right_maxis.append(float("-inf"))
            else:
                right_maxis.append(max(right_maxis[-1], nums[x + 1]))
        right_maxis = right_maxis[::-1]

        # print(left_maxis)
        # print(right_maxis)

        # process
        ans = 0
        for x in range(1, L - 1):
            ans = max(ans, (left_maxis[x] - nums[x]) * right_maxis[x])
        return ans


nums = [12,6,1,2,7]
nums = [1,10,3,4,19]
nums = [1,2,3]

solution = Solution()
print(solution.maximumTripletValue(nums))