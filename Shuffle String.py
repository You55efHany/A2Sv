class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        ans = list()
        for i in range(len(s)):
            ans.append('')
        
        for i in range(len(s)):
            ans[indices[i]] = s[i]
        ans = str(ans).replace('[', '').replace(']', '').replace(', ', '').replace("'", "")
        return ans
