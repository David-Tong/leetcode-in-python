class Solution(object):
    def resultsArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # pre-process
        L = len(nums)
        slow, fast = 0, 0

        # process
        ans = list()
        while slow + k <= L:
            matched = True
            fast = max(slow, fast)
            while fast < slow + k:
                if fast > slow:
                    if nums[fast - 1] + 1 != nums[fast]:
                        matched = False
                        ans.append(-1)
                        break
                fast += 1
            if matched:
                ans.append(nums[fast - 1])
            slow += 1
        return ans


nums = [1,2,3,4,3,2,5]
k = 3

nums = [2,2,2,2,2]
k = 4

nums = [3,2,3,2,3,2]
k = 2

nums = [1,2,3,4,3,2,5,6,7]
k = 3

nums = [1]
k = 1

nums = [_ for _ in range(10 ** 5)]
k = 10000

solution = Solution()
print(solution.resultsArray(nums, k))