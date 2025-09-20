class Solution(object):
    def countHillValley(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # pre-process
        processed = list()
        for num in nums:
            if not processed or num != processed[-1]:
                processed.append(num)
        # print(processed)

        # process
        L = len(processed)
        ans = 0
        for x in range(1, L - 1):
            if processed[x - 1] < processed[x] > processed[x + 1]:
                ans += 1
            if processed[x - 1] > processed[x] < processed[x + 1]:
                ans += 1
        return ans


nums = [2,4,1,1,6,5]
# nums = [6,6,5,5,4,1]

solution = Solution()
print(solution.countHillValley(nums))
