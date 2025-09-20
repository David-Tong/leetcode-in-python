class Solution(object):
    def partitionDisjoint(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # pre-process
        L = len(nums)
        maxis = list()
        for x in range(L):
            if maxis:
                maxis.append(max(maxis[-1], nums[x]))
            else:
                maxis.append(nums[x])
        minis = list()
        for x in range(L - 1, -1, -1):
            if minis:
                minis.append(min(minis[-1], nums[x]))
            else:
                minis.append(nums[x])
        minis = minis[::-1]

        # print(maxis)
        # print(minis)

        # process
        for x in range(0, L - 1):
            if maxis[x] <= minis[x + 1]:
                return x + 1


nums = [5,0,3,8,6]
nums = [1,1,1,0,6,12]
nums = [1,2]

solution = Solution()
print(solution.partitionDisjoint(nums))
