class Solution(object):
  def findLonelyPixel(self, picture):
    """
    :type picture: List[List[str]]
    :rtype: int
    """
    ans = 0
    col = {}
    row = {}
    for i in range(len(picture)):
      for j in range(len(picture[0])):
        if picture[i][j] == "B":
          row[i] = row.get(i, 0) + 1
          col[j] = col.get(j, 0) + 1

    for i in range(len(picture)):
      for j in range(len(picture[0])):
        if picture[i][j] == "B":
          if row.get(i, 0) == 1 and col.get(j, 0) == 1:
            ans += 1
          elif row.get(i, 0) == 1:
            continue
          else:
            break
    return ans
