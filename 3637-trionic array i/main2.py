class Solution(object):
    def isTrionic(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # pre-process
        L = len(nums)
        increasings, decreasings = list(), list()

        idx = 0
        start = 0
        increasing = True
        while idx < L - 1:
            if nums[idx] == nums[idx+1]:
                if increasing:
                    if idx > start:
                        increasings.append((start, idx))
                else:
                    if idx > start:
                        decreasings.append((start, idx))
                start = idx + 1
            elif nums[idx] < nums[idx+1]:
                if not increasing:
                    if idx > start:
                        decreasings.append((start, idx))
                    start = idx
                    increasing = True
            else:
                if increasing:
                    if idx > start:
                        increasings.append((start, idx))
                    start = idx
                    increasing = False
            idx += 1
        if increasing:
            if idx > start:
                increasings.append((start, L - 1))
        else:
            if idx > start:
                decreasings.append((start, L - 1))

        # print(increasings)
        # print(decreasings)

        # process
        if len(increasings) != 2 or len(decreasings) != 1:
            return False

        if increasings[0][1] == decreasings[0][0] and decreasings[0][1] == increasings[1][0]:
            if increasings[0][0] == 0 and increasings[1][1] == L - 1:
                return True
        return False


nums = [1,3,5,4,2,6]
nums = [2,1,3]
nums = [1,2,3,2,1]
nums = [1,2,3,2,1,2,3]
nums = [1,2,3,2,1,2,3,3]
nums = [2,4,3,3]
nums = [1,1,2,3,3,3,2,1,2,2,3]
nums = [2,4,3,3]
nums = [6,5,1]
nums = [3,3,8,1,4,6]

solution = Solution()
print(solution.isTrionic(nums))
