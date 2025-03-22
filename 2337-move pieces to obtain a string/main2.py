class Solution(object):
    def canChange(self, start, target):
        """
        :type start: str
        :type target: str
        :rtype: bool
        """
        # pre-process
        M, N = len(start), len(target)

        # process
        idx, idx2 = 0, 0
        while idx < M:
            if start[idx] != "_":
                while idx2 < N and target[idx2] == "_":
                    idx2 += 1
                if idx2 >= N:
                    return False
                if start[idx] != target[idx2]:
                    return False
                else:
                    if start[idx] == "L" and idx < idx2:
                        return False
                    elif start[idx] == "R" and idx > idx2:
                        return False
                    else:
                        idx2 += 1
            idx += 1

        # post-process
        while idx2 < N:
            if target[idx2] != "_":
                return  False
            idx2 += 1
        return True


start = "_L__R__R_"
target = "L______RR"

start = "R_L_"
target = "__LR"

start = "_R"
target = "R_"

start = "_____"
target = "L___R"

start = "_L__R__R_L"
targret = "L______RR_"

solution = Solution()
print(solution.canChange(start, target))
