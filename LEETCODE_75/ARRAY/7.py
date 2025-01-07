# Reverse Words in a String

class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()
        return " ".join(s[::-1])
    
