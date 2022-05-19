class Solution(object):
    def minimumJumps(self, forbidden, a, b, x):
        """
        :type forbidden: List[int]
        :type a: int
        :type b: int
        :type x: int
        :rtype: int
        """
        L = 6000
        if x == 0:
            return 0

        # bfs(0, 0) - (current position, jump direction), -1 jump backward, 1 jump forward
        from collections import deque
        bfs = deque()
        bfs.append((0, 0, 1))
        visited = set()
        visited.add((0, 0))
        while bfs:
            curr, direction, steps = bfs.popleft()
            # jump forward

            new = curr + a
            if 0 <= new <= L:
                if new not in forbidden:
                    if (new, 1) not in visited:
                        if new == x:
                            return steps
                        bfs.append((new, 1, steps + 1))
                        visited.add((new, 1))

            # jump backward
            if direction != -1:
                new = curr - b
                if 0 <= new <= L:
                    if new not in forbidden:
                        if (new, -1) not in visited:
                            if new == x:
                                return steps
                            bfs.append((new, -1, steps + 1))
                            visited.add((new, -1))
        return -1


forbidden = [14,4,18,1,15]
a = 3
b = 15
x = 9

forbidden = [8,3,16,6,12,20]
a = 15
b = 13
x = 11

forbidden = [1,6,2,14,5,4]
a = 16
b = 9
x = 7

forbidden = [162,118,178,152,167,100,40,74,199,186,26,73,200,127,30,124,193,84,184,36,103,149,153,9,54,154,133,95,45,198,79,157,64,122,59,71,48,177,82,35,14,176,16,108,111,6,168,31,134,164,136,72,98]
a = 29
b = 98
x = 80

solution = Solution()
print(solution.minimumJumps(forbidden, a, b, x))
