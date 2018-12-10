class Solution(object):
  def wordsTyping(self, sentence, rows, cols):
    """
    :type sentence: List[str]
    :type rows: int
    :type cols: int
    :rtype: int
    """
    s = " ".join(sentence) + " "
    n = len(s)
    start = 0
    for _ in range(rows):
      start += cols - 1
      if s[start % n] == " ":
        start += 1
      elif s[(start + 1) % n] == " ":
        start += 2
      else:
        while start > 0 and s[(start - 1) % n] != " ":
          start -= 1
    return start / n
