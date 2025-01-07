class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()
        return " ".join(s[::-1])
    

solution = Solution()
print(solution.reverseWords("the sky is blue"))