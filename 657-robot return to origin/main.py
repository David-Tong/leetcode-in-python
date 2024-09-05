class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        from collections import defaultdict
        directions = defaultdict(int)
        for move in moves:
            directions[move] += 1

        if directions['R'] == directions['L']:
            if directions['U'] == directions['D']:
                return True
        return False


moves = "UD"
moves = "LL"

solution = Solution()
print(solution.judgeCircle(moves))
