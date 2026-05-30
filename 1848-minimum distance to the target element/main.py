class Solution(object):
    def getMinDistance(self, nums, target, start):
        """
        :type nums: List[int]
        :type target: int
        :type start: int
        :rtype: int
        """
        # pre-process
        idxes = list()
        for idx, num in enumerate(nums):
            if num == target:
                idxes.append(idx)
        # print(idxes)

        # process
        from bisect import bisect_left
        idx = bisect_left(idxes, start)
        if 0 < idx < len(idxes):
            ans = min(abs(start - idxes[idx - 1]), abs(start - idxes[idx]))
        elif idx == 0:
            ans = abs(start - idxes[idx])
        else:
            ans = abs(start - idxes[idx - 1])
        return ans


nums = [1,2,3,4,5]
target = 5
start = 3

nums = [1,2,3,4,5]
target = 1
start = 3

nums = [1,1,1,1,1,1,1,1,1,1]
target = 1
start = 9

solution = Solution()
print(solution.getMinDistance(nums, target, start))
