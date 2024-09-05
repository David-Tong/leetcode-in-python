class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        N = len(chars)

        slow = 0
        fast = 1
        index = 0
        while fast < N:
            if chars[slow] != chars[fast]:
                chars[index] = chars[slow]
                index += 1
                if fast - slow > 1:
                    for num in list(str(fast - slow)):
                        chars[index] = num
                        index += 1
                slow = fast
            fast += 1

        chars[index] = chars[slow]
        index += 1

        if fast - slow > 1:
            for num in list(str(fast - slow)):
                chars[index] = num
                index += 1

        return index


chars = ["a","a","b","b","c","c","c"]
chars = ["a"]
chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]

solution = Solution()
print(solution.compress(chars))
print(chars)
