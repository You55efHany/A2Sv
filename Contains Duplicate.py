class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        c = set(nums)
        return len(c) < len(nums)
        
