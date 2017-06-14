from collections import deque
class Solution(object):
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        numbers = "B123456789"
        queue = deque([click])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
        while queue:
            i, j = queue.popleft()
            if board[i][j] == "B":
                continue
            if board[i][j] == "M":
                board[i][j] = "X"
                break
            mineCnt = 0
            nbrs = []
            for di, dj in directions:
                ni, nj = i + di, j + dj
                if 0 <= ni < len(board) and 0 <= nj < len(board[0]) and board[ni][nj] in ["M", "E"]:
                    if board[ni][nj] == "M":
                        mineCnt += 1
                    else:
                        nbrs.append((ni, nj))
            if mineCnt == 0:
                queue.extend(nbrs)
            board[i][j] = numbers[mineCnt]
        return board