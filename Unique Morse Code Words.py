class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        a = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        mp = {}
        for i in range(len(a)):
            mp[chr(ord('a') + i)] = a[i] = a[i]
        
        ans = set({})
        for i in words:
            tmp = ""
            for j in i:
                tmp += mp[j]
            ans.add(tmp)
        return len(ans)
