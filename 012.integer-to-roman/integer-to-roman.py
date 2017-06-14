d = {1: "I", 5: "V", 10: "X", 50: "L", 100: "C", 500: "D", 1000: "M", 2: "II", 3: "III" ,4: "IV", 6: "VI", 7: "VII", 8: "VIII" ,9: "IX", 20: "XX", 30: "XXX", 40: "XL", 60: "LX", 70: "LXX", 80: "LXXX",90: "XC", 200: "CC", 300: "CCC", 400: "CD", 600: "DC", 700: "DCC", 800: "DCCC", 900: "CM", 2000: "MM", 3000: "MMM" }
class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        global d
        sub = {}
        divider = 1000
        ans = ""
        while num > 0:
            multiple = num / divider
            ans += d.get(multiple * divider, "")
            num = num % divider
            divider /= 10
        return ans
        