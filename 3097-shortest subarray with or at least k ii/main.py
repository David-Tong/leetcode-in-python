class Solution(object):
    def minimumSubarrayLength(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def binarize(num):
            binary = list()
            for x in range(L):
                if num >> x & 1:
                    binary.append(1)
                else:
                    binary.append(0)
            return binary

        def addOrs(total, binary):
            for x in range(L):
                if binary[x] == 1:
                    if ors[x] == 0:
                        total += 2 ** x
                    ors[x] += 1
            return total

        def delOrs(total, binary):
            for x in range(L):
                if binary[x] == 1:
                    ors[x] -= 1
                    if ors[x] == 0:
                        total -= 2 ** x
            return total

        # pre-process
        N = len(nums)
        L = 30
        from collections import defaultdict
        dicts = defaultdict(list)

        # process
        ans = float("inf")
        left, right = 0, 0
        total, ors = 0, [0] * L
        while right < N:
            dicts[right] = binarize(nums[right])
            total = addOrs(total, dicts[right])
            right += 1

            while left < right and total >= k:
                ans = min(ans, right - left)
                total = delOrs(total, dicts[left])
                del dicts[left]
                left += 1

        return -1 if ans == float("inf") else ans


nums = [1,2,3]
k = 2

nums = [2,1,8]
k = 10

nums = [1, 2]
k = 0

solution = Solution()
print(solution.minimumSubarrayLength(nums, k))
