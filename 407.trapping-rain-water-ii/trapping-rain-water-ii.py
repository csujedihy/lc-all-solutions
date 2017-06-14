import heapq
class Solution(object):
    def trapRainWater(self, heightMap):
        """
        :type heightMap: List[List[int]]
        :rtype: int
        """
        if len(heightMap) < 2 or len(heightMap[0]) < 2:
            return 0
        heap = []
        mw = len(heightMap[0])
        mh = len(heightMap)
        ans = 0
        dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        visited = [[0] * mw for _ in xrange(0, mh)]
        
        for j in range(0, mw):
            heap.append((heightMap[0][j], (0, j)))
            heap.append((heightMap[mh - 1][j], (mh - 1, j)))
            visited[0][j] = 1
            visited[mh - 1][j] = 1
        for i in range(0, mh):
            heap.append((heightMap[i][0], (i, 0)))
            heap.append((heightMap[i][mw - 1], (i, mw - 1)))
            visited[i][0] = 1
            visited[i][mw - 1] = 1
        heapq.heapify(heap)
        
        while heap:
            h, (i, j) = heapq.heappop(heap)
            for d in dir:
                ni, nj = i + d[0], j + d[1]
                if 0 <= ni < mh and 0 <= nj < mw:
                    if visited[ni][nj] == 0:
                        visited[ni][nj] = 1
                        ans += max(0, h - heightMap[ni][nj])
                        heapq.heappush(heap, (max(h, heightMap[ni][nj]), (ni, nj)))
     
        return ans
                
                
                
                