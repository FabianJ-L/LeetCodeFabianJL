class Solution(object):
    def romanToInt(self, s):

        num = 0
        listRomanInt = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        for i in range(len(s)):

            if i + 1 < len(s) and listRomanInt[s[i]] < listRomanInt[s[i + 1]]:
                num -= listRomanInt[s[i]]
            else:
                num += listRomanInt[s[i]]

        return num
