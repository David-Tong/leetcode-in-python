class Solution(object):
    def longestPath(self, parent, s):
        """
        :type parent: List[int]
        :type s: str
        :rtype: int
        """
        N = len(parent)

        from collections import defaultdict
        tree = defaultdict(list)
        for idx, node in enumerate(parent):
            if node != -1:
                tree[idx].append(node)
                tree[node].append(idx)

        visited = [False] * N
        visited[0] = True

        # up_path - max the path go through and up the vertex
        # end_path - max the path will not go up the vertex
        def doPath(vertex):
            from collections import defaultdict
            sub_up_paths = defaultdict(int)
            sub_end_paths = defaultdict(int)

            for node in tree[vertex]:
                if not visited[node]:
                    visited[node] = True
                    sub_up_path, sub_end_path = doPath(node)
                    sub_up_paths[node] = sub_up_path
                    sub_end_paths[node] = sub_end_path

            # get up path
            from heapq import heapify, heappush, heappop
            heap = list()
            heapify(heap)

            up_path = 1
            for node in sub_up_paths:
                if s[node] != s[vertex]:
                    up_path = max(up_path, sub_up_paths[node] + 1)
                    heappush(heap, sub_up_paths[node] * -1)

            # get end path
            heap_up_path = [0] * 2
            idx = 0
            while heap and idx < 2:
                heap_up_path[idx] = heappop(heap) * -1
                idx += 1
            end_path = heap_up_path[0] + heap_up_path[1] + 1

            for node in sub_end_paths:
                end_path = max(end_path, sub_end_paths[node])

            return up_path, end_path

        up_path, end_path = doPath(0)
        ans = max(up_path, end_path)
        return ans


parent = [-1,0,0,1,1,2]
s = "abacbe"

parent = [-1,0,0,0]
s = "aabc"

parent = [-1,137,65,60,73,138,81,17,45,163,145,99,29,162,19,20,132,132,13,60,21,18,155,65,13,163,125,102,96,60,50,101,100,86,162,42,162,94,21,56,45,56,13,23,101,76,57,89,4,161,16,139,29,60,44,127,19,68,71,55,13,36,148,129,75,41,107,91,52,42,93,85,125,89,132,13,141,21,152,21,79,160,130,103,46,65,71,33,129,0,19,148,65,125,41,38,104,115,130,164,138,108,65,31,13,60,29,116,26,58,118,10,138,14,28,91,60,47,2,149,99,28,154,71,96,60,106,79,129,83,42,102,34,41,55,31,154,26,34,127,42,133,113,125,113,13,54,132,13,56,13,42,102,135,130,75,25,80,159,39,29,41,89,85,19]
s = "ajunvefrdrpgxltugqqrwisyfwwtldxjgaxsbbkhvuqeoigqssefoyngykgtthpzvsxgxrqedntvsjcpdnupvqtroxmbpsdwoswxfarnixkvcimzgvrevxnxtkkovwxcjmtgqrrsqyshxbfxptuvqrytctujnzzydhpal"

solution = Solution()
print(solution.longestPath(parent, s))
