class Solution(object):
    def maximumScore(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # pre-process
        L = len(nums)

        lefts = list()
        for idx in range(k, -1, -1):
            if not lefts:
                lefts.append([nums[idx], idx])
            else:
                if lefts[-1][0] > nums[idx]:
                    lefts[-1][1] = idx + 1
                    lefts.append([nums[idx], idx])
        lefts[-1][1] = 0
        lefts = lefts[::-1]

        rights = list()
        for idx in range(k, L):
            if not rights:
                rights.append([nums[idx], idx])
            else:
                if rights[-1][0] > nums[idx]:
                    rights[-1][1] = idx - 1
                    rights.append([nums[idx], idx])
        rights[-1][1] = L - 1
        rights = rights[::-1]

        # calculate
        left = 0
        right = 0

        ans = float("-inf")
        while left < len(lefts) and right < len(rights):
            ans = max(ans, min(lefts[left][0], rights[right][0]) * (rights[right][1] - lefts[left][1] + 1))
            if lefts[left][0] <= rights[right][0]:
                left += 1
            else:
                right += 1

        while left < len(lefts):
            ans = max(ans, min(lefts[left][0], rights[right - 1][0]) * (rights[right - 1][1] - lefts[left][1] + 1))
            left += 1

        while right < len(rights):
            ans = max(ans, min(lefts[left - 1][0], rights[right][0]) * (rights[right][1] - lefts[left - 1][1] + 1))
            right += 1

        return ans


nums = [1,4,3,7,4,5]
k = 3

nums = [5,5,4,5,4,1,1,1]
k = 0

nums = [15]
k = 0

nums = [1,2,4,1,2,3,1,5,6,7,8,11,2,12,14,5,1,2,77]
k = 6

solution = Solution()
print(solution.maximumScore(nums, k))
