class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        frq = [0]*len(s)
        for i in shifts:
            if(i[2] == 1):
                if(i[1]+1 < len(s)):
                    frq[i[1]+1] -= 1
                frq[i[0]] += 1
            else:
                if(i[1]+1 < len(s)):
                    frq[i[1]+1] += 1
                frq[i[0]] -= 1
        for i in range(1,len(s)):
            frq[i] += frq[i-1]
        a = list(s)
        for i in range(len(s)):
           a[i] = chr((ord(s[i]) - ord('a') + frq[i]) % 26 + ord('a'))
        return ''.join(a)
            
                
