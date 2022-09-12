class Solution(object):
    def minDeletions(self, s):
        """
        :type s: str
        :rtype: int
        """
        from collections import defaultdict
        frequencies = defaultdict(int)
        for ch in s:
            frequencies[ch] += 1

        from heapq import heapify, heappush, heappop
        heap = list(frequencies.values())
        heapify(heap)

        counts = set()
        ans = 0
        while heap:
            count = heappop(heap)
            if count not in counts or count == 0:
                counts.add(count)
            else:
                count -= 1
                ans += 1
                heappush(heap, count)
        return ans


s = "aab"
s = "aaabbbcc"
s = "ceabaacb"
s = "z"
s = "bbcebab"

solution = Solution()
print(solution.minDeletions(s))
