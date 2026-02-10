from collections import defaultdict
class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        ans = 0
        mp = defaultdict(lambda: 0)
        mc = defaultdict(lambda: 0)

        re = list()
        for x,y in queries:
            mc[mp[x]] -= 1

            if mc[mp[x]] == 0:
                ans -= 1

            mp[x] = y
            mp[y] += 1

            if mp[y] == 1:
                ans += 1
            re.append(ans)
        return ans
            
                
