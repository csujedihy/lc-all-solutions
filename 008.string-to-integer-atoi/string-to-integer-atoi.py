class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        INT_MAX = 2147483647
        INT_MIN = -2147483648
        ans = 0
        str = str.lstrip()
        signFlag = 1
        if str and str[0] in ["+", "-"]:
            if str[0] == "-":
                signFlag = -1
            str = str[1:]

        for c in str:
            if not c.isdigit():
                if ans == 0:
                    return ans
                break
            num = int(c)
            ans *= 10
            ans += num
        ans = ans * signFlag
        if ans > INT_MAX:
            ans = INT_MAX
        if ans < INT_MIN:
            ans = INT_MIN
        return ans