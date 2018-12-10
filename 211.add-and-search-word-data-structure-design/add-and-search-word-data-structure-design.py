class TrieNode:
  def __init__(self):
    self.neighbours = {}
    self.isWord = False


class Trie:
  def __init__(self):
    self.root = TrieNode()

  def addWord(self, word):
    root = self.root
    for i in range(0, len(word)):
      c = word[i]
      if c in root.neighbours:
        root = root.neighbours[c]
      else:
        newnode = TrieNode()
        root.neighbours[c] = newnode
        root = root.neighbours[c]
    root.isWord = True


class WordDictionary:
  def __init__(self):
    self.trie = Trie()
    self.cache = set([])

  def addWord(self, word):
    self.trie.addWord(word)
    self.cache.add(word)

  def search(self, word):
    if word in self.cache:
      return True

    def dfsHelper(root, word, index):
      if not root:
        return False

      if len(word) == index:
        if root.isWord:
          return True
        return False

      if word[index] != ".":
        if dfsHelper(root.neighbours.get(word[index], None), word, index + 1):
          return True
      else:
        for nbr in root.neighbours:
          if dfsHelper(root.neighbours[nbr], word, index + 1):
            return True
      return False

    return dfsHelper(self.trie.root, word, 0)
