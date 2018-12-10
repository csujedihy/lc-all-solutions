class Solution(object):
  def findWords(self, words):
    """
    :type words: List[str]
    :rtype: List[str]
    """
    ans = []
    d = {}
    row1 = "qwertyuiop"
    row2 = "asdfghjkl"
    row3 = "zxcvbnm"
    for r in row1:
      d[r] = 1.0
    for r in row2:
      d[r] = 2.0
    for r in row3:
      d[r] = 3.0

    for word in words:
      same = True
      pre = d[word[0].lower()]
      for c in word:
        if pre != d[c.lower()]:
          same = False
          break
        pre = d[c.lower()]
      if same:
        ans.append(word)
    return ans
