class Solution(object):
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        paths = input.split('\n')
        stack = list()

        indent = 0
        ans = 0
        for path in paths:
            try:
                idx = path.rindex('\t') + 1
            except ValueError:
                idx = 0
            if idx < indent:
                while idx < indent:
                    stack.pop()
                    indent -= 1
            stack.append(path[idx:])
            indent += 1

            curr_path = "/".join(stack)
            print(curr_path)
            if "." in curr_path:
                ans = max(ans, len(curr_path))

        return ans


input = "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"
input = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"
input = "a"
input = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext\n\tabcdefghijklimnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz.ext"
input = "file1.txt\nfile2.txt\nlongfile.txt"

solution = Solution()
print(solution.lengthLongestPath(input))
