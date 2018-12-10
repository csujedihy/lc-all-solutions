class Solution:
  # @param s, a list of 1 length strings, e.g., s = ['h','e','l','l','o']
  # @return nothing
  def reverseWords(self, s):
    def swap(start, end, slist):
      while start < end:
        slist[start], slist[end] = slist[end], slist[start]
        start += 1
        end -= 1

    wstart, wend = 0, 0
    for i in range(0, len(s)):
      if s[i] == " ":
        wend = i - 1
        swap(wstart, wend, s)
        wstart = i + 1
      elif i + 1 == len(s):
        swap(wstart, i, s)

    swap(0, len(s) - 1, s)
