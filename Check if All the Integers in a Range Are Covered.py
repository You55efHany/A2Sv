class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        a = list()
        for i in range(1001):
            a.append(0)
        for i in range(len(ranges)):
            a[ranges[i][0]] += 1
            a[ranges[i][1] + 1] -= 1
        
        
        for i in range(1,101):
            a[i] += a[i - 1]
            
        for i in range(left,right + 1):
            if(a[i] == 0):
                return False
        return True
