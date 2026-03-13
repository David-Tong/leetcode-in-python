class Solution(object):
    def minTime(self, s, order, k):
        """
        :type s: str
        :type order: List[int]
        :type k: int
        :rtype: int
        """
        # pre-process
        L = len(s)

        # helper function
        def count(target):
            mask = ['-'] * L
            idx = 0
            while idx <= target:
                mask[order[idx]] = '*'
                idx += 1

            res = 0
            idx = 0
            stack = 0
            while idx < L:
                if mask[idx] == "*":
                    res += (L - idx) * (stack + 1)
                    stack = 0
                else:
                    stack += 1
                idx += 1
            return res

        # process
        left, right = 0, L - 1
        while left + 1 < right:
            middle = (left + right) // 2
            if count(middle) >= k:
                right = middle
            else:
                left = middle + 1

        if count(left) >= k:
            return left
        elif count(right) >= k:
            return right
        else:
            return -1


s = "abc"
order = [1,0,2]
k = 2

s = "cat"
order = [0,2,1]
k = 6

s = "xy"
order = [0,1]
k = 4

s = "owe"
order = [2,1,0]
k = 4

s = "itk"
order = [2,0,1]
k = 4



solution = Solution()
print(solution.minTime(s, order, k))
