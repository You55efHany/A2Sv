class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        a = sorted(list(set(nums)))
        nums.clear()
        for i in a:
            nums.append(i)
