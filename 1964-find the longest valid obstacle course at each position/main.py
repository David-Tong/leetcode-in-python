class Solution(object):
    def longestObstacleCourseAtEachPosition(self, obstacles):
        """
        :type obstacles: List[int]
        :rtype: List[int]
        """
        from bisect import bisect_right

        # dp[x] - the minimal obstacle to make x length course
        dp = list()
        ans = list()
        for obstacle in obstacles:
            idx = bisect_right(dp, obstacle)
            if idx >= len(dp):
                dp.append(obstacle)
            else:
                dp[idx] = obstacle
            ans.append(idx + 1)
        return ans


obstacles = [1,2,3,2]
obstacles = [2,2,1]
obstacles = [3,1,5,6,4,2]
obstacles = [1]
obstacles = [1,2,3,4,5,6]
obstacles = [6,5,4,3,2,1]
obstacles = [5,4,5,7,11,2,3,4,1,2,5,6,9,3,2,1,5,6]

solution = Solution()
print(solution.longestObstacleCourseAtEachPosition(obstacles))
