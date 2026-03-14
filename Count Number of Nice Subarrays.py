from collections import defaultdict

class Solution:
  
    def dynamic_sliding_window(self,arr,tar):
        left = 0
        window_sum = 0
        result = 0

        d = defaultdict(int)
        for right in range(len(arr)):
            if arr[right]%2 == 1:
                window_sum += 1

            while window_sum > tar:
                if arr[left]%2 == 1:
                    window_sum -= 1
                left += 1
            if(window_sum <= tar):
                result += right-left+1
        return result
    
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        return self.dynamic_sliding_window(nums,k)-self.dynamic_sliding_window(nums,k-1)
