import math
class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        ans = 0
        for i in range(len(points)):
            mp = {}
            for j in range(len(points)):
                if i == j:
                    continue
                dis1 = ((points[i][0] - points[j][0]) ** 2) + ((points[i][1] - points[j][1]) ** 2)
                if(dis1 not in mp):
                    mp[dis1] = 1
                else:
                    mp[dis1] += 1
            for j in mp.values():
                if j > 1:
                    ans += math.perm(j,2)
        return ans
