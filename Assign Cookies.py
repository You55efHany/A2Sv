class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        p1 = 0
        p2 = 0
        ans = 0
        while p1 < len(s) and p2 < len(g):
            if s[p1] >= g[p2]:
                p2 += 1
                ans += 1
            p1 += 1
        return ans
