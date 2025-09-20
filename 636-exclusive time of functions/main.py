class Solution(object):
    def exclusiveTime(self, n, logs):
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """
        # process
        stack = list()
        pid, event, t = logs[0].split(":")
        pid, t = int(pid), int(t)
        if event != "start":
            raise Exception
        stack.append(pid)

        pt = t
        ans = [0] * n
        for log in logs[1:]:
            pid, event, t = log.split(":")
            pid, t = int(pid), int(t)
            if event == "start":
                if stack:
                    ans[stack[-1]] += t - pt
                stack.append(pid)
            elif event == "end":
                t += 1
                ans[stack[-1]] += t - pt
                stack.pop()
            pt = t
        return ans


n = 2
logs = ["0:start:0","1:start:2","1:end:5","0:end:6"]

n = 1
logs = ["0:start:0","0:start:2","0:end:5","0:start:6","0:end:6","0:end:7"]

n = 2
logs = ["0:start:0","0:start:2","0:end:5","1:start:6","1:end:6","0:end:7"]

n = 3
logs = ["0:start:0","0:end:0","1:start:1","1:end:1","2:start:2","2:end:2","2:start:3","2:end:3"]

solution = Solution()
print(solution.exclusiveTime(n, logs))
