class Solution(object):
    def check(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # pre-process
        L = len(nums)
        mini = float("inf")
        starts = list()
        for x in range(L):
            if nums[x] < mini:
                mini = nums[x]
            if nums[x] == mini:
                starts.append(x)

        # process
        for start in starts:
            sort = True
            for x in range(L - 1):
                idx = (start + x) % L
                nxt_idx = (idx + 1) % L
                if nums[idx] > nums[nxt_idx]:
                    sort = False
                    break
            if sort:
                return True
        return False


nums = [3,4,5,1,2]
nums = [2,1,3,4]
nums = [1,2,3]
nums = [1,1,1]
nums = [6,10,6]

solution = Solution()
print(solution.check(nums))
