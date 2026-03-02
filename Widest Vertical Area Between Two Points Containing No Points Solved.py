class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        x = list()
        for i,j in points:
            x.append(i)
        x.sort()
        ans = 0
        for i in range(1,len(x)):
            ans = max(ans,x[i]-x[i-1])
        return ans
