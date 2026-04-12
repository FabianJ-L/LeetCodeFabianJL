class Solution(object):
    def mergeAlternately(self, word1, word2):

        output = ""
        i = 0

        while i < len(word1) or i < len(word2):
            if i < len(word1):
                output += word1[i]
            if i < len(word2):
                output += word2[i]
            i += 1

        return output
        