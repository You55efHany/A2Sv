class Solution:
    def reverseString(self, s: List[str]) -> None:
        k = s[::-1]
        for i in range(len(k)):
            s[i] = k[i]
        return s
        
