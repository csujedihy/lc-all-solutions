class Solution:
  # @param board, a list of lists of 1 length string
  # @param word, a string
  # @return a boolean
  def exist(self, board, word):
    # write your code here
    if word == "":
      return True
    if len(board) == 0:
      return False
    visited = [[0] * len(board[0]) for i in range(0, len(board))]
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def dfs(i, j, board, visited, word, index):
      if word[index] != board[i][j]:
        return False
      if len(word) - 1 == index:
        return True
      for direction in directions:
        ni, nj = i + direction[0], j + direction[1]
        if ni >= 0 and ni < len(board) and nj >= 0 and nj < len(board[0]):
          if visited[ni][nj] == 0:
            visited[ni][nj] = 1
            if dfs(ni, nj, board, visited, word, index + 1):
              return True
            visited[ni][nj] = 0
      return False

    for i in range(0, len(board)):
      for j in range(0, len(board[0])):
        visited[i][j] = 1
        if dfs(i, j, board, visited, word, 0):
          return True
        visited[i][j] = 0
    return False
