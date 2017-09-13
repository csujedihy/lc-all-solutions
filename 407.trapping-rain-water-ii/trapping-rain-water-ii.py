class Solution(object):
    def trapRainWater(self, heightMap):
        """
        :type heightMap: List[List[int]]
        :rtype: int
        """
        if not heightMap:
            return 0
        h = len(heightMap)
        w = len(heightMap[0])
        ans = 0
        heap = []
        visited = set()
        for j in range(w):
            heapq.heappush(heap, (heightMap[0][j], 0, j))
            heapq.heappush(heap, (heightMap[h - 1][j], h - 1, j))
            visited |= {(0, j), (h - 1, j)}
        for i in range(h):
            heapq.heappush(heap, (heightMap[i][0], i, 0))
            heapq.heappush(heap, (heightMap[i][w - 1], i, w - 1))
            visited |= {(i, 0), (i, w - 1)}
        dirs = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        while heap:
            height, i, j = heapq.heappop(heap)
            for di, dj in dirs:
                ni, nj = i + di, j + dj
                if 0 <= ni < h and 0 <= nj < w and (ni, nj) not in visited:
                    ans += max(0, height - heightMap[ni][nj])
                    heapq.heappush(heap, (max(heightMap[ni][nj], height), ni, nj))
                    visited |= {(ni, nj)}
        return ans
            
        