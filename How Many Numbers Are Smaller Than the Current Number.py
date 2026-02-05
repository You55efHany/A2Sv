class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        ans = []

        for i in range(len(nums)):
            ans.append([nums[i],i])
        ans.sort()

        realans = []
        for i in range(len(nums)):
            realans.append([0])
        lst = -1
        jj = 0
        for i in range(len(nums)):
            if lst != ans[i][0]:
                lst = ans[i][0]
                jj = i
            realans[ans[i][1]] = jj

        return realans

