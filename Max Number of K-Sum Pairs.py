from collections import Counter

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        d = Counter(nums)
        ans = 0
        for i in nums:
            if d[i] > 0:
                if k-i == i:
                    ans += d[i]//2
                    d[i] -= (d[i]//2)*2
                elif k - i in d:
                    t1 = min(d[i],d[k-i])
                    ans += t1
                    d[i] -= t1
                    d[k-i] -= t1
        return ans
        
