class Solution(object):
    def maxWidthRamp(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # pre-process
        L = len(nums)
        # get a strictly decreasing sequence from left to right
        lefts = list()
        lefts_idx = list()
        for x in range(L):
            if lefts:
                if lefts[-1] > nums[x]:
                    lefts.append(nums[x])
                    lefts_idx.append(x)
            else:
                lefts.append(nums[x])
                lefts_idx.append(x)
        # print(lefts)
        # print(lefts_idx)

        # get a strictly increasing sequence from right to left
        rights = list()
        rights_idx = list()
        for x in range(L - 1, -1, -1):
            if rights:
                if rights[-1] < nums[x]:
                    rights.append(nums[x])
                    rights_idx.append(x)
            else:
                rights.append(nums[x])
                rights_idx.append(x)
        # print(rights)
        # print(rights_idx)

        # process
        from bisect import bisect_left
        ans = 0
        for x in range(len(lefts)):
            left = lefts[x]
            left_idx = lefts_idx[x]
            idx = bisect_left(rights, left)
            if idx < len(rights):
                right_idx = rights_idx[idx]
            if left_idx < right_idx:
                ans = max(ans, right_idx - left_idx)
        return ans


nums = [6,0,8,2,1,5]
nums = [9,8,1,0,1,9,4,0,4,1]
nums = [1,2]
nums = [9,8,7,6,5,4,3,2,1]
nums = [1,2,3,4,5,6,7,8,9]
nums = [_ for _ in range(5 * 10 ** 4)]

solution = Solution()
print(solution.maxWidthRamp(nums))
