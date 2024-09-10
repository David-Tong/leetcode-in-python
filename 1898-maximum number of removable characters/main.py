class Solution(object):
    def maximumRemovals(self, s, p, removable):
        """
        :type s: str
        :type p: str
        :type removable: List[int]
        :rtype: int
        """
        def canRemove(k, s, p, removable):
            if k == 0:
                return True

            # make new s
            removals = sorted(removable[:k])
            ns = ""
            for x in range(len(removals)):
                if x == 0:
                    ns = s[:removals[x]]
                else:
                    ns += s[removals[x - 1] + 1:removals[x]]
            ns += s[removals[x] + 1:]

            # check if p is a subsequence of ns
            x, y = 0, 0
            while x < len(ns):
                if ns[x] == p[y]:
                    y += 1
                if y == len(p):
                    return True
                x += 1
            return False

        left = 0
        right = len(removable)

        while left + 1 < right:
            middle = (left + right) // 2
            if canRemove(middle, s, p, removable):
                left = middle
            else:
                right = middle - 1

        if canRemove(right, s, p, removable):
            return right
        else:
            return left


s = "abcacb"
p = "ab"
removable = [3,1,0]

s = "abcbddddd"
p = "abcd"
removable = [3,2,1,4,5,6]

s = "abcab"
p = "abc"
removable = [0,1,2,3,4]

<<<<<<< HEAD
s = "abcabcabc"
p = "abc"
removable = [0,1,2,6,7,8]

solution = Solution()
print(solution.maximumRemovals(s, p, removable))
=======
solution = Solution()
print(solution.maximumRemovals(s, p, removable))
>>>>>>> 8454ad0cbabb9eb52f0445fdebf643388dc21556
