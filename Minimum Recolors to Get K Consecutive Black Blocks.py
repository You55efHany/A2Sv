from collections import Counter
from collections import defaultdict

class Solution:

    def static_sliding_window(self,arr, k):
        n = len(arr)

        # first window
        window_sum = sum(arr[:k])
        result = k-window_sum

        # slide the window
        for i in range(k, n):
            window_sum += arr[i]
            window_sum -= arr[i-k]
            result = min(result, k-window_sum)

        return result

    def minimumRecolors(self, blocks: str, k: int) -> int:
        n = len(blocks)
        a = [0]*n
        for i in range(n):
            if blocks[i] == 'B':
                a[i] = 1
        return self.static_sliding_window(a,k)
            
