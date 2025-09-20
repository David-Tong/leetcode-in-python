class Solution(object):
    def largestInteger(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # pre-process
        L = len(nums)
        from collections import defaultdict
        dicts = defaultdict(int)
        for num in nums:
            dicts[num] += 1

        # process
        if k == 1:
            for num in sorted(nums, reverse=True):
                if dicts[num] == 1:
                    return num
            return -1
        elif k == L:
            return max(nums)
        else:
            maxi, mini = max(nums[0], nums[-1]), min(nums[0], nums[-1])
            if dicts[maxi] == 1:
                return maxi
            elif dicts[mini] == 1:
                return mini
            else:
                return -1


nums = [3,9,2,1,7]
k = 3

nums = [3,9,7,2,1,7]
k = 4

nums = [0,0]
k = 1

nums = [0,0]
k = 2

solution = Solution()
print(solution.largestInteger(nums, k))
