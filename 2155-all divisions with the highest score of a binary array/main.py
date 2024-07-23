class Solution(object):
    def maxScoreIndices(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # pre-process
        presums = [0]
        for num in nums:
            presums.append(presums[-1] + num)

        # process
        L = len(presums)
        maxi = 0
        ans = list()
        for x in range(L):
            if x == 0:
                left_score = 0
            else:
                left_score = x - presums[x]
            if x == L - 1:
                right_score = 0
            else:
                right_score = presums[-1] - presums[x]
            if left_score + right_score > maxi:
                maxi = left_score + right_score
                ans = [x]
            elif left_score + right_score == maxi:
                ans.append(x)
        return ans


nums = [0,0,1,0]
nums = [0,0,0]
nums = [1,1]

solution = Solution()
print(solution.maxScoreIndices(nums))
