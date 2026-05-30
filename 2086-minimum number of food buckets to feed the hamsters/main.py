class Solution(object):
    def minimumBuckets(self, hamsters):
        """
        :type hamsters: str
        :rtype: int
        """
        # pre-process
        # short-cut
        if hamsters == "H" or hamsters == "HH":
            return -1

        L = len(hamsters)
        foods = [False] * L

        # process
        ans = 0
        idx = 0
        while idx < L:
            if hamsters[idx] == 'H':
                # if both sides with hamsters, return -1
                if 0 < idx < L - 1:
                    if hamsters[idx - 1] == 'H' and hamsters[idx + 1] == 'H':
                        return -1
                elif idx == 0:
                    if hamsters[idx + 1] == 'H':
                        return -1
                elif idx == L - 1:
                    if hamsters[idx - 1] == 'H':
                        return -1

                # if no food on the left, and we may place food on the right
                # then place food on the right
                if idx == 0 or not foods[idx - 1]:
                    if idx < L - 1 and hamsters[idx + 1] == '.':
                        foods[idx + 1] = True
                        ans += 1
                    # if we can't place food on the right, then place on the left
                    else:
                        foods[idx - 1] = True
                        ans += 1
            idx += 1
        return ans


hamsters = "H..H"
hamsters = ".H.H."
hamsters = ".HHH."

import random
hamsters = "".join([random.choice("H..................") for _ in range(100)])
print(hamsters)

solution = Solution()
print(solution.minimumBuckets(hamsters))
