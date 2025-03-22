class Solution(object):
    def canChange(self, start, target):
        """
        :type start: str
        :type target: str
        :rtype: bool
        """
        # pre-process
        starts, targets = list(), list()
        for idx, ch in enumerate(start):
            if ch != "_":
                starts.append((ch, idx))
        for idx, ch in enumerate(target):
            if ch != "_":
                targets.append((ch, idx))

        # process
        L = len(starts)
        if len(starts) != len(targets):
            return False
        for x in range(L):
            if starts[x][0] == targets[x][0]:
                if starts[x][0] == "L":
                    if starts[x][1] < targets[x][1]:
                        return False
                elif starts[x][0] == "R":
                    if starts[x][1] > targets[x][1]:
                        return False
            else:
                return False
        return True


start = "_L__R__R_"
target = "L______RR"

start = "R_L_"
target = "__LR"

start = "_R"
target = "R_"

start = "_____"
target = "L___R"

solution = Solution()
print(solution.canChange(start, target))
