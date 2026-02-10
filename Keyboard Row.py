class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        r1 = set("qwertyuiopQWERTYUIOP")
        r2 = set("asdfghjklASDFGHJKL")
        r3 = set("zxcvbnmZXCVBNM")

        ans = []
        for w in words:
            s = set(w)
            if s.issubset(r1) or s.issubset(r2) or s.issubset(r3):
                ans.append(w)
        return ans



        
