class Solution(object):
  def toHex(self, num):
    """
    :type num: int
    :rtype: str
    """
    d = {0: "0", 1: "1", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9", 10: "a", 11: "b", 12: "c",
         13: "d", 14: "e", 15: "f"}
    ans = ""
    mask = 0xf0000000
    flag = False
    for i in range(0, 8):
      halfb = (num & mask) >> 28
      if halfb != 0:
        flag = True
      if flag:
        ans = ans + d[(num & mask) >> 28]
      num = num << 4
    if ans == "":
      return "0"
    return ans
