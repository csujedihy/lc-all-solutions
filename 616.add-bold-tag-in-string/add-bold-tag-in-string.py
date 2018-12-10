class Solution(object):
  def addBoldTag(self, s, dict):
    """
    :type s: str
    :type dict: List[str]
    :rtype: str
    """
    intervals = []
    ans = []
    for word in dict:
      start = 0
      loc = s.find(word, start)
      while loc != -1:
        intervals.append([loc, loc + len(word) - 1])
        start = loc + 1
        loc = s.find(word, start)

    intervals = self.merge(intervals)
    d = {}
    for start, end in intervals:
      d[start] = end
    i = 0
    while i < len(s):
      if i in d:
        ans.append("<b>{}</b>".format(s[i:d[i] + 1]))
        i = d[i] + 1
      else:
        ans.append(s[i])
        i += 1
    return "".join(ans)

  def merge(self, intervals):
    ans = []
    for intv in sorted(intervals, key=lambda x: x[0]):
      if ans and ans[-1][1] + 1 >= intv[0]:
        ans[-1][1] = max(ans[-1][1], intv[1])
      else:
        ans += intv,
    return ans
