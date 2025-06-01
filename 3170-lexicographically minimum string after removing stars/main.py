class Solution(object):
    def clearStars(self, s):
        """
        :type s: str
        :rtype: str
        """
        # pre-process
        L = len(s)
        from heapq import heapify, heappush, heappop
        heap = list()
        heapify(heap)
        removals = set()
        for idx, ch in enumerate(s):
            if ch != "*":
                heappush(heap, (ch, -idx))
            else:
                _, idx2 = heappop(heap)
                removals.add(-idx2)
                removals.add(idx)

        # process
        ans = ""
        for x in range(L):
            if x not in removals:
                ans += s[x]
        return ans


s = "aaba*"
s = "abc"
s = "abcacaca***"

solution = Solution()
print(solution.clearStars(s))
