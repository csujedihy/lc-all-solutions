class Solution(object):
  def addBinary(self, a, b):
    """
    :type a: str
    :type b: str
    :rtype: str
    """
    diff = abs(len(a) - len(b))
    if len(a) > len(b):
      b = "0" * diff + b
    else:
      a = "0" * diff + a

    ret = ""
    carry = 0
    ai, bi = len(a) - 1, len(b) - 1
    al, bl = len(a), len(b)
    while ai >= 0 and bi >= 0:
      ac, bc = a[ai], b[bi]
      if ac == "1" and bc == "1":
        if carry == 1:
          ret += "1"
        else:
          ret += "0"
        carry = 1
      elif ac == "0" and bc == "0":
        if carry == 1:
          ret += "1"
        else:
          ret += "0"
        carry = 0
      else:
        if carry == 1:
          ret += "0"
        else:
          ret += "1"

      ai -= 1
      bi -= 1

    if carry == 1:
      ret += "1"
    return ret[::-1]
