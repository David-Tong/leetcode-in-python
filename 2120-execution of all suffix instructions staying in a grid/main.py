class Solution(object):
    def executeInstructions(self, n, startPos, s):
        """
        :type n: int
        :type startPos: List[int]
        :type s: str
        :rtype: List[int]
        """
        DIRECTIONS = {"L": (0, -1), "R": (0, 1), "U": (-1, 0), "D": (1, 0)}
        L = len(s)
        ans = list()
        for u in range(L):
            x, y = startPos
            steps = 0
            for v in range(u, L):
                dx, dy = DIRECTIONS[s[v]]
                x, y = x + dx, y + dy
                if 0 <= x < n and 0 <= y < n:
                    steps += 1
                else:
                    break
            ans.append(steps)
        return ans


n = 3
startPos = [0,1]
s = "RRDDLU"

n = 2
startPos = [1, 1]
s = "LURD"

n = 1
startPos = [0,0]
s = "LRUD"

solution = Solution()
print(solution.executeInstructions(n, startPos, s))
