class Solution(object):
    def findStrobogrammatic(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.d = {"0": "0", "1": "1", "6" : "9", "8": "8", "9": "6"}
        def dfs(half, path, res, n):
            if len(path) == half:
                pathStr = "".join(path)
                if half * 2 == n:
                    res.append(pathStr + "".join([self.d[x] for x in pathStr[::-1]]))
                else:
                    for c in "018":
                        res.append(pathStr + c + "".join([self.d[x] for x in pathStr[::-1]]))
                return
            
            for c in "01689":
                if c == "0" and len(path) == 0:
                    continue
                path.append(c)
                dfs(half, path, res, n)
                path.pop()
  
        res = []
        dfs(n/2, [], res, n)
        return res
                