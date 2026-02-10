class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        ans: List[int]
        for i in range(len(nums)):
            ans[i] = nums[nums[i] - 1]
        return ans
