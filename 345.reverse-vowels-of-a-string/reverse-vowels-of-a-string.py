import string


class Solution(object):
  def reverseVowels(self, s):
    """
    :type s: str
    :rtype: str
    """
    vowels = set(["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"])
    s = list(s)
    start, end = 0, len(s) - 1
    while start < end:
      if s[start] not in vowels:
        start += 1
      elif s[end] not in vowels:
        end -= 1
      else:
        s[start], s[end] = s[end], s[start]
        start += 1
        end -= 1
    return "".join(s)
