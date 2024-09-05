class Solution(object):
    def countOfPairs(self, n, x, y):
        """
        :type n: int
        :type x: int
        :type y: int
        :rtype: List[int]
        """
        ans = [0] * n

        for node in range(n):
            from collections import deque
            bfs = deque()
            bfs.append(node)
            visited = [False] * n
            visited[node] = True

            step = 0
            while bfs:
                for _ in range(len(bfs)):
                    curr = bfs.popleft()
                    if curr > 0 and not visited[curr - 1]:
                        bfs.append(curr - 1)
                        visited[curr - 1] = True
                        ans[step] += 1
                    if curr < n - 1 and not visited[curr + 1]:
                        bfs.append(curr + 1)
                        visited[curr + 1] = True
                        ans[step] += 1
                    if curr == x - 1 and not visited[y - 1]:
                        bfs.append(y - 1)
                        visited[y - 1] = True
                        ans[step] += 1
                    if curr == y - 1 and not visited[x - 1]:
                        bfs.append(x - 1)
                        visited[x - 1] = True
                        ans[step] += 1
                step += 1

        return ans


n = 3
x = 1
y = 3

n = 5
x = 2
y = 4

n = 4
x = 1
y = 1

solution = Solution()
print(solution.countOfPairs(n, x, y))
