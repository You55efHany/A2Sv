class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        a = nums*1
        for i in range(1,len(nums)):
            nums[i] += nums[i-1]
        n = len(nums)
        for i in range(len(nums)):
            #print(nums[i],a[i],end=" ")
            if nums[i] == nums[n-1]-nums[i]+a[i]:
                return i
        return -1
