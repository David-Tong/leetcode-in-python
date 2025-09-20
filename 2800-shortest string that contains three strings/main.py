class Solution(object):
    def minimumString(self, a, b, c):
        """
        :type a: str
        :type b: str
        :type c: str
        :rtype: str
        """
        # pre-process
        # helper function
        # overlap
        def overlap3(s1, s2, s3):
            return overlap2(overlap2(s1, s2), s3)

        def overlap2(s1, s2):
            # conner case
            if s2 in s1:
                return s1
            L1, L2 = len(s1), len(s2)
            anchor = s2[0]
            anchors = list()
            for idx, ch in enumerate(s1):
                if ch == anchor:
                    anchors.append(idx)
            for anchor in anchors:
                idx = 0
                while anchor + idx < L1 and idx < L2:
                    if s1[anchor + idx] != s2[idx]:
                        break
                    idx += 1
                if anchor + idx == L1:
                    return s1[:anchor] + s2
            return s1 + s2

        # print(overlap3(a, b, c))

        # process
        ARRANGEMENTS = ((a, b, c), (a, c, b), (b, a, c), (b, c, a), (c, a, b), (c, b, a))

        mini = float("inf")
        ans = ""
        for arrangement in ARRANGEMENTS:
            s = overlap3(*arrangement)
            # print(arrangement, s)
            if len(s) < mini:
                mini = len(s)
                ans = s
            elif len(s) == mini:
                if s < ans:
                    ans = s
        return ans


a = "abc"
b = "bca"
c = "aaa"

a = "ca"
b = "a"
c = "a"

a = "ab"
b = "a"
c = "c"

solution = Solution()
print(solution.minimumString(a, b, c))
