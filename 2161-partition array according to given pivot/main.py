class Solution(object):
    def pivotArray(self, nums, pivot):
        """
        :type nums: List[int]
        :type pivot: int
        :rtype: List[int]
        """
        lt = list()
        gt = list()
        count = 0
        for num in nums:
            if num < pivot:
                lt.append(num)
            elif num > pivot:
                gt.append(num)
            else:
                count += 1

        return lt + [pivot] * count + gt


nums = [9,12,5,10,14,3,10]
pivot = 10

nums = [-3,4,3,2]
pivot = 2

solution = Solution()
print(solution.pivotArray(nums, pivot))
