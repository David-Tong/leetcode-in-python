class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        import sys
        sys.setrecursionlimit(50000)

        def swap(nums, x, y):
            nums[x], nums[y] = nums[y], nums[x]

        def ordered(nums, left, right):
            idx = left
            while idx < right:
                if nums[idx] > nums[idx + 1]:
                    return False
                idx += 1
            return True

        def partition(nums, left, right):
            from random import randint
            pivot = randint(left, right)
            swap(nums, pivot, left)
            index = left + 1
            x = index
            while x <= right:
                if nums[x] < nums[left]:
                    swap(nums, x, index)
                    index += 1
                x += 1
            swap(nums, left, index - 1)
            return index - 1

        def quickSort(nums, left, right):
            # short cut
            if ordered(nums, left, right):
                return nums

            if left < right:
                index = partition(nums, left, right)
                quickSort(nums, left, index - 1)
                quickSort(nums, index + 1, right)
            return nums

        return quickSort(nums, 0, len(nums) - 1)


nums = [1,3,7,8,2,4,5,6,9,10]
nums = [3] + [2] * 100000

solution = Solution()
print(solution.sortArray(nums))
