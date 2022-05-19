class Solution(object):
    def canReach(self, arr, start):
        """
        :type arr: List[int]
        :type start: int
        :rtype: bool
        """
        if arr[start] == 0:
            return True

        N = len(arr)
        from collections import deque
        bfs = deque()
        bfs.append(start)
        visited = [0] * N
        visited[start] = 1
        while bfs:
            curr = bfs.popleft()
            for jump in [-1 * arr[curr], arr[curr]]:
                next = curr + jump
                if 0 <= next < N:
                    if visited[next] == 0:
                        bfs.append(next)
                        visited[next] = 1
                        if arr[next] == 0:
                            return True
        return False


arr = [4,2,3,0,3,1,2]
start = 5

arr = [4,2,3,0,3,1,2]
start = 0

arr = [3,0,2,1,2]
start = 2

arr = [4,0,3,0,3,1,2]
start = 5

arr = [0,1]
start = 1

arr = [0,3,0,6,3,3,4]
start = 6

solution = Solution()
print(solution.canReach(arr, start))
