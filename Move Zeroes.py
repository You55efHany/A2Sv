class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        a = sorted(nums, key=lambda x: 1 if x == 0 else 0)
        nums[:] = a
