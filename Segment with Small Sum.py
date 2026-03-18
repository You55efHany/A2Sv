def dynamic_sliding_window(arr, target):
    left = 0
    window_sum = 0
    result = 0
    
    for right in range(len(arr)):
        window_sum += arr[right]
        
        while window_sum > target:
            window_sum -= arr[left]
            left += 1
        
        result = max(result, right - left + 1)
    return result

n,k = map(int,input().split())
a = list(map(int,input().split()))
print(dynamic_sliding_window(a,k))
