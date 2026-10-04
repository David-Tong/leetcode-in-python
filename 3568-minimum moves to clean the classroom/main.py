class Solution(object):
    def minMoves(self, classroom, energy):
        """
        :type classroom: List[str]
        :type energy: int
        :rtype: int
        """
        # pre-process
        M = len(classroom)
        N = len(classroom[0])
        DIRECTIONS = ((-1, 0),(1, 0), (0, -1), (0, 1))

        # search the map
        start = (-1, -1)
        litter_positions = []
        for x in range(M):
            for y in range(N):
                if classroom[x][y] == 'S':
                    start = (x, y)
                elif classroom[x][y] == 'L':
                    litter_positions.append((x, y))

        if start == (-1, -1):
            return -1
        if not litter_positions:
            return 0

        # setup bitmask index
        litter_index = {}
        for i, (lx, ly) in enumerate(litter_positions):
            litter_index[(lx, ly)] = i

        # initialize
        full_mask = (1 << len(litter_positions)) - 1

        # process
        from collections import deque
        bfs = deque()
        bfs.append((start, energy, full_mask))
        from collections import defaultdict
        visited = defaultdict(int)
        visited[(start[0], start[1], full_mask)] = energy

        steps = 1
        while bfs:
            size = len(bfs)
            for _ in range(size):
                (x, y), e, mask = bfs.popleft()
                # print(x, y, e, mask)

                # stop search when energy is zero or less
                if e <= 0:
                    continue

                # search
                for dx, dy in DIRECTIONS:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < M and 0 <= ny < N:
                        # obstacle grid
                        if classroom[nx][ny] == 'X':
                            continue

                        ne = e - 1
                        new_mask = mask

                        #  litter grid
                        if classroom[nx][ny] == 'L':
                            idx = litter_index[(nx, ny)]
                            # not cleaned yet
                            if (mask >> idx) & 1:
                                new_mask = mask & ~(1 << idx)

                        # refill grid
                        elif classroom[nx][ny] == 'R':
                            ne = energy

                        # check end condition
                        if new_mask == 0:
                            return steps

                        # move forward
                        state = (nx, ny, new_mask)
                        if state not in visited or visited[state] < ne:
                            visited[state] = ne
                            bfs.append(((nx, ny), ne, new_mask))
            steps += 1

        return -1


classroom = ["S.", "XL"]
energy = 2

classroom = ["LS", "RL"]
energy = 4

classroom = ["L.S", "RXL"]
energy = 3

solution = Solution()
print(solution.minMoves(classroom, energy))
