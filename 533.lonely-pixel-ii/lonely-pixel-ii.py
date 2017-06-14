class Solution(object):
    def findBlackPixel(self, picture, N):
        """
        :type picture: List[List[str]]
        :type N: int
        :rtype: int
        """
        rowSign = {}
        ans = 0
        col = {}
        row = {}
        for i in range(len(picture)):
            sign = "".join(picture[i])
            rowSign[sign] = rowSign.get(sign, 0) + 1 if sign.count("B") == N else 0
            for j in range(len(picture[0])):
                if picture[i][j] == "B":
                    col[j] = col.get(j, 0) + 1
        for key in rowSign:
            if rowSign[key] == N:
                for j in range(len(key)):
                    if key[j] == "B" and col.get(j, 0) == N:
                        ans += N
        return ans