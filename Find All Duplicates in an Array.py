from collections import Counter
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]: 
        d = Counter(nums)
        ans = list()
        for i,j in d.items():
            if(j == 2):
                ans.append(i)
        return ans
