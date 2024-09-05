class Solution(object):
    def restoreArray(self, adjacentPairs):
        """
        :type adjacentPairs: List[List[int]]
        :rtype: List[int]
        """
        from collections import defaultdict
        dicts = defaultdict(list)

        for pair in adjacentPairs:
            dicts[pair[0]].append(pair[1])
            dicts[pair[1]].append(pair[0])

        start = float("inf")
        end = float("-inf")
        for key in dicts:
            if len(dicts[key]) == 1:
                start = min(start, key)
                end = max(end, key)


        visited = defaultdict(bool)

        ans = [start]
        curr = start
        visited[curr] = True
        while curr != end:
            for nxt in dicts[curr]:
                if not visited[nxt]:
                    visited[nxt] = True
                    ans.append(nxt)
                    curr = nxt
                    break
        return ans


adjacentPairs = [[2,1],[3,4],[3,2]]

solution = Solution()
print(solution.restoreArray(adjacentPairs))
