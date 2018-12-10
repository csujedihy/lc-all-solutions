class Solution(object):
  def palindromePairs(self, words):
    """
    :type words: List[str]
    :rtype: List[List[int]]
    """
    ans = []
    d = {}
    for i, word in enumerate(words):
      d[word] = i

    for i, word in enumerate(words):
      if word == "":
        ans.extend([(i, j) for j in range(len(words)) if i != j and words[j] == words[j][::-1]])
        continue
      for j in range(len(word)):
        left = word[:j]
        right = word[j:]
        if right == right[::-1] and left[::-1] in d and d[left[::-1]] != i:
          ans.append((i, d[left[::-1]]))
        if left == left[::-1] and right[::-1] in d and d[right[::-1]] != i:
          ans.append((d[right[::-1]], i))
    return ans
