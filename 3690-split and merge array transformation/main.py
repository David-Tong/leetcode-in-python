class Solution(object):
    def minSplitMerge(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        # pre-process
        # helper function
        # map numbers to characters
        # example: [1,1,2,3] -> "AABC"
        def map_to_chars(arr, mapping):
            return "".join(mapping[x] for x in arr)

        # build mapping from numbers to characters
        distinct = []
        for x in nums1 + nums2:
            if x not in distinct:
                distinct.append(x)

        mapping = {}
        for i, x in enumerate(distinct):
            mapping[x] = chr(ord('A') + i)

        # convert nums1 and nums2 to character strings
        start = map_to_chars(nums1, mapping)
        target = map_to_chars(nums2, mapping)

        # helper function
        # generate all moves
        def generate_moves(s):
            # generate all strings reachable by one split-and-merge
            n = len(s)
            results = []
            for L in range(n):
                for R in range(L, n):
                    removed = s[L:R + 1]
                    remain = s[:L] + s[R + 1:]
                    # insert removed at all positions
                    for pos in range(len(remain) + 1):
                        new_s = remain[:pos] + removed + remain[pos:]
                        if new_s != s:
                            results.append(new_s)
            return results

        # process
        # bfs
        if start == target:
            return 0

        from collections import deque
        bfs = deque()
        bfs.append((start, 0))
        visited = set([start])

        while bfs:
            cur, steps = bfs.popleft()
            for nxt in generate_moves(cur):
                if nxt == target:
                    return steps + 1
                if nxt not in visited:
                    visited.add(nxt)
                    bfs.append((nxt, steps + 1))

        return -1


nums1 = [3,1,2]
nums2 = [1,2,3]

"""
nums1 = [1,1,2,3,4,5]
nums2 = [5,4,3,2,1,1]

nums1 = [85,-87,24,-87,13]
nums2 = [85,-87,-87,24,13]
"""

solution = Solution()
print(solution.minSplitMerge(nums1, nums2))
