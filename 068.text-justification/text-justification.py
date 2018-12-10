class Solution(object):
  def fullJustify(self, words, maxWidth):
    """
    :type words: List[str]
    :type maxWidth: int
    :rtype: List[str]
    """
    ans = []
    line = []
    lens = map(len, words)
    idx = 0
    curLen = 0
    while idx < len(words):
      if curLen == 0:
        curLen = lens[idx]
      else:
        curLen += lens[idx] + 1
      line.append(words[idx])
      idx += 1
      if curLen > maxWidth:
        curLen = 0
        line.pop()
        idx -= 1
        if len(line) == 1:
          ans.append(line[0] + " " * (maxWidth - len(line[0])))
          line = []
          continue
        spaces = maxWidth - sum(map(len, line))
        avgSpace = spaces / (len(line) - 1)
        extraSpace = spaces % (len(line) - 1)
        res = ""
        for i in range(0, len(line)):
          res += line[i]
          if i < len(line) - 1:
            res += " " * (avgSpace + (extraSpace > 0))
            extraSpace -= 1
        ans.append(res)
        line = []
      elif idx == len(words):
        res = ""
        for i in range(0, len(line)):
          res += line[i]
          if i < len(line) - 1:
            res += " "
        res += " " * (maxWidth - len(res))
        ans.append(res)
    return ans
