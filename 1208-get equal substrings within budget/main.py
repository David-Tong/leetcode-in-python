class Solution(object):
    def equalSubstring(self, s, t, maxCost):
        """
        :type s: str
        :type t: str
        :type maxCost: int
        :rtype: int
        """
        # pre-process
        L = len(s)
        costs = list()
        for x in range(L):
            costs.append(abs(ord(s[x]) - ord(t[x])))

        # process, sliding window
        left = 0
        right = 0
        ans = 0
        cost = 0
        while right < L:
            cost += costs[right]
            while left < right and cost > maxCost:
                cost -= costs[left]
                left += 1
            right += 1
            if cost <= maxCost:
                ans = max(ans, right - left)
        return ans


s = "abcd"
t = "bcdf"
maxCost = 3

s = "abcd"
t = "cdef"
maxCost = 3

s = "abcd"
t = "acde"
maxCost = 0

s = "bbcd"
t = "acde"
maxCost = 0

s = "pxezla"
t = "loewbi"
maxCost = 25

solution = Solution()
print(solution.equalSubstring(s, t, maxCost))
