class Solution(object):
    def maxSumOfThreeSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # pre-process
        L = len(nums)
        presums = [0]
        for num in nums:
            presums.append(presums[-1] + num)
        # print(nums)
        # print(presums)

        # process
        # three-pass : stars and bars
        # {x x x x} x x x {x x x x x}
        #       i-1 i      i+k

        # left_maxes, left_idxes
        left_maxes = [0] * L
        left_idxes = [-1] * L
        left_max = 0
        for x in range(k - 1, L):
            left_total = presums[x + 1] - presums[x + 1 - k]
            if left_total > left_max:
                left_maxes[x] = left_total
                left_idxes[x] = x + 1 - k
                left_max = left_total
            else:
                left_maxes[x] = left_maxes[x - 1]
                left_idxes[x] = left_idxes[x - 1]
        # print(left_maxes)
        # print(left_idxes)

        # right maxes, right idxes
        right_maxes = [0] * L
        right_idxes = [-1] * L
        right_max = 0
        for x in range(L - k, -1, -1):
            right_total = presums[x + k] - presums[x]
            if right_total >= right_max:
                right_maxes[x] = right_total
                right_idxes[x] = x
                right_max = right_total
            else:
                right_maxes[x] = right_maxes[x + 1]
                right_idxes[x] = right_idxes[x + 1]
        # print(right_maxes)
        # print(right_idxes)

        # search middle
        ans = None
        maxi = 0
        print("**", k, L - 2 * k + 1)
        for x in range(k, L - 2 * k + 1):
            middle_total = presums[x + k] - presums[x]
            total = middle_total + left_maxes[x - 1] + right_maxes[x + k]
            # print(x, middle_total)
            if total > maxi:
                maxi = total
                ans = (left_idxes[x - 1], x, right_idxes[x + k])
        return ans


nums = [1,2,1,2,6,7,5,1]
k = 2

nums = [1,2,1,2,1,2,1,2,1]
k = 2

nums = [7,13,20,19,19,2,10,1,1,19]
k = 3

solution = Solution()
print(solution.maxSumOfThreeSubarrays(nums, k))
