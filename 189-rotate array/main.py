class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        def rotateByGroup(nums, s, k):
            global count
            last = s + len(nums) - k
            tmp = nums[last]
            curr = last
            while curr != s:
                nums[curr] = nums[curr - k]
                curr = curr - k
                count += 1
                if curr < 0:
                    curr += len(nums)
            nums[s] = tmp
            count += 1

        global count
        count = 0
        k = k % len(nums)
        if k == 0: return nums
        groups = 1
        if len(nums) % k == 0:
            groups = k

        start = 0
        while start < len(nums) and count < len(nums):
            rotateByGroup(nums, start, k)
            start += 1

        return nums


nums = [1, 2, 3, 4, 5, 6, 7]
k = 3

nums = [-1, -100, 3, 99]
k = 2

#nums = [1,2,3,4,5,6]
#k = 4

solution = Solution()
print(solution.rotate(nums, k))
