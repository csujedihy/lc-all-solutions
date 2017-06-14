class Solution(object):
    def findMinStep(self, board, hand):
        """
        :type board: str
        :type hand: str
        :rtype: int
        """

        def dfs(line, balls, visited):
            line = reduceLine(line)
            if (line, balls) in visited:
                return visited[line, balls]
            if len(line) == 0:
                return len(hand) - len(balls)
            if len(balls) == 0:
                return float("inf")
            res = float("inf")
            for i in range(len(balls)):
                for j in range(len(line) + 1):
                    if j == 0 and line[0] != balls[i]:
                            continue
                    elif j == len(line) and line[-1] != balls[i]:
                            continue
                    elif 0 < j < len(line) and balls[i] != line[j - 1] and balls[i] != line[j]:
                            continue
                    res = min(res, dfs(line[:j] + balls[i] + line[j:], balls[:i] + balls[i + 1:], visited))
            visited[line, balls] = res
            return res

        def reduceLine(line):
            def reducer(line):
                if len(line) < 3:
                    return line
                ret = []
                dp = [1] * len(line)
                pre = line[-1]
                count = 1
                for i in reversed(range(len(line) - 1)):
                    if line[i] == pre:
                        count += 1
                    else:
                        pre = line[i]
                        count = 1
                    dp[i] = count
                i = 0

                while i < len(line):
                    if dp[i] >= 3:
                        i += dp[i]
                    else:
                        ret.extend(line[i:i + dp[i]])
                        i += dp[i]
                return "".join(ret)

            if len(line) < 3:
                return line
            ans = line
            for _ in range(len(line) / 3):
                ans = reducer(ans)
            return ans

        visited = {}
        ret = dfs(board, "".join(sorted(hand)), visited)
        return ret if ret != float("inf") else -1