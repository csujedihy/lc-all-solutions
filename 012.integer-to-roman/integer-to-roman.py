class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        ans = ""
        values = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}
        literals = ["M", "D", "C", "L", "X", "V", "I"]
        for idx in [0, 2, 4]:
            k = num / values[literals[idx]]
            re = (num % values[literals[idx]]) / values[literals[idx + 2]]
            ans += k * literals[idx]
            if re >= 9:
                ans += literals[idx + 2] + literals[idx] 
            elif re >= 5:
                ans += literals[idx + 1] + (re - 5) * literals[idx + 2]
            elif re == 4:
                ans += literals[idx + 2] + literals[idx + 1]
            else:
                ans += re * literals[idx + 2]
            num %= values[literals[idx + 2]]
        return ans
        