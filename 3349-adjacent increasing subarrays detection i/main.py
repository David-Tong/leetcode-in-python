class Solution(object):
    def hasIncreasingSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        # pre-process
        L = len(nums)
        count = 1
        increasings = list()
        for x in range(1, L):
            if nums[x] > nums[x - 1]:
                count += 1
            else:
                increasings.append(count)
                count = 1
        increasings.append(count)
        # print(increasings)

        # process
        I = len(increasings)
        idx = 0
        while idx < I:
            if idx > 0:
                if increasings[idx] >= k and increasings[idx - 1] >= k:
                    return True
            if increasings[idx] >= 2 * k:
                return True
            idx += 1
        return False


nums = [2,5,7,8,9,2,3,4,3,1]
k = 3

nums = [1,2,3,4,4,4,4,5,6,7]
k = 5

nums = [1,1,2,3,4,5,6,1,2,4]
k = 3

nums = [-15,19]
k = 1

nums = [19,-15]
k = 1

solution = Solution()
print(solution.hasIncreasingSubarrays(nums, k))
