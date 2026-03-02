class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        dec = {}

        for i in arr1:
            if i in dec:
                dec[i] += 1
            else:
                dec[i] = 1

        ans = list()
        ans2 = list()
        for i in arr2:
            while dec[i] > 0:
                dec[i] -= 1
                ans.append(i)

        for i,j in dec.items():
            while j > 0:
                j -= 1
                ans2.append(i)
        ans2.sort()
        for i in ans2:
            ans.append(i)
        return ans
