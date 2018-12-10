class Solution(object):
  def reverseWords(self, s):
    """
    :type s: str
    :rtype: str
    """
    s = s.split()
    for i, word in enumerate(s):
      s[i] = word[::-1]
    return " ".join(s)
