class Solution(object):
  def fractionAddition(self, expression):
    """
    :type expression: str
    :rtype: str
    """

    def add(a, b):
      if a == "0/1":
        return b

      def gcd(a, b):
        while b != 0:
          a, b = b, a % b
        return a

      (an, ad), (bn, bd) = map(int, a.split("/")), map(int, b.split("/"))
      lcm = (ad * bd) / (gcd(ad, bd))
      an, bn = an * (lcm / ad), bn * (lcm / bd)
      n = an + bn
      g = gcd(n, lcm)
      return str(n / g) + "/" + str(lcm / g)

    expression += "+"
    ans = "0/1"
    start = 0
    for i in range(1, len(expression)):
      if expression[i] in ["+", "-"]:
        num = expression[start:i]
        ans = add(ans, num)
        start = i
    return ans if ans[0] != "+" else ans[1:]
