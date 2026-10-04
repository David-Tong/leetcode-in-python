class Solution(object):
    def maximumWeight(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[int]
        """
        # pre-process
        L = len(intervals)
        intervals = sorted([(left, right, weight, idx)
                            for idx, (left,right,weight) in enumerate(intervals)],
                           key=lambda x: (x[1], x[0]))
        ends = [intervals[x][1] for x in range(L)]

        # process
        # dp init
        # dp[x][y] - maximum score of y non-overlapping intervals for new intervals[:x+1]
        dp = [[float('-inf')] * 5 for _ in range(L)]
        # best[x][y] - record lexicographically smallest information
        best = [[[] for _ in range(5)] for _ in range(L)]

        dp[0][0] = 0
        best[0][0] = []
        dp[0][1] = intervals[0][2]
        best[0][1] = [intervals[0][3]]

        for y in range(2, 5):
            dp[0][y] = float('-inf')
            best[0][y] = []

        # dp transfer
        from bisect import bisect_left
        for x in range(1, L):
            left, right, weight, idx = intervals[x]
            z = bisect_left(ends, left) - 1

            for y in range(5):
                # case 1: not pick x
                dp[x][y] = dp[x - 1][y]
                best[x][y] = best[x - 1][y]

                # case 2: pick x
                if y > 0:
                    if z >= 0 and dp[z][y - 1] != float('-inf'):
                        candidate_score = dp[z][y - 1] + weight
                        candidate_list = best[z][y - 1] + [idx]
                    elif z == -1 and y == 1:
                        candidate_score = weight
                        candidate_list = [idx]
                    else:
                        continue

                    if candidate_score > dp[x][y]:
                        dp[x][y] = candidate_score
                        best[x][y] = candidate_list
                    elif candidate_score == dp[x][y]:
                        if candidate_list < best[x][y]:
                            best[x][y] = candidate_list

        # post-process
        # find best score first
        # then choose the smallest y (1..4) that achieves best_score
        best_score = max(dp[L - 1][1:5])
        best_list_final = list()
        first_idx = float('inf')
        for y in range(1, 5):
            if dp[L - 1][y] == best_score:
                sorted_best_list = sorted(best[L - 1][y])
                if sorted_best_list[0] < first_idx:
                    first_idx = best[L - 1][y][0]
                    best_list_final = sorted_best_list
        ans = best_list_final
        return ans


intervals = [[1,3,2],[4,5,2],[1,5,5],[6,9,3],[6,7,1],[8,9,1]]
intervals = [[5,8,1],[6,7,7],[4,7,3],[9,10,6],[7,8,2],[11,14,3],[3,5,5]]
intervals = [[4,4,1],[2,5,3],[2,3,2]]
# intervals = [[16,22,26],[7,13,7],[6,22,46],[1,10,1],[14,21,13],[9,9,18],[13,24,28]]

solution = Solution()
print(solution.maximumWeight(intervals))
