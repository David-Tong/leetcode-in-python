class Solution(object):
    def constructDistancedSequence(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        # pre-process
        from copy import deepcopy

        L = 2 * n - 1
        self.ans = ""

        def doConstruct(idx, sequence):
            if idx == L:
                self.ans = sequence
                return True

            if sequence[idx] != "":
                return doConstruct(idx + 1, sequence)
            else:
                x = n
                while x > 0:
                    if x not in set(sequence):
                        next_sequence = deepcopy(sequence)
                        next_sequence[idx] = x

                        go = False
                        if x == 1:
                            go = True
                        else:
                            if idx + x < L and next_sequence[idx + x] == "":
                                next_sequence[idx + x] = x
                                go = True
                        if go:
                            if doConstruct(idx + 1, next_sequence):
                                return True
                    x -= 1
                return False

        sequence = [""] * L
        doConstruct(0, sequence)
        return self.ans


n = 3
n = 5
n = 1
n = 10
n = 20

solution = Solution()
print(solution.constructDistancedSequence(n))

