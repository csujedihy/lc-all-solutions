class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: List[str]
        """
        res = []
        if not self.checkWordBreak(s, wordDict):
            return res
        queue = [(0, "")]
        slen = len(s)
        lenList = [l for l in set(map(len, wordDict))]
        while queue:
            tmpqueue = []
            for q in queue:
                start, path = q
                for l in lenList:
                    if start + l <= slen and s[start:start+l] in wordDict:
                        newnode = (start + l, path + " " + s[start:start+l] if path else s[start:start+l])
                        tmpqueue.append(newnode)
                        if start + l == slen:
                            res.append(newnode[1])
            queue, tmpqueue = tmpqueue, []
        return res

    def checkWordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """
        queue = [0]
        slen = len(s)
        lenList = [l for l in set(map(len,wordDict))]
        visited = [0 for _ in range(0, slen + 1)]
        while queue:
            tmpqueue = []
            for start in queue:
                for l in lenList:
                    if s[start:start+l] in wordDict:
                        if start + l == slen:
                            return True
                        if visited[start + l] == 0:
                            tmpqueue.append(start+l)
                            visited[start + l] = 1
            queue, tmpqueue = tmpqueue, []
        return False