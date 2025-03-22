class Solution(object):
    def rotateString(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        # pre-process
        if len(s) != len(goal):
            return False
        L = len(s)

        # process
        idx = 0
        while idx < L:
            shift = 0
            matched = True
            while shift < L:
                idx2 = (idx + shift) % L
                if s[idx2] != goal[shift]:
                    matched = False
                    break
                shift += 1
            if matched:
                return True
            idx += 1
        return False


s = "abcde"
goal = "cdeab"

s = "abcde"
goal = "abced"

solution = Solution()
print(solution.rotateString(s, goal))
