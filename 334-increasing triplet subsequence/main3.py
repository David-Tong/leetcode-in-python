class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # pre-process
        L = len(nums)
        min_lefts = list()
        min_left = float("inf")
        for x in range(L):
            if nums[x] < min_left:
                min_left = nums[x]
            min_lefts.append(min_left)
        max_rights = list()
        max_right = float("-inf")
        for x in range(L - 1, -1, -1):
            if nums[x] > max_right:
                max_right = nums[x]
            max_rights.append(max_right)
        max_rights = max_rights[::-1]

        print(min_lefts)
        print(max_rights)

        # process
        for x in range(1, L - 1):
            print(x)
            if min_lefts[x - 1] < nums[x] < max_rights[x + 1]:
                return True
        return False


nums = [1,2,3,4,5]
nums = [5,4,3,2,1]
nums = [2,1,5,0,4,6]
nums = [3,1,4,2,5]
nums = [3,1,4,2,2]
nums = [1,2]
nums = [1,1,-2,6]
nums = [1,5,0,4,1,3]
#nums = [0,4,2,1,0,-1,-3]

solution = Solution()
print(solution.increasingTriplet(nums))
