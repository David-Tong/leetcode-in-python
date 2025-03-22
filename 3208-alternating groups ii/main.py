from symbol import and_expr


class Solution(object):
    def numberOfAlternatingGroups(self, colors, k):
        """
        :type colors: List[int]
        :type k: int
        :rtype: int
        """
        # pre-process
        L = len(colors)
        evens = [0]
        odds = [0]
        for idx, color in enumerate(colors):
            if idx % 2 == 0:
                evens.append(evens[-1] + color)
                odds.append(odds[-1])
            else:
                evens.append(evens[-1])
                odds.append(odds[-1] + color)

        # print(evens)
        # print(odds)

        # process
        def isAlternating(idx, l):
            if idx + l > L:
                raise RuntimeError

            if idx % 2 == 0 and colors[idx] == 0:
                if evens[idx + l] - evens[idx] == 0 and \
                    odds[idx + l] - odds[idx] == l // 2:
                    return True
            elif idx % 2 == 1 and colors[idx] == 1:
                if evens[idx + l] - evens[idx] == 0:
                    if l % 2 == 0 and odds[idx + l] - odds[idx] == l // 2:
                        return True
                    elif l % 2 == 1 and odds[idx + l] - odds[idx] == l // 2 + 1:
                        return True
            elif idx % 2 == 1 and colors[idx] == 0:
                if odds[idx + l] - odds[idx] == 0 and \
                    evens[idx + l] - evens[idx] == l // 2:
                    return True
            elif idx % 2 == 0 and colors[idx] == 1:
                if odds[idx + l] - odds[idx] == 0:
                    if l % 2 == 0 and evens[idx + l] - evens[idx] == l // 2:
                        return True
                    if l % 2 == 1 and evens[idx + l] - evens[idx] == l // 2 + 1:
                        return True
            return False

        def checkAlternating(idx):
            if idx + k <= L:
                return isAlternating(idx, k)
            else:
                return isAlternating(idx, L - idx) and isAlternating(0, k + idx - L) and \
                    colors[-1] != colors[0]

        ans = 0
        for idx, color in enumerate(colors):
            if checkAlternating(idx):
                print(idx)
                ans += 1
        return ans


colors = [0,1,0,1,0]
k = 3

colors = [0,1,0,0,1,0,1]
k = 6

colors = [1,1,0,1]
k = 4

colors = [1,0,0]
k = 3

solution = Solution()
print(solution.numberOfAlternatingGroups(colors, k))
