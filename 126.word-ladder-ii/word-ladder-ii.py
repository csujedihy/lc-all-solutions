from collections import deque


class Solution(object):
  def findLadders(self, beginWord, endWord, wordlist):
    """
    :type beginWord: str
    :type endWord: str
    :type wordlist: Set[str]
    :rtype: List[List[int]]
    """

    def getNbrs(src, dest, wordList):
      res = []
      for c in string.ascii_lowercase:
        for i in range(0, len(src)):
          newWord = src[:i] + c + src[i + 1:]
          if newWord == src:
            continue
          if newWord in wordList or newWord == dest:
            yield newWord

    def bfs(beginWord, endWord, wordList):
      distance = {beginWord: 0}
      queue = deque([beginWord])
      length = 0
      while queue:
        length += 1
        for k in range(0, len(queue)):
          top = queue.popleft()
          for nbr in getNbrs(top, endWord, wordList):
            if nbr not in distance:
              distance[nbr] = distance[top] + 1
              queue.append(nbr)
      return distance

    def dfs(beginWord, endWord, wordList, path, res, distance):
      if beginWord == endWord:
        res.append(path + [])
        return

      for nbr in getNbrs(beginWord, endWord, wordList):
        if distance.get(nbr, -2) + 1 == distance[beginWord]:
          path.append(nbr)
          dfs(nbr, endWord, wordList, path, res, distance)
          path.pop()

    res = []
    distance = bfs(endWord, beginWord, wordlist)
    dfs(beginWord, endWord, wordlist, [beginWord], res, distance)
    return res
