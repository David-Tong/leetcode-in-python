class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        self.DIRECTIONS = ((-1, 0), (1, 0), (0, -1), (0, 1))
        self.visited = []
        self.ans = False

        def dfs(i, j, board, word):
                if board[i][j] == word[0]:
                    if len(word) == 1:
                        return True
                    else:
                        for direction in self.DIRECTIONS:
                            new_i = i + direction[0]
                            new_j = j + direction[1]
                            if new_i >= 0 and new_i < len(board) and new_j >= 0 and new_j < len(board[0]):
                                if (new_i, new_j) not in self.visited:
                                    self.visited.append((new_i, new_j))
                                    if dfs(new_i, new_j, board, word[1:]):
                                        return True
                                    self.visited.pop()
                return False

        for x in range(len(board)):
            for y in range(len(board[0])):
                if board[x][y] == word[0]:
                    self.visited.append((x, y))
                    if dfs(x, y, board, word):
                        return True
                    self.visited.pop()
        return False


board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"

board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
#word = "ABCB"
word = "SEE"

#board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
#word = "ABCB"

board = [["a", "a"]]
word = "aaa"

board = [["C","A","A"],["A","A","A"],["B","C","D"]]
word = "AAB"

borad = [["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","B"],["A","A","A","A","B","A"]]
word = "AAAAAAAAAAAAABB"

#board = [["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]]
#word = "ABCESEEEFS"

solution = Solution()
print(solution.exist(board, word))
