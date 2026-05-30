class Solution(object):
    def minDeletion(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        # pre-process
        from collections import defaultdict
        dicts = defaultdict(int)
        for ch in s:
            dicts[ch] += 1

        from heapq import heapify, heappush, heappop
        heap = list()
        heapify(heap)
        for ch in dicts:
            heappush(heap, (dicts[ch], ch))

        # process
        ans = 0
        while len(heap) > k:
            deletion, _ = heappop(heap)
            ans += deletion
        return ans


s = "abc"
k = 2

s = "aabb"
k = 2

s = "yyyzz"
k = 1

solution = Solution()
print(solution.minDeletion(s, k))
