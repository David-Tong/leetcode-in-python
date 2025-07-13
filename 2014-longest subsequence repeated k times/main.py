class Solution(object):
    def longestSubsequenceRepeatedK(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        # pre-process
        # helper function
        # check - check if we have ss repeated k times in s
        def check(ss):
            M, N = len(s), len(ss)
            idx, idx2 = 0, 0
            repeat = 0
            while idx < M:
                if s[idx] == ss[idx2]:
                    idx2 += 1
                    if idx2 == N:
                        idx2 = 0
                        repeat += 1
                    if repeat >= k:
                        return True
                idx += 1
            return repeat >= k

        # process
        # use bfs to generate possible subsequence
        from collections import Counter
        counter = Counter(s)
        candidates = [c for c in counter if counter[c] >= k]
        candidates = sorted(candidates)

        # bfs
        from collections import deque
        bfs = deque()
        bfs.append("")
        ans = ""
        while bfs:
            curr = bfs.popleft()
            for c in candidates:
                nxt = curr + c
                if check(nxt):
                    bfs.append(nxt)
                    ans = nxt
        return ans


s = "letsleetcode"
k = 2

s = "bb"
k = 2

s = "ab"
k = 2

solution = Solution()
print(solution.longestSubsequenceRepeatedK(s, k))
