class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        N = len(nums)

        from collections import defaultdict
        dicts = defaultdict(int)

        for num in nums:
            dicts[num] += 1

        if N % 2 == 0:
            idx = N - 2
        else:
            idx = N - 1

        for key in sorted(dicts):
            while dicts[key] > 0:
                if idx >= 0:
                    nums[idx] = key
                    dicts[key] -= 1
                    idx -= 2
                else:
                    if N % 2 == 0:
                        idx = N - 1
                    else:
                        idx = N - 2
        return nums


nums = [1,5,1,1,6,4]
#nums = [1,3,2,2,3,1]
nums = [4,5,5,6]
nums = [1,2,2,2,3,3]

solution = Solution()
print(solution.wiggleSort(nums))
