class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        curr_sum = numbers[l] + numbers[r]
        while curr_sum != target:
            if(curr_sum > target):
                curr_sum -= numbers[r]
                r -= 1
                curr_sum += numbers[r]
            elif curr_sum < target:
                curr_sum -= numbers[l]
                l += 1
                curr_sum += numbers[l]
        return [l + 1, r + 1]
