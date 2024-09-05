class Solution(object):
    def buddyStrings(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        L = len(s)

        # pre-process
        from collections import Counter
        counter_s = Counter(s)
        counter_goal = Counter(goal)

        moreTwo = False
        for key in counter_s:
            if counter_s[key] != counter_goal[key]:
                return False
            else:
                if counter_s[key] > 1:
                    moreTwo = True

        diff = 0
        for idx in range(L):
            if s[idx] != goal[idx]:
                diff += 1

        if diff == 0:
            if moreTwo:
                return True
            else:
                return False
        elif diff == 2:
            return True
        else:
            return False


s = "ab"
goal = "ba"

s = "ab"
goal = "ab"

s = "aa"
goal = "aa"

solution = Solution()
print(solution.buddyStrings(s, goal))