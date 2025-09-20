class Solution(object):
    def printVertically(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        # pre-process
        words = s.split()
        L = max(map(lambda word: len(word), words))
        containers = [list() for _ in range(L)]

        # process
        idx = 0
        while idx < L:
            for word in words:
                if idx < len(word):
                    containers[idx].append(word[idx])
                else:
                    containers[idx].append(" ")
            idx += 1

        ans = list()
        for container in containers:
            ans.append("".join(container).rstrip())
        return ans


s = "HOW ARE YOU"
s = "TO BE OR NOT TO BE"
# s = "CONTEST IS COMING"

solution = Solution()
print(solution.printVertically(s))
