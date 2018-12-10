class TrieNode:
  def __init__(self, char):
    self.neighbours = {}
    self.isWord = False


class Trie:
  def __init__(self):
    self.root = TrieNode("-")

  def addWord(self, word):
    root = self.root
    for i in range(0, len(word)):
      c = word[i]
      if c in root.neighbours:
        root = root.neighbours[c]
      else:
        newnode = TrieNode(c)
        root.neighbours[c] = newnode
        root = root.neighbours[c]
    root.isWord = True


class Solution:
  # @param board, a list of lists of 1 length string
  # @param words: A list of string
  # @return: A list of string
  def findWords(self, board, words):
    # write your code here
    trie = Trie()
    res = []
    visited = [[0] * len(board[0]) for i in range(0, len(board))]
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def dfs(i, j, board, visited, res, root, path):
      if not root:
        return

      if root.isWord:
        res.append(path)

      for direction in directions:
        ni, nj = i + direction[0], j + direction[1]
        if 0 <= ni < len(board) and 0 <= nj < len(board[0]):
          c = board[ni][nj]
          if visited[ni][nj] == 0:
            visited[ni][nj] = 1
            dfs(ni, nj, board, visited, res, root.neighbours.get(c, None), path + c)
            visited[ni][nj] = 0

    for word in words:
      trie.addWord(word)
    root = trie.root
    for i in range(0, len(board)):
      for j in range(0, len(board[0])):
        c = board[i][j]
        visited[i][j] = 1
        dfs(i, j, board, visited, res, root.neighbours.get(c, None), c)
        visited[i][j] = 0
    return list(set(res))
