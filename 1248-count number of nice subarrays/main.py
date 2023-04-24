class Solution(object):
    def numberOfSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def countSubarrys(left, right, left_limit, right_limit):
            if left - 1 == left_limit and right + 1 == right_limit:
                return 1
            elif left - 1 == left_limit:
                return right_limit - right
            elif right - 1 == right_limit:
                return left_limit - left
            else:
                return (left - left_limit) * (right_limit - right)

        odds = list()
        for idx, num in enumerate(nums):
            if num % 2 == 1:
                odds.append(idx)
        L = len(odds)

        ans = 0
        for idx in range(len(odds)):
            if idx + k - 1 >= len(odds):
                break
            else:
                left_limit = odds[idx - 1] if idx > 0 else -1
                right_limit = odds[idx + k] if idx + k < L else len(nums)
                ans += countSubarrys(odds[idx], odds[idx + k - 1], left_limit, right_limit)
        return ans


nums = [1,1,2,1,1]
k = 3

nums = [2,4,6]
k = 1

nums = [2,2,2,1,2,2,1,2,2,2]
k = 2

nums = [1]
k = 1

nums = [2,2,2,1,2,2,1,2,2,2,1,2,2,1,2,2,1,2,1,1,1,2,1]
k = 2

solution = Solution()
print(solution.numberOfSubarrays(nums, k))
