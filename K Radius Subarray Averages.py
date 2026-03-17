from typing import List

class Solution:
    def static_sliding_window(self, arr, k):
        n = len(arr)
        res = [-1] * n
        window_size = 2 * k + 1
        
        if window_size > n:
            return res
        
        window_sum = sum(arr[:window_size])
        res[k] = window_sum // window_size

        for i in range(k + 1, n - k):
            window_sum += arr[i + k]
            window_sum -= arr[i - k - 1]
            res[i] = window_sum // window_size

        return res

    def getAverages(self, nums: List[int], k: int) -> List[int]:
        return self.static_sliding_window(nums, k)
