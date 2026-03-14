from collections import defaultdict

class Solution:
  
    def static_sliding_window(self,arr, k):
        n = len(arr)

        window_sum = sum(arr[:k])
        result = window_sum

        for i in range(k, n):
            window_sum += arr[i]
            window_sum -= arr[i-k]
            result = max(result, window_sum)

        return result/k

    def findMaxAverage(self, nums: List[int], k: int) -> float:
        return self.static_sliding_window(nums,k)
