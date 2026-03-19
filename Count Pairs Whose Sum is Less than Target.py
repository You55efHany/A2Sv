class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        p1 = n - 1
        ans = 0

        for i in range(n):
            while p1 > i and nums[i] + nums[p1] >= target:
                p1 -= 1

            if p1 > i:
                ans += (p1 - i)

        return ans
