class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        step = len(s) // 2
        left = 0
        right = len(s) - 1
        count = 0
        while count < step:
            tmp = s[left + count]
            s[left + count] = s[right - count]
            s[right - count] = tmp
            count += 1
        return s


solution = Solution()
s = ["h", "e", "l", "l", "o"]
s = ["H","a","n","n","a","h"]
s = ["A"]

print(solution.reverseString(s))