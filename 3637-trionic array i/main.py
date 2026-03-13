class Solution(object):
    def isTrionic(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # pre-process
        L = len(nums)
        flag = 0

        # process
        idx = 0
        count = 0
        while idx < L - 1:
            if nums[idx] == nums[idx + 1]:
                return False
            if flag == 0 or flag == 2:
                if nums[idx] < nums[idx + 1]:
                    count += 1
                else:
                    if count == 0:
                        return False
                    else:
                        if flag == 0:
                            flag = 1
                        else:
                            return False
            elif flag == 1:
                if nums[idx] > nums[idx + 1]:
                    count += 1
                else:
                    if count == 0:
                        return False
                    else:
                        flag = 2
            idx += 1

        # post-process
        return True if flag == 2 else False


nums = [1,3,5,4,2,6]
nums = [2,1,3]
nums = [1,2,3,2,1]
nums = [1,2,3,2,1,2,3]
nums = [1,2,3,2,1,2,3,3]
nums = [2,4,3,3]

solution = Solution()
print(solution.isTrionic(nums))
