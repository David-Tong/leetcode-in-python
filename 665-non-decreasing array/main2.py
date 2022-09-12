class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        L = len(nums)
        stack = list()
        count = 0
        for idx, num in enumerate(nums):
            if stack and stack[-1] > num:
                if idx < L - 1 and stack[-1] > nums[idx + 1]:
                    # modify previous
                    previous_largers = 0
                    while stack and stack[-1] > num:
                        previous_largers += 1
                        stack.pop()
                    if previous_largers > 1:
                        return False
                    count += 1
                # modify current and make it larger than all previous
                else:
                    count += 1
                    if idx < L - 1:
                        num = nums[idx + 1]
            stack.append(num)

        if count > 1:
            return False
        else:
            return True


nums = [4,2,3]
nums = [4,2,1]
nums = [3,4,2,3]
nums = [1]
nums = [5,7,1,8]

solution = Solution()
print(solution.checkPossibility(nums))
