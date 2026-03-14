from collections import defaultdict

class Solution:
  
    def dynamic_sliding_window(self,arr):
        left = 0
        window_sum = 0
        result = 0

        d = defaultdict(int)
        for right in range(len(arr)):
            d[arr[right]] += 1

            while d[arr[right]] >= 2:
                d[arr[left]] -= 1
                left += 1
            result = max(result, right - left + 1)
        return result

    def lengthOfLongestSubstring(self, s: str) -> int:
        a = list(s)
        return(self.dynamic_sliding_window(a))
