class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        import string
        N = len(beginWord)

        from collections import deque
        bfs = deque()
        bfs.append((beginWord, list()))
        from collections import defaultdict
        visited = defaultdict(int)
        visited[beginWord] = 1

        levels = 1
        anses = list()
        end_search = False
        while bfs and not end_search:
            levels += 1
            size = len(bfs)
            for x in range(size):
                word, path = bfs.popleft()
                for y in range(N):
                    for ch in string.ascii_lowercase:
                        newWord = word[:y] + ch + word[y+1:]
                        if newWord != word and newWord in wordList:
                            if newWord not in visited or newWord in visited and levels <= visited[newWord]:
                                bfs.append((newWord, path + [word]))
                                visited[newWord] = levels

                            if newWord == endWord:
                                end_search = True
                                anses.append(path + [word, newWord])
        return anses


beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]

beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

#beginWord = "a"
#endWord = "c"
#wordList = ["a","b","c"]

#beginWord = "red"
#endWord = "tax"
#wordList = ["ted","tex","red","tax","tad","den","rex","pee"]

solution = Solution()
print(solution.findLadders(beginWord, endWord, wordList))
