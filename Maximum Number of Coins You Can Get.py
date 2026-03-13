from typing import List

class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse=True)
        n = len(piles)
        res = 0

        for i in range(1, 2*n//3, 2):
            res += piles[i]
        
        return res
