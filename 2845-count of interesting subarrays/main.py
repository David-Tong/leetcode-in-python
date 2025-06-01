from itertools import count


class Solution(object):
    def countInterestingSubarrays(self, nums, modulo, k):
        """
        :type nums: List[int]
        :type modulo: int
        :type k: int
        :rtype: int
        """
        # pre-process
        from collections import defaultdict
        dicts = defaultdict(int)
        dicts[0] = 1

        # process
        # x x x x (x x x)
        #   k1   +   k   =   k2
        count = 0
        ans = 0
        for num in nums:
            if num % modulo == k:
                count += 1
            k2 = count % modulo
            k1 = (k2 - k + modulo) % modulo
            ans += dicts[k1]
            dicts[k2] += 1
        return ans


nums = [3,2,4]
modulo = 2
k = 1

nums = [3,1,9,6]
modulo = 3
k = 0

solution = Solution()
print(solution.countInterestingSubarrays(nums, modulo, k))
