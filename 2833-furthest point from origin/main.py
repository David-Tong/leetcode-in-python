class Solution(object):
    def furthestDistanceFromOrigin(self, moves):
        """
        :type moves: str
        :rtype: int
        """
        # process
        steps = 0
        blanks = 0
        for move in moves:
            if move == "L":
                steps -= 1
            elif move == "R":
                steps += 1
            else:
                blanks += 1
        steps = abs(steps)
        ans = steps + blanks
        return ans


moves = "L_RL__R"

solution = Solution()
print(solution.furthestDistanceFromOrigin(moves))
