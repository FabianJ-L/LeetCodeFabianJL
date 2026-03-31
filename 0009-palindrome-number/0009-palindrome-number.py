class Solution(object):
    def isPalindrome(self, x):

        if x < 0:
            return False

        strX = str(x)
        reversedNum = 0
        lenght = len(strX) - 1

        for i, char in enumerate(strX):
            reversedNum = int(char) * (10 ** i) + reversedNum 
            lenght = lenght - 1
        
        if reversedNum == x:
            return True
        
        else:
            return False
        