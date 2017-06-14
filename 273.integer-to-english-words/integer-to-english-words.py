units = {1: "", 100: " Hundred", 1000: " Thousand", 1000000: " Million", 1000000000: " Billion"}
tenToTwenty = {10: "Ten", 11: "Eleven", 12: "Twelve", 13: "Thirteen", 14: "Fourteen", 15: "Fifteen", 16: "Sixteen", 17: "Seventeen", 18: "Eighteen", 19: "Nineteen", 20: "Twenty"}
tens = {2: "Twenty", 3: "Thirty", 4: "Forty", 5: "Fifty", 6: "Sixty", 7: "Seventy", 8: "Eighty", 9: "Ninety"}
digit = {1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine", 10: "Ten"}
class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        global units, tenToTwenty, tens, digit
        ans = []
        def getNum(number):
            global units, tenToTwenty, tens, digit
            divider = 1000
            ans = []
            h = number / 100
            if h != 0:
                ans.append(digit[h] + " Hundred")
            number = number % 100
            if number in tenToTwenty:
                ans.append(tenToTwenty[number])
            else:
                t = number / 10
                if t != 0:
                    ans.append(tens[t])
                number = number % 10
                d = number
                if d != 0:
                    ans.append(digit[d])
            return " ".join(ans)

        divider = 1000000000
        while num > 0:
            res = num / divider
            if res != 0:
                ans.append(getNum(res) + units[divider])
            num = num % divider
            divider /= 1000
        if not ans:
            return "Zero"
        return " ".join(ans)