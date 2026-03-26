class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        
        if k == n:
            return sum(cardPoints)
        
        total = sum(cardPoints)
        window_size = n - k
        
        curr = sum(cardPoints[:window_size])
        min_sum = curr
        
        for i in range(window_size, n):
            curr += cardPoints[i]
            curr -= cardPoints[i - window_size]
            min_sum = min(min_sum, curr)
        
        return total - min_sum
