class Solution(object):
    def leftmostBuildingQueries(self, heights, queries):
        """
        :type heights: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        # pre-process
        H = len(heights)
        Q = len(queries)
        # ensure a < b
        for x in range(Q):
            if queries[x][0] > queries[x][1]:
                queries[x] = [queries[x][1], queries[x][0]]
        # sort by b descending
        queries_n = [[query, idx] for idx, query in enumerate(queries)]
        queries_n = sorted(queries_n, key=lambda x: x[0][1], reverse=True)

        # process
        # maintain an ordered list
        idx_h = H - 1
        idx_q = 0
        # queue will hold all heights in ascending order
        # queue - [height, idx]
        queue_h = list()
        queue_idx = list()

        ans = [0] * Q
        while idx_h >= 0 and idx_q < Q:
            while idx_h > queries_n[idx_q][0][1]:
                while queue_h and queue_h[0] <= heights[idx_h]:
                    queue_h.pop(0)
                    queue_idx.pop(0)
                queue_h.insert(0, heights[idx_h])
                queue_idx.insert(0, idx_h)
                idx_h -= 1

            # query
            idx_alice = queries_n[idx_q][0][0]
            idx_bob = queries_n[idx_q][0][1]
            idx_ans = queries_n[idx_q][1]
            # shortcut
            if idx_alice == idx_bob or heights[idx_alice] < heights[idx_bob]:
                ans[idx_ans] = idx_bob
            # binary search
            else:
                from bisect import bisect_right
                target = max(heights[idx_alice], heights[idx_bob])
                idx = bisect_right(queue_h, target)
                if idx < len(queue_h):
                    ans[idx_ans] = queue_idx[idx]
                else:
                    ans[idx_ans] = -1
            idx_q += 1

        return ans


heights = [6,4,8,5,2,7]
queries = [[0,1],[0,3],[2,4],[3,4],[2,2]]

heights = [5,3,8,2,6,1,4,6]
queries = [[0,7],[3,5],[5,2],[3,0],[1,6]]

heights = [1,2,1,2,1,2]
queries = [[0,0],[0,1],[0,2],[0,3],[0,4],[0,5],[1,0],[1,1],[1,2],[1,3],[1,4],[1,5],[2,0],[2,1],[2,2],[2,3],[2,4],[2,5],[3,0],[3,1],[3,2],[3,3],[3,4],[3,5],[4,0],[4,1],[4,2],[4,3],[4,4],[4,5],[5,0],[5,1],[5,2],[5,3],[5,4],[5,5]]

solution = Solution()
print(solution.leftmostBuildingQueries(heights, queries))