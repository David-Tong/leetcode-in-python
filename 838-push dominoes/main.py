class Solution(object):
    def pushDominoes(self, dominoes):
        """
        :type dominoes: str
        :rtype: str
        """
        L = len(dominoes)

        from collections import deque
        bfs = deque()
        visited = set()

        ans = ["."] * L
        for idx, dominoe in enumerate(dominoes):
            if dominoe == "R" or dominoe == "L":
                bfs.append((idx, dominoe))
                visited.add(idx)
                ans[idx] = dominoe

        while bfs:
            size = len(bfs)
            from collections import defaultdict
            enque = defaultdict(chr)
            for x in range(size):
                idx, direction = bfs.popleft()
                if direction == "R":
                    if idx < L - 1 and idx + 1 not in visited:
                        if idx + 1 not in enque:
                            enque[idx + 1] = "R"
                        else:
                            del enque[idx + 1]
                elif direction == "L":
                    if idx > 0 and idx - 1 not in visited:
                        if idx - 1 not in enque:
                            enque[idx - 1] = "L"
                        else:
                            del enque[idx - 1]

            for idx in enque:
                bfs.append((idx, enque[idx]))
                visited.add(idx)
                ans[idx] = enque[idx]

        return "".join(ans)


dominoes = "RR.L"
dominoes = ".L.R...LR..L.."
dominoes = "L"
dominoes = ".L.R...LR..L..L"
dominoes = "......R........L"
dominoes = "RLLL..LR....LL......LLR.RL...RRL..........R..L....RR.R..L.LR.L...L..LL.R.R.L.RR.....LRL.L.LL..LRR.L."

solution = Solution()
print(solution.pushDominoes(dominoes))
