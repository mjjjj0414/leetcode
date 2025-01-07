# Problem: Merge Strings Alternately
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        words = ""
        num = 0

        while num < len(word1) or num < len(word2):
            if num < len(word1):
                words += word1[num]  
            if num < len(word2):
                words += word2[num] 
            num += 1 
        return words
    