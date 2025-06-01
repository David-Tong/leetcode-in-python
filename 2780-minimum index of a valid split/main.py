class Solution(object):
    def minimumIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # pre-process
        # get dominant element
        L = len(nums)
        middle = L // 2
        dominant = sorted(nums)[middle]

        dominant_counts = [0] * L
        for x in range(L):
            if nums[x] == dominant:
                if x == 0:
                    dominant_counts[x] = 1
                else:
                    dominant_counts[x] += dominant_counts[x - 1] + 1
            else:
                if x == 0:
                    dominant_counts[x] = 0
                else:
                    dominant_counts[x] += dominant_counts[x - 1]

        # process
        for x in range(L):
            if dominant_counts[x] > (x + 1) // 2 and \
                dominant_counts[-1] - dominant_counts[x] > (L - x - 1) // 2:
                return x
        return -1


nums = [1,2,2,2]
nums = [2,1,3,1,1,1,7,1,2,1]
nums = [3,3,3,3,7,2,2]

solution = Solution()
print(solution.minimumIndex(nums))
