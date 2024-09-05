class Solution(object):
    def isPossibleDivide(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        # pre-process
        if len(nums) % k != 0:
            return False

        N = len(nums) // k

        from collections import defaultdict
        dicts = defaultdict(int)

        for num in nums:
            dicts[num] += 1

        # process
        for _ in range(N):
            start = min(dicts.keys())
            for x in range(k):
                if start + x in dicts:
                    dicts[start + x] -= 1
                    if dicts[start + x] == 0:
                        del dicts[start + x]
                else:
                    return False
        return True


nums = [1,2,3,3,4,4,5,6]
k = 4

nums = [3,2,1,2,3,4,3,4,5,9,10,11]
k = 3

nums = [1,2,3,4]
k = 3

solution = Solution()
print(solution.isPossibleDivide(nums, k))
