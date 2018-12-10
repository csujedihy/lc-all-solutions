class Solution(object):
  def sortTransformedArray(self, nums, a, b, c):
    """
    :type nums: List[int]
    :type a: int
    :type b: int
    :type c: int
    :rtype: List[int]
    """

    def f(x):
      return a * (x ** 2) + b * x + c

    if a == 0:
      if b >= 0:
        return [f(x) for x in nums]
      else:
        return [f(x) for x in reversed(nums)]

    mid = (-1.0) * b / (2.0 * a)
    up, down = [], []

    if a >= 0:
      for num in nums:
        if num >= mid:
          up.append(f(num))
        else:
          down.append(f(num))
      down.reverse()
    else:
      for num in nums:
        if num >= mid:
          down.append(f(num))
        else:
          up.append(f(num))
      down.reverse()

    res = []
    upIdx = 0
    downIdx = 0
    while upIdx < len(up) and downIdx < len(down):
      upTop = up[upIdx]
      downTop = down[downIdx]

      if upTop < downTop:
        res.append(upTop)
        upIdx += 1
      else:
        res.append(downTop)
        downIdx += 1
    if upIdx < len(up):
      res.extend(up[upIdx:len(up)])
    if downIdx < len(down):
      res.extend(down[downIdx:len(down)])
    return res
