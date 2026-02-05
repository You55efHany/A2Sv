class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        tmp = len(nums) / 3
        mp = {}
        for i in nums:
            if i  in mp:
                mp[i] += 1
            else:
                mp[i] = 1
        
        ans = list()
        for i,j in mp.items():
            if j > tmp:
                ans.append(i)
        return ans

        
