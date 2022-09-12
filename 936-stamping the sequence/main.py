class Solution(object):
    def movesToStamp(self, stamp, target):
        """
        :type stamp: str
        :type target: str
        :rtype: List[int]
        """
        S = len(stamp)
        T = len(target)

        def doStamp(stamp, target, start):
            stamped = 0
            index = 0
            while index < S:
                if target[start + index] == "?":
                    pass
                elif stamp[index] == target[start + index]:
                    stamped += 1
                else:
                    return 0, target
                index += 1

            target = target[:start] + "?" * S + target[start + S:]
            return stamped, target

        l = 0
        seen = set()
        ans = list()
        while l < T:
            found = False
            for index in range(T - S + 1):
                if index in seen:
                    continue

                stamped, target = doStamp(stamp, target, index)

                if stamped > 0:
                    found = True
                    l += stamped
                    seen.add(index)
                    ans.append(index)

            if not found:
                return list()

        return ans[::-1]


stamp = "abc"
target = "ababc"

stamp = "abca"
target = "aabcaca"

solution = Solution()
print(solution.movesToStamp(stamp, target))
