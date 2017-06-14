class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        d = {}
        s3 = list(s3)
        if len(s1) + len(s2) != len(s3):
            return False
        def dfs(s1, i, s2, j, d, path, s3):
            if (i, j) in d:
                return d[(i, j)]
            
            if path == s3:
                return True
            
            if i < len(s1):
                if s3[i + j] == s1[i]:
                    path.append(s1[i])
                    if dfs(s1, i + 1, s2, j, d, path, s3):
                        return True
                    path.pop()
                    d[(i+1, j)] = False
            
            if j < len(s2):
                if s3[i + j] == s2[j]:
                    path.append(s2[j])
                    if dfs(s1, i, s2, j + 1, d, path, s3):
                        return True
                    path.pop()
                    d[(i, j+1)] = False

            
            return False
            
        return dfs(s1, 0, s2, 0, d, [], s3)