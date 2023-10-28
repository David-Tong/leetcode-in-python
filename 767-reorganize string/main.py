class Solution(object):
    def reorganizeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        from heapq import heapify, heappush, heappop
        heap = list()
        heapify(heap)

        from collections import defaultdict
        dicts = defaultdict(int)
        for ch in s:
            dicts[ch] += 1

        # pre-process
        for ch in dicts:
            heappush(heap, (-1 * dicts[ch], ch))

        ans = ""
        while heap:
            count, ch = heappop(heap)
            if not heap:
                if count < - 1:
                    return ""
                else:
                    ans += ch
                    return ans
            else:
                count2, ch2 = heappop(heap)
                ans += ch + ch2

                if count < -1:
                    heappush(heap, (count + 1, ch))
                if count2 < -1:
                    heappush(heap, (count2 + 1, ch2))
        return ans


s = "aab"
s = "aaab"
s = "aabbbaacccdddddddd"

solution = Solution()
print(solution.reorganizeString(s))
