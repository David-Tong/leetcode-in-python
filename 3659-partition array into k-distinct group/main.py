class Solution(object):
    def partitionArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        # pre-process
        L = len(nums)
        if L % k != 0:
            return False
        D = L // k

        from collections import defaultdict
        dicts = defaultdict(int)
        for num in nums:
            dicts[num] += 1

        # process
        for num in dicts:
            if dicts[num] > D:
                return False
        return True


nums = [1,2,3,4]
k = 2

nums = [3, 5, 2, 2]
k = 2

nums = [1,5,2,3]
k = 3

solution = Solution()
print(solution.partitionArray(nums, k))
