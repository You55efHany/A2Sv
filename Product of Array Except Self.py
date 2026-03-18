class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        t1 = 1
        z = 0
        for i in nums:
            if i == 0:
                z += 1
            else:
                t1 *= i
        ans = [0]*len(nums)
        for i in range(len(nums)):
            if z >= 2:
                break
            if z == 1:
                if nums[i] == 0:
                    ans[i] = t1
            else:
                ans[i] = t1 // nums[i]
        return ans
                
